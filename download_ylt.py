#!/usr/bin/env python3
"""
Download Complete Young's Literal Translation (YLT)
Most literal English translation, public domain
"""

import json
import urllib.request
import os
import sys

print("=" * 70)
print("Young's Literal Translation (YLT) Downloader")
print("=" * 70)
print()
print("Young's Literal Translation (1898) is the most literal")
print("word-for-word English translation in the public domain.")
print()

# Create bible_data directory
os.makedirs('bible_data', exist_ok=True)

# GetBible API URL for complete YLT
url = "https://api.getbible.net/v2/ylt.json"

print("Step 1: Downloading YLT Bible...")
print(f"Source: {url}")
print()

try:
    print("Fetching data (this may take 30-60 seconds)...")
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=120) as response:
        data = json.loads(response.read().decode('utf-8'))
    
    print("✓ Download successful!")
    print()
    print("Step 2: Converting to display format...")
    
    converted_books = []
    total_verses = 0
    total_chapters = 0
    
    for book in data.get('books', []):
        book_name = book.get('name', 'Unknown')
        print(f"  Processing: {book_name}")
        
        converted_chapters = []
        for chapter in book.get('chapters', []):
            chapter_num = chapter.get('chapter', 0)
            
            verses_list = []
            for verse in chapter.get('verses', []):
                verse_num = verse.get('verse', 0)
                verse_text = verse.get('text', '')
                
                verses_list.append({
                    'verse': verse_num,
                    'text': verse_text
                })
                total_verses += 1
            
            converted_chapters.append({
                'chapter': chapter_num,
                'verses': verses_list
            })
            total_chapters += 1
        
        converted_books.append({
            'name': book_name,
            'chapters': converted_chapters
        })
    
    print()
    print(f"✓ Processed {len(converted_books)} books")
    print(f"  Total chapters: {total_chapters}")
    print(f"  Total verses: {total_verses:,}")
    
    if len(converted_books) != 66:
        print()
        print(f"⚠️  WARNING: Expected 66 books, but got {len(converted_books)}")
    else:
        print("✓ All 66 books present!")
    
    print()
    print("Step 3: Saving to file...")
    
    ylt_bible = {
        "translation": "YLT",
        "books": converted_books
    }
    
    output_file = 'bible_data/ylt.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(ylt_bible, f, indent=2, ensure_ascii=False)
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    
    print("✓ Complete!")
    print()
    print("=" * 70)
    print("Download Complete!")
    print("=" * 70)
    print()
    print(f"Translation: Young's Literal Translation (YLT)")
    print(f"Translator: Robert Young")
    print(f"Year: 1898")
    print(f"Style: Extremely literal, word-for-word")
    print(f"File: {output_file}")
    print(f"Size: {file_size:.1f} MB")
    print(f"Books: {len(converted_books)} / 66")
    print(f"Chapters: {total_chapters:,}")
    print(f"Verses: {total_verses:,}")
    print()
    
    if len(converted_books) == 66:
        print("✅ SUCCESS: Complete Bible downloaded!")
        print()
        print("YLT is the most literal English translation available.")
        print("It closely follows the word order and structure of the")
        print("original Hebrew and Greek texts.")
        print()
        print("To use this translation:")
        print("1. Edit config.json")
        print("2. Change: \"translation\": \"YLT\"")
        print("3. Run: python3 bible_display.py")
        print()
        print("Example verse (John 3:16 in YLT):")
        print("'for God did so love the world, that His Son -- the only begotten")
        print(" -- He gave, that every one who is believing in him may not perish,")
        print(" but may have life age-during.'")
        print()
    else:
        print("⚠️  WARNING: Download may be incomplete")
        sys.exit(1)
    
except urllib.error.URLError as e:
    print(f"✗ Network Error: {e}")
    print()
    print("Check your internet connection and try again.")
    sys.exit(1)
    
except Exception as e:
    print(f"✗ Error: {e}")
    print()
    print("Please try running the script again.")
    sys.exit(1)
