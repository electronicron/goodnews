#!/usr/bin/env python3
"""
Bible Display for Waveshare 2.13" v4 E-Paper
Supports both verse and chapter display modes
- Verse mode: Random verse every hour
- Chapter mode: 4 chapters per day (every 6 hours), sequential or random
"""

import os
import sys
import json
import random
import logging
from datetime import datetime
from pathlib import Path

# Import Waveshare e-paper library
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
STATE_FILE = SCRIPT_DIR / "chapter_state.json"

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
        return {
            "translation": "KJV",
            "display_mode": "verse",
            "chapter_mode": "sequential",
            "chapters_per_day": 4,
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
        logging.info(f"Loaded Bible translation: {translation}")
        return data
    except Exception as e:
        logging.error(f"Error loading Bible data: {e}")
        return None


def load_chapter_state():
    """Load the current chapter state for sequential mode"""
    try:
        if STATE_FILE.exists():
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        else:
            # Initialize state
            return {
                "book_index": 0,
                "chapter_index": 0,
                "last_date": ""
            }
    except Exception as e:
        logging.error(f"Error loading chapter state: {e}")
        return {"book_index": 0, "chapter_index": 0, "last_date": ""}


def save_chapter_state(state):
    """Save the current chapter state for sequential mode"""
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump(state, f, indent=2)
        logging.info(f"Saved chapter state: {state}")
    except Exception as e:
        logging.error(f"Error saving chapter state: {e}")


def get_chapter_period():
    """
    Get which chapter period of the day we're in (0-3)
    Divides day into 4 periods of 6 hours each:
    Period 0: 00:00-05:59
    Period 1: 06:00-11:59
    Period 2: 12:00-17:59
    Period 3: 18:00-23:59
    """
    now = datetime.now()
    hour = now.hour
    return hour // 6  # 0, 1, 2, or 3


def get_daily_verse(bible_data):
    """
    Get a verse for this hour. Uses date + hour as seed for consistency.
    The same verse will be shown for the entire hour, then change every hour.
    """
    now = datetime.now()
    seed = int(now.strftime("%Y%m%d%H"))
    random.seed(seed)
    
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
    
    chapter = random.choice(chapters)
    chapter_num = chapter.get('chapter', 1)
    verses = chapter.get('verses', [])
    
    if not verses:
        logging.error(f"No verses found in {book_name} {chapter_num}")
        return None
    
    verse = random.choice(verses)
    verse_num = verse.get('verse', 1)
    text = verse.get('text', '')
    
    reference = f"{book_name} {chapter_num}:{verse_num}"
    
    logging.info(f"Selected verse: {reference}")
    return {
        'reference': reference,
        'text': text,
        'type': 'verse'
    }


def get_chapter_sequential(bible_data):
    """
    Get the next chapter in sequential order.
    Advances through the Bible one chapter at a time.
    """
    books = bible_data.get('books', [])
    if not books:
        logging.error("No books found in Bible data")
        return None
    
    state = load_chapter_state()
    book_index = state.get('book_index', 0)
    chapter_index = state.get('chapter_index', 0)
    
    # Wrap around if we've gone past the end
    if book_index >= len(books):
        book_index = 0
        chapter_index = 0
    
    book = books[book_index]
    book_name = book.get('name', 'Unknown')
    chapters = book.get('chapters', [])
    
    if chapter_index >= len(chapters):
        # Move to next book
        book_index += 1
        chapter_index = 0
        if book_index >= len(books):
            book_index = 0
        book = books[book_index]
        book_name = book.get('name', 'Unknown')
        chapters = book.get('chapters', [])
    
    chapter = chapters[chapter_index]
    chapter_num = chapter.get('chapter', 1)
    verses = chapter.get('verses', [])
    
    # Prepare chapter text (first several verses or summary)
    text = get_chapter_text(verses, book_name, chapter_num)
    
    reference = f"{book_name} {chapter_num}"
    
    # Advance to next chapter for next time
    chapter_index += 1
    state['book_index'] = book_index
    state['chapter_index'] = chapter_index
    state['last_date'] = datetime.now().strftime("%Y-%m-%d")
    save_chapter_state(state)
    
    logging.info(f"Selected chapter (sequential): {reference}")
    return {
        'reference': reference,
        'text': text,
        'type': 'chapter',
        'verse_count': len(verses)
    }


def get_chapter_random(bible_data):
    """
    Get a random chapter from the Bible.
    Uses date + period as seed for consistency within 6-hour periods.
    """
    now = datetime.now()
    period = get_chapter_period()
    seed = int(now.strftime(f"%Y%m%d{period}"))
    random.seed(seed)
    
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
    
    chapter = random.choice(chapters)
    chapter_num = chapter.get('chapter', 1)
    verses = chapter.get('verses', [])
    
    text = get_chapter_text(verses, book_name, chapter_num)
    
    reference = f"{book_name} {chapter_num}"
    
    logging.info(f"Selected chapter (random): {reference}")
    return {
        'reference': reference,
        'text': text,
        'type': 'chapter',
        'verse_count': len(verses)
    }


def get_chapter_text(verses, book_name, chapter_num):
    """
    Create display text for a chapter.
    Shows first few verses with indication of total verses.
    """
    if not verses:
        return "Chapter text not available"
    
    # For short chapters (5 or fewer verses), show all
    if len(verses) <= 5:
        text_parts = []
        for v in verses:
            verse_num = v.get('verse', 1)
            verse_text = v.get('text', '')
            text_parts.append(f"{verse_num}. {verse_text}")
        return " ".join(text_parts)
    
    # For longer chapters, show first 3 verses
    text_parts = []
    for v in verses[:3]:
        verse_num = v.get('verse', 1)
        verse_text = v.get('text', '')
        text_parts.append(f"{verse_num}. {verse_text}")
    
    text_parts.append(f"... ({len(verses)} verses total)")
    return " ".join(text_parts)


def get_content(bible_data, config):
    """
    Get content to display based on configuration.
    Returns either a verse or a chapter depending on display_mode.
    """
    display_mode = config.get('display_mode', 'verse').lower()
    
    if display_mode == 'chapter':
        chapter_mode = config.get('chapter_mode', 'sequential').lower()
        if chapter_mode == 'sequential':
            return get_chapter_sequential(bible_data)
        else:  # random
            return get_chapter_random(bible_data)
    else:  # verse mode (default)
        return get_daily_verse(bible_data)


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
                lines.append(test_line)
                current_line = []
            else:
                current_line.pop()
                lines.append(' '.join(current_line))
                current_line = [word]
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines


def create_image(content, config):
    """Create an image with the verse or chapter text"""
    # Display dimensions (Waveshare 2.13" V4: 122x250)
    width = 250
    height = 122
    
    rotation = config.get('display_rotation', 0)
    if rotation in [90, 270]:
        width, height = height, width
    
    image = Image.new('1', (width, height), 255)  # 255: white
    draw = ImageDraw.Draw(image)
    
    # Load fonts
    font_size_ref = config.get('font_size_reference', 14)
    font_size_text = config.get('font_size_text', 12)
    
    try:
        font_ref = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size_ref)
        font_text = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', font_size_text)
        font_date = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 10)
    except:
        font_ref = ImageFont.load_default()
        font_text = ImageFont.load_default()
        font_date = ImageFont.load_default()
    
    # Get content
    reference = content['reference']
    text = content['text']
    content_type = content.get('type', 'verse')
    
    # Layout
    margin = 5
    y_position = margin
    
    # Draw reference
    draw.text((margin, y_position), reference, font=font_ref, fill=0)
    ref_bbox = font_ref.getbbox(reference)
    y_position += (ref_bbox[3] - ref_bbox[1]) + 8
    
    # Draw separator line
    draw.line([(margin, y_position), (width - margin, y_position)], fill=0, width=1)
    y_position += 8
    
    # Draw text
    max_width = width - (2 * margin)
    lines = wrap_text(text, font_text, max_width)
    
    # Limit lines to fit on display
    max_lines = 6 if content_type == 'verse' else 5
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        if content_type == 'chapter' and 'verse_count' in content:
            lines[-1] = lines[-1][:40] + "..."
    
    for line in lines:
        draw.text((margin, y_position), line, font=font_text, fill=0)
        line_bbox = font_text.getbbox(line)
        y_position += (line_bbox[3] - line_bbox[1]) + 2
    
    # Draw date and mode at bottom
    date_str = datetime.now().strftime("%m/%d/%Y")
    if content_type == 'chapter':
        period = get_chapter_period() + 1
        mode_str = f"Ch {period}/4"
        date_str = f"{date_str} • {mode_str}"
    
    date_bbox = font_date.getbbox(date_str)
    date_x = width - margin - (date_bbox[2] - date_bbox[0])
    date_y = height - margin - (date_bbox[3] - date_bbox[1])
    draw.text((date_x, date_y), date_str, font=font_date, fill=0)
    
    # Apply rotation if needed
    if rotation == 90:
        image = image.rotate(90, expand=True)
    elif rotation == 180:
        image = image.rotate(180)
    elif rotation == 270:
        image = image.rotate(270, expand=True)
    
    return image


