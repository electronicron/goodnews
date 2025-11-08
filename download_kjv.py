#!/usr/bin/env python3
"""
Download Complete KJV Bible in JSON Format
This script downloads the KJV Bible and converts it to the format needed for your display
"""

import json
import urllib.request
import os
import sys

print("=" * 70)
print("KJV Bible Downloader")
print("=" * 70)
print()
print("This will download the complete King James Version Bible")
print("and format it for your e-paper display.")
print()

# Create bible_data directory
os.makedirs('bible_data', exist_ok=True)

# Method 1: Download from GitHub (aruljohn/Bible-kjv)
# This is a well-maintained repository with each book as a separate JSON file

print("Step 1: Downloading KJV Bible data from GitHub...")
print("Source: https://github.com/aruljohn/Bible-kjv")
print()

base_url = "https://raw.githubusercontent.com/aruljohn/Bible-kjv/master/"

# List of all 66 books in order
books_list = [
    # Old Testament
    ("Genesis", "Genesis"),
    ("Exodus", "Exodus"),
    ("Leviticus", "Leviticus"),
    ("Numbers", "Numbers"),
    ("Deuteronomy", "Deuteronomy"),
    ("Joshua", "Joshua"),
    ("Judges", "Judges"),
    ("Ruth", "Ruth"),
    ("1 Samuel", "1 Samuel"),
    ("2 Samuel", "2 Samuel"),
    ("1 Kings", "1 Kings"),
    ("2 Kings", "2 Kings"),
    ("1 Chronicles", "1 Chronicles"),
    ("2 Chronicles", "2 Chronicles"),
    ("Ezra", "Ezra"),
    ("Nehemiah", "Nehemiah"),
    ("Esther", "Esther"),
    ("Job", "Job"),
    ("Psalms", "Psalms"),
    ("Proverbs", "Proverbs"),
    ("Ecclesiastes", "Ecclesiastes"),
    ("Song of Solomon", "Song of Solomon"),
    ("Isaiah", "Isaiah"),
    ("Jeremiah", "Jeremiah"),
    ("Lamentations", "Lamentations"),
    ("Ezekiel", "Ezekiel"),
    ("Daniel", "Daniel"),
    ("Hosea", "Hosea"),
    ("Joel", "Joel"),
    ("Amos", "Amos"),
    ("Obadiah", "Obadiah"),
    ("Jonah", "Jonah"),
    ("Micah", "Micah"),
    ("Nahum", "Nahum"),
    ("Habakkuk", "Habakkuk"),
    ("Zephaniah", "Zephaniah"),
    ("Haggai", "Haggai"),
    ("Zechariah", "Zechariah"),
    ("Malachi", "Malachi"),
    # New Testament
    ("Matthew", "Matthew"),
    ("Mark", "Mark"),
    ("Luke", "Luke"),
    ("John", "John"),
    ("Acts", "Acts"),
    ("Romans", "Romans"),
    ("1 Corinthians", "1 Corinthians"),
    ("2 Corinthians", "2 Corinthians"),
    ("Galatians", "Galatians"),
    ("Ephesians", "Ephesians"),
    ("Philippians", "Philippians"),
    ("Colossians", "Colossians"),
    ("1 Thessalonians", "1 Thessalonians"),
    ("2 Thessalonians", "2 Thessalonians"),
    ("1 Timothy", "1 Timothy"),
    ("2 Timothy", "2 Timothy"),
    ("Titus", "Titus"),
    ("Philemon", "Philemon"),
    ("Hebrews", "Hebrews"),
    ("James", "James"),
    ("1 Peter", "1 Peter"),
    ("2 Peter", "2 Peter"),
    ("1 John", "1 John"),
    ("2 John", "2 John"),
    ("3 John", "3 John"),
    ("Jude", "Jude"),
    ("Revelation", "Revelation"),
]

all_books = []
total_verses = 0

print("Downloading 66 books...")
print("This may take a minute or two...")
print()

for i, (filename, display_name) in enumerate(books_list, 1):
    # Format the URL (spaces become %20)
    url = base_url + filename.replace(" ", "%20") + ".json"
    
    try:
        print(f"  [{i:2d}/66] Downloading {display_name}...", end=" ")
        
        with urllib.request.urlopen(url) as response:
            book_data = json.loads(response.read().decode())
        
        # Convert to our format
        converted_chapters = []
        for chapter in book_data.get('chapters', []):
            chapter_num = chapter.get('chapter')
            verses_list = []
            
            for verse in chapter.get('verses', []):
                verses_list.append({
                    'verse': verse.get('verse'),
                    'text': verse.get('text', '')
                })
            
            converted_chapters.append({
                'chapter': chapter_num,
                'verses': verses_list
            })
            total_verses += len(verses_list)
        
        all_books.append({
            'name': display_name,
            'chapters': converted_chapters
        })
        
        print("✓")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("Continuing with other books...")

print()
print(f"Successfully downloaded {len(all_books)} books with {total_verses:,} verses!")
print()

# Create the final JSON structure
kjv_bible = {
    "translation": "KJV",
    "books": all_books
}

# Save to file
output_file = 'bible_data/kjv.json'
print(f"Step 2: Saving to {output_file}...")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(kjv_bible, f, indent=2, ensure_ascii=False)

# Get file size
file_size = os.path.getsize(output_file) / (1024 * 1024)  # Convert to MB

print("✓ Complete!")
print()
print("=" * 70)
print("Download Complete!")
print("=" * 70)
print()
print(f"File: {output_file}")
print(f"Size: {file_size:.1f} MB")
print(f"Books: {len(all_books)}")
print(f"Verses: {total_verses:,}")
print()
print("What's next?")
print("1. Test the display: python3 bible_display.py")
print("2. Update config.json if needed (should already be set to KJV)")
print()
print("To use this translation:")
print("  Edit config.json and set: \"translation\": \"KJV\"")
print()
