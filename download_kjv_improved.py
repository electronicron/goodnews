#!/usr/bin/env python3
"""
Download Complete KJV Bible - IMPROVED VERSION
Uses GetBible API for more reliable download
"""

import json
import urllib.request
import os
import sys

print("=" * 70)
print("King James Version (KJV) Bible Downloader - IMPROVED")
print("=" * 70)
print()
print("Downloading complete KJV Bible from GetBible API...")
print("This method downloads the entire Bible in one file - much faster!")
print()

# Create bible_data directory
os.makedirs('bible_data', exist_ok=True)

# GetBible API URL for complete KJV
url = "https://api.getbible.net/v2/kjv.json"

print("Step 1: Downloading KJV Bible...")
print(f"Source: {url}")
print()

try:
    print("Fetching data (this may take 30-60 seconds)...")
    
    # Download with timeout
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=120) as response:
        data = json.loads(response.read().decode('utf-8'))
    
    print("✓ Download successful!")
    print()
    print("Step 2: Converting to display format...")
    
    # GetBible format structure:
    # {
    #   "translation": "...",
    #   "abbreviation": "...",
    #   "books": [
    #     {
    #       "nr": 1,
    #       "name": "Genesis",
    #       "chapters": [
    #         {
    #           "chapter": 1,
    #           "verses": [
    #             {
    #               "verse": 1,
    #               "name": "Genesis 1:1",
    #               "text": "In the beginning..."
    #             }
    #           ]
    #         }
    #       ]
    #     }
    #   ]
    # }
    
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
    
    # Verify we have all 66 books
    if len(converted_books) != 66:
        print()
        print(f"⚠️  WARNING: Expected 66 books, but got {len(converted_books)}")
        print("    The download may be incomplete.")
    else:
        print("✓ All 66 books present!")
    
    print()
    print("Step 3: Saving to file...")
    
    # Create final JSON structure
    kjv_bible = {
        "translation": "KJV",
        "books": converted_books
    }
    
    output_file = 'bible_data/kjv.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(kjv_bible, f, indent=2, ensure_ascii=False)
    
    file_size = os.path.getsize(output_file) / (1024 * 1024)
    
    print("✓ Complete!")
    print()
    print("=" * 70)
    print("Download Complete!")
    print("=" * 70)
    print()
    print(f"Translation: King James Version (KJV)")
    print(f"File: {output_file}")
    print(f"Size: {file_size:.1f} MB")
    print(f"Books: {len(converted_books)} / 66")
    print(f"Chapters: {total_chapters:,}")
    print(f"Verses: {total_verses:,}")
    print()
    
    if len(converted_books) == 66:
        print("✅ SUCCESS: Complete Bible downloaded!")
        print()
        print("What's next?")
        print("1. Test the display: python3 bible_display.py")
        print("2. Make sure config.json has: \"translation\": \"KJV\"")
        print()
    else:
        print("⚠️  WARNING: Download may be incomplete")
        print("   Try running the script again")
        print()
        sys.exit(1)
    
except urllib.error.URLError as e:
    print(f"✗ Network Error: {e}")
    print()
    print("Troubleshooting:")
    print("1. Check your internet connection")
    print("2. The GetBible API may be temporarily down")
    print("3. Try again in a few minutes")
    print()
    sys.exit(1)
    
except urllib.error.HTTPError as e:
    print(f"✗ HTTP Error {e.code}: {e.reason}")
    print()
    print("The GetBible API returned an error.")
    print("Try again in a few minutes.")
    print()
    sys.exit(1)
    
except json.JSONDecodeError as e:
    print(f"✗ JSON Error: {e}")
    print()
    print("The downloaded data was not valid JSON.")
    print("Try running the script again.")
    print()
    sys.exit(1)
    
except Exception as e:
    print(f"✗ Unexpected Error: {e}")
    print()
    print("An unexpected error occurred.")
    print("Please try running the script again.")
    print()
    sys.exit(1)
