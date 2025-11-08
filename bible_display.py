#!/usr/bin/env python3
"""
Daily Bible Verse Display for Waveshare 2.13" v4 E-Paper
Displays a random Bible verse that changes daily
"""

import os
import sys
import json
import random
import logging
from datetime import datetime
from pathlib import Path

# Import Waveshare e-paper library
# Make sure the waveshare library is installed
try:
    from waveshare_epd import epd2in13_V4
    from PIL import Image, ImageDraw, ImageFont
except ImportError as e:
    print(f"Error importing libraries: {e}")
    print("Please run the setup script first!")
    sys.exit(1)

# Configuration
SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = SCRIPT_DIR / "config.json"
BIBLE_DATA_DIR = SCRIPT_DIR / "bible_data"
LOG_FILE = SCRIPT_DIR / "bible_display.log"

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)


def load_config():
    """Load configuration from config.json"""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        logging.info(f"Loaded configuration: {config}")
        return config
    except FileNotFoundError:
        logging.error(f"Config file not found: {CONFIG_FILE}")
        logging.info("Using default configuration")
        return {
            "translation": "NIV",
            "font_size_reference": 14,
            "font_size_text": 12,
            "display_rotation": 0
        }
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing config file: {e}")
        return {}


def load_bible_data(translation):
    """Load Bible data from JSON file"""
    bible_file = BIBLE_DATA_DIR / f"{translation.lower()}.json"
    
    if not bible_file.exists():
        logging.error(f"Bible data file not found: {bible_file}")
        logging.error(f"Available translations in {BIBLE_DATA_DIR}:")
        if BIBLE_DATA_DIR.exists():
            for f in BIBLE_DATA_DIR.glob("*.json"):
                logging.error(f"  - {f.stem.upper()}")
        return None
    
    try:
        with open(bible_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.info(f"Loaded Bible data from {bible_file}")
        return data
    except Exception as e:
        logging.error(f"Error loading Bible data: {e}")
        return None


def get_daily_verse(bible_data):
    """
    Get a verse for this hour. Uses date + hour as seed for consistency.
    The same verse will be shown for the entire hour, then change every hour.
    """
    # Use current date + hour as seed for reproducible randomness
    now = datetime.now()
    # Format: YYYYMMDDHH (e.g., 2025110714 for Nov 7, 2025 at 2 PM)
    seed = int(now.strftime("%Y%m%d%H"))
    random.seed(seed)
    
    # Select a random book
    books = bible_data.get('books', [])
    if not books:
        logging.error("No books found in Bible data")
        return None
    
    book = random.choice(books)
    book_name = book.get('name', 'Unknown')
    chapters = book.get('chapters', [])
    
    if not chapters:
        logging.error(f"No chapters found in {book_name}")
        return None
    
    # Select a random chapter
    chapter = random.choice(chapters)
    chapter_num = chapter.get('chapter', 1)
    verses = chapter.get('verses', [])
    
    if not verses:
        logging.error(f"No verses found in {book_name} {chapter_num}")
        return None
    
    # Select a random verse
    verse = random.choice(verses)
    verse_num = verse.get('verse', 1)
    text = verse.get('text', '')
    
    reference = f"{book_name} {chapter_num}:{verse_num}"
    
    logging.info(f"Selected verse: {reference}")
    return {
        'reference': reference,
        'text': text
    }


def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        current_line.append(word)
        test_line = ' '.join(current_line)
        bbox = font.getbbox(test_line)
        width = bbox[2] - bbox[0]
        
        if width > max_width:
            if len(current_line) == 1:
                # Single word too long, add it anyway
                lines.append(test_line)
                current_line = []
            else:
                # Remove last word and start new line
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines


def create_image(verse_data, config):
    """Create an image with the verse text"""
    # E-paper display size for 2.13" V4
    width = 122
    height = 250
    
    # Create blank image
    image = Image.new('1', (width, height), 255)  # 255 = white
    draw = ImageDraw.Draw(image)
    
    # Load fonts
    try:
        font_text = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 
                                       config.get('font_size_text', 12))
        font_ref = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 
                                      config.get('font_size_reference', 14))
    except Exception as e:
        logging.warning(f"Could not load custom fonts: {e}. Using default.")
        font_text = ImageFont.load_default()
        font_ref = ImageFont.load_default()
    
    # Prepare text
    reference = verse_data['reference']
    text = verse_data['text']
    
    # Calculate layout
    margin = 5
    y_position = margin
    
    # Draw reference at top
    ref_lines = wrap_text(reference, font_ref, width - 2 * margin)
    for line in ref_lines:
        draw.text((margin, y_position), line, font=font_ref, fill=0)
        bbox = font_ref.getbbox(line)
        y_position += bbox[3] - bbox[1] + 3
    
    y_position += 8  # Space between reference and text
    
    # Draw verse text
    text_lines = wrap_text(text, font_text, width - 2 * margin)
    for line in text_lines:
        if y_position > height - 20:  # Stop if we run out of space
            break
        draw.text((margin, y_position), line, font=font_text, fill=0)
        bbox = font_text.getbbox(line)
        y_position += bbox[3] - bbox[1] + 2
    
    # Draw date at bottom
    date_text = datetime.now().strftime("%B %d, %Y")
    date_bbox = font_text.getbbox(date_text)
    date_width = date_bbox[2] - date_bbox[0]
    draw.text(((width - date_width) // 2, height - 15), date_text, font=font_text, fill=0)
    
    return image


def display_on_epaper(image, config):
    """Display the image on the e-paper display"""
    try:
        logging.info("Initializing e-paper display...")
        epd = epd2in13_V4.EPD()
        epd.init()
        epd.Clear(0xFF)
        
        # Rotate image if needed
        rotation = config.get('display_rotation', 0)
        if rotation != 0:
            image = image.rotate(rotation, expand=True)
        
        # Display image
        logging.info("Displaying image on e-paper...")
        epd.display(epd.getbuffer(image))
        
        # Put display to sleep to save power
        logging.info("Putting display to sleep...")
        epd.sleep()
        
        logging.info("Display update complete!")
        return True
        
    except Exception as e:
        logging.error(f"Error displaying on e-paper: {e}")
        return False


def main():
    """Main function"""
    logging.info("=" * 50)
    logging.info("Starting Hourly Bible Verse Display")
    logging.info("=" * 50)
    
    # Load configuration
    config = load_config()
    translation = config.get('translation', 'NIV')
    
    # Load Bible data
    logging.info(f"Loading Bible translation: {translation}")
    bible_data = load_bible_data(translation)
    
    if bible_data is None:
        logging.error("Could not load Bible data. Exiting.")
        sys.exit(1)
    
    # Get this hour's verse
    verse_data = get_daily_verse(bible_data)
    
    if verse_data is None:
        logging.error("Could not get verse. Exiting.")
        sys.exit(1)
    
    logging.info(f"Verse: {verse_data['reference']}")
    logging.info(f"Text preview: {verse_data['text'][:50]}...")
    
    # Create image
    image = create_image(verse_data, config)
    
    # Save image for debugging
    debug_image_path = SCRIPT_DIR / "last_displayed.png"
    image.save(debug_image_path)
    logging.info(f"Saved debug image to {debug_image_path}")
    
    # Display on e-paper
    success = display_on_epaper(image, config)
    
    if success:
        logging.info("Successfully updated display!")
    else:
        logging.error("Failed to update display")
        sys.exit(1)


if __name__ == "__main__":
    main()
