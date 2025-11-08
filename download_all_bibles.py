#!/usr/bin/env python3
"""
Download ALL Bible Translations
Downloads KJV, WEB, ASV, and Darby in one go!
"""

import json
import urllib.request
import os
import sys
import time

print("=" * 70)
print("MASTER BIBLE DOWNLOADER")
print("=" * 70)
print()
print("This script will download ALL FOUR translations:")
print("  1. KJV (King James Version)")
print("  2. WEB (World English Bible)")
print("  3. ASV (American Standard Version)")
print("  4. YLT (Young's Literal Translation)")
print()
print("Total download size: ~18-20 MB")
print("Estimated time: 2-5 minutes")
print()

response = input("Continue? (y/n): ")
if response.lower() != 'y':
    print("Download cancelled.")
    sys.exit(0)

print()

# Create bible_data directory
os.makedirs('bible_data', exist_ok=True)

# Translations to download
translations = [
    {
        'name': 'King James Version',
        'abbrev': 'KJV',
        'code': 'kjv',
        'url': 'https://api.getbible.net/v2/kjv.json',
        'year': '1611/1769',
        'style': 'Traditional English'
    },
    {
        'name': 'World English Bible',
        'abbrev': 'WEB',
        'code': 'web',
        'url': 'https://api.getbible.net/v2/web.json',
        'year': '2020',
        'style': 'Modern English'
    },
    {
        'name': 'American Standard Version',
        'abbrev': 'ASV',
        'code': 'asv',
        'url': 'https://api.getbible.net/v2/asv.json',
        'year': '1901',
        'style': 'Scholarly, formal'
    },
    {
        'name': 'Young\'s Literal Translation',
        'abbrev': 'YLT',
        'code': 'ylt',
        'url': 'https://api.getbible.net/v2/ylt.json',
        'year': '1898',
        'style': 'Extremely literal'
    }
]

results = []

for i, trans in enumerate(translations, 1):
    print("=" * 70)
    print(f"Downloading {i}/4: {trans['name']} ({trans['abbrev']})")
    print("=" * 70)
    print()
    
    try:
        print(f"Fetching {trans['code']}.json from GetBible API...")
        
        req = urllib.request.Request(trans['url'], headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=120) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        print("✓ Downloaded!")
        print("  Converting to display format...")
        
        converted_books = []
        total_verses = 0
        
        for book in data.get('books', []):
            book_name = book.get('name', 'Unknown')
            
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
            
            converted_books.append({
                'name': book_name,
                'chapters': converted_chapters
            })
        
        bible_data = {
            "translation": trans['abbrev'],
            "books": converted_books
        }
        
        output_file = f"bible_data/{trans['code']}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(bible_data, f, indent=2, ensure_ascii=False)
        
        file_size = os.path.getsize(output_file) / (1024 * 1024)
        
        result = {
            'name': trans['name'],
            'abbrev': trans['abbrev'],
            'file': output_file,
            'books': len(converted_books),
            'verses': total_verses,
            'size': file_size,
            'success': len(converted_books) == 66
        }
        results.append(result)
        
        if result['success']:
            print(f"✓ SUCCESS: {result['books']} books, {result['verses']:,} verses")
            print(f"  File: {output_file} ({file_size:.1f} MB)")
        else:
            print(f"⚠️  WARNING: Only {result['books']} books (expected 66)")
        
        print()
        
        # Small delay between downloads to be nice to the API
        if i < len(translations):
            print("Waiting 2 seconds before next download...")
            time.sleep(2)
            print()
        
    except Exception as e:
        print(f"✗ ERROR downloading {trans['name']}: {e}")
        results.append({
            'name': trans['name'],
            'abbrev': trans['abbrev'],
            'success': False,
            'error': str(e)
        })
        print()
        continue

# Summary
print()
print("=" * 70)
print("DOWNLOAD SUMMARY")
print("=" * 70)
print()

successful = [r for r in results if r.get('success', False)]
failed = [r for r in results if not r.get('success', False)]

if successful:
    print(f"✅ Successfully downloaded {len(successful)} translation(s):")
    print()
    for r in successful:
        print(f"  • {r['name']} ({r['abbrev']})")
        print(f"    File: {r['file']}")
        print(f"    Books: {r['books']}, Verses: {r['verses']:,}, Size: {r['size']:.1f} MB")
        print()

if failed:
    print(f"❌ Failed to download {len(failed)} translation(s):")
    print()
    for r in failed:
        print(f"  • {r['name']} ({r['abbrev']})")
        if 'error' in r:
            print(f"    Error: {r['error']}")
        print()

print("=" * 70)
print("What's Next?")
print("=" * 70)
print()
print("You now have multiple Bible translations!")
print()
print("To switch between them:")
print("1. Edit config.json")
print("2. Change the 'translation' field to one of:")

for r in successful:
    print(f"   - \"{r['abbrev']}\" for {r['name']}")

print()
print("3. Run: python3 bible_display.py")
print()
print("Example config.json:")
print('{')
print('  "translation": "WEB",  ← Change this to switch')
print('  "font_size_reference": 14,')
print('  "font_size_text": 12,')
print('  "display_rotation": 0')
print('}')
print()

if len(successful) == len(translations):
    print("🎉 All downloads complete! Happy Bible reading!")
else:
    print("⚠️  Some downloads failed. Try running individual scripts:")
    for r in failed:
        print(f"   python3 download_{r['abbrev'].lower()}.py")
    
print()
