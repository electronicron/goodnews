#!/usr/bin/env python3
"""
Download World English Bible (WEB) - Modern English Translation
Public Domain, Modern English, easier to read than KJV
"""

import json
import urllib.request
import os

print("=" * 70)
print("World English Bible (WEB) Downloader")
print("=" * 70)
print()
print("Downloading the World English Bible - a modern English translation")
print("in the public domain.")
print()

# Create bible_data directory
os.makedirs('bible_data', exist_ok=True)

# Download from thiagobodruk/bible repository
url = "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_bbe.json"

print("Downloading from GitHub...")
print("Source: https://github.com/thiagobodruk/bible")
print()

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    
    print("✓ Download successful!")
    print()
    print("Converting to display format...")
    
    # The thiagobodruk format is:
    # [
    #   {
    #     "abbrev": "gn",
    #     "name": "Genesis",
    #     "chapters": [
    #       ["verse 1", "verse 2", ...],  # Chapter 1
    #       ["verse 1", "verse 2", ...]   # Chapter 2
    #     ]
    #   }
    # ]
    
    converted_books = []
    total_verses = 0
    
    for book in data:
        book_name = book.get('name', 'Unknown')
        chapters_data = book.get('chapters', [])
        
        converted_chapters = []
        for chapter_index, verses_list in enumerate(chapters_data, 1):
            verses = []
            for verse_index, verse_text in enumerate(verses_list, 1):
                verses.append({
                    'verse': verse_index,
                    'text': verse_text
                })
                total_verses += 1
            
            converted_chapters.append({
                'chapter': chapter_index,
                'verses': verses
            })
        
        converted_books.append({
            'name': book_name,
            'chapters': converted_chapters
        })
        
        print(f"  ✓ {book_name}")
    
    # Create final structure
    web_bible = {
        "translation": "WEB",
        "books": converted_books
    }
    
    output_file = 'bible_data/web.json'
    print()
    print(f"Saving to {output_file}...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(web_bible, f, indent=2, ensure_ascii=False)
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    
    print("✓ Complete!")
    print()
    print("=" * 70)
    print("Download Complete!")
    print("=" * 70)
    print()
    print(f"File: {output_file}")
    print(f"Size: {file_size:.1f} MB")
    print(f"Books: {len(converted_books)}")
    print(f"Verses: {total_verses:,}")
    print()
    print("The World English Bible uses modern English and is easier to read")
    print("than the King James Version while remaining accurate.")
    print()
    print("To use this translation:")
    print("  1. Edit config.json")
    print("  2. Change: \"translation\": \"WEB\"")
    print("  3. Run: python3 bible_display.py")
    print()
    
except Exception as e:
    print(f"✗ Error: {e}")
    print()
    print("Troubleshooting:")
    print("1. Check your internet connection")
    print("2. Try again in a few moments")
    print("3. Download manually from:")
    print("   https://github.com/thiagobodruk/bible")
    sys.exit(1)