def update_display(image):
    """Update the e-paper display with the image"""
    try:
        epd = epd2in13_V4.EPD()
        logging.info("Initializing e-paper display...")
        epd.init()
        epd.Clear(0xFF)
        
        logging.info("Updating display...")
        epd.display(epd.getbuffer(image))
        
        logging.info("Putting display to sleep...")
        epd.sleep()
        
        logging.info("Display updated successfully!")
        return True
    except Exception as e:
        logging.error(f"Error updating display: {e}")
        return False


def main():
    """Main function"""
    logging.info("=" * 50)
    logging.info("Starting Bible Display")
    logging.info("=" * 50)
    
    # Load configuration
    config = load_config()
    translation = config.get('translation', 'KJV')
    display_mode = config.get('display_mode', 'verse')
    
    logging.info(f"Display mode: {display_mode}")
    if display_mode == 'chapter':
        chapter_mode = config.get('chapter_mode', 'sequential')
        logging.info(f"Chapter mode: {chapter_mode}")
        period = get_chapter_period() + 1
        logging.info(f"Chapter period: {period}/4")
    
    # Load Bible data
    bible_data = load_bible_data(translation)
    if not bible_data:
        logging.error("Failed to load Bible data")
        return 1
    
    # Get content to display
    content = get_content(bible_data, config)
    if not content:
        logging.error("Failed to get content")
        return 1
    
    # Create image
    image = create_image(content, config)
    
    # Save image for debugging
    debug_image_path = SCRIPT_DIR / "last_displayed.png"
    image.save(debug_image_path)
    logging.info(f"Saved debug image to {debug_image_path}")
    
    # Update display
    success = update_display(image)
    
    if success:
        logging.info("Successfully updated display!")
        return 0
    else:
        logging.error("Failed to update display")
        return 1


if __name__ == "__main__":
    sys.exit(main())
