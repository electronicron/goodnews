# Bible Translation Download Guide

## Overview

This guide explains how to download complete Bible translations for your e-paper display.

---

## ⚖️ Copyright & Legal Information

### ✅ FREE Public Domain Translations (No Restrictions)
- **KJV** (King James Version, 1611/1769) - Most popular
- **WEB** (World English Bible) - Modern English
- **ASV** (American Standard Version, 1901)
- **YLT** (Young's Literal Translation)
- **BBE** (Bible in Basic English)

### ❌ Copyrighted Translations (Cannot Download Freely)
- **NIV** (New International Version) - Biblica/HarperCollins
- **ESV** (English Standard Version) - Crossway
- **NASB** (New American Standard Bible) - Lockman Foundation
- **NLT** (New Living Translation) - Tyndale
- **NKJV** (New King James Version) - Thomas Nelson

**Important:** Even if you find copyrighted translations online, using them without permission violates copyright law. Stick to public domain translations!

---

## 🚀 Quick Start: Download KJV (Recommended)

### Method 1: Automatic Download (Easiest!)

I've created a script that downloads the complete KJV Bible automatically:

```bash
python3 download_kjv.py
```

This will:
- Download all 66 books (31,102 verses)
- Convert to the correct format
- Save as `bible_data/kjv.json`
- Take about 1-2 minutes

**That's it!** Then just run:
```bash
python3 bible_display.py
```

---

## 📖 Available Translation Sources

### Option 1: GitHub Repositories (Best for Beginners)

#### KJV - King James Version
**Source:** https://github.com/aruljohn/Bible-kjv
- **Download:** Use the `download_kjv.py` script (included)
- **Quality:** Excellent, well-maintained
- **Format:** Already in JSON, easy to convert

#### Multiple Translations
**Source:** https://github.com/thiagobodruk/bible
- **Includes:** KJV, WEB, and many other languages
- **Format:** JSON and XML
- **Download:**
  ```bash
  # Download the entire repository
  git clone https://github.com/thiagobodruk/bible.git
  
  # Or download specific translation:
  wget https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_kjv.json
  ```

#### Bible Translations Repository
**Source:** https://github.com/bibleapi/bibleapi-bibles-json
- Multiple translations in JSON
- Ready to use format
- Various languages

---

## 📥 Step-by-Step: Manual Download

### For KJV from GitHub

1. **Visit the repository:**
   ```
   https://github.com/aruljohn/Bible-kjv
   ```

2. **Download the ZIP:**
   - Click the green "Code" button
   - Select "Download ZIP"
   - Extract the files

3. **Use the conversion script (I'll provide below)**

### For Other Translations

1. **Visit one of these sources:**
   - https://github.com/thiagobodruk/bible
   - https://github.com/bibleapi/bibleapi-bibles-json
   - https://sourceforge.net/projects/biblesuper/files/All%20Bibles%20-%20JSON/

2. **Download the JSON file for your preferred translation**

3. **Convert to the correct format (see below)**

---

## 🔄 Converting Bible Formats

Different sources use different JSON structures. Your display expects this format:

```json
{
  "translation": "KJV",
  "books": [
    {
      "name": "Genesis",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {
              "verse": 1,
              "text": "In the beginning God created the heaven and the earth."
            }
          ]
        }
      ]
    }
  ]
}
```

### If Your Format is Different

I can create a converter script. Common formats include:

**Format A (thiagobodruk):**
```json
[
  {
    "abbrev": "gn",
    "name": "Genesis",
    "chapters": [
      ["Verse 1", "Verse 2", "Verse 3"]
    ]
  }
]
```

**Format B (farskipper):**
```json
{
  "Genesis 1:1": "In the beginning...",
  "Genesis 1:2": "And the earth..."
}
```

Would you like me to create converter scripts for these?

---

## 🌐 Using Bible APIs (Alternative)

If you want always-updated content, you can use an API instead of downloaded files.

### Bible-API.com (Free, Simple)
```python
import requests

# Get a verse
response = requests.get('https://bible-api.com/john+3:16?translation=kjv')
verse = response.json()
print(verse['text'])
```

**Pros:**
- Always up-to-date
- Many translations
- No large files to download

**Cons:**
- Requires internet connection
- Rate limited (15 requests per 30 seconds)
- May go offline

### API.Bible (Free, Comprehensive)
- Requires free API key
- 2,500+ translations
- Very reliable

---

## 📋 Comparison Table

| Translation | Year | Style | Availability | Difficulty |
|-------------|------|-------|--------------|------------|
| KJV | 1611 | Formal | ✅ Free | ⭐ Easy |
| WEB | Modern | Formal | ✅ Free | ⭐ Easy |
| ASV | 1901 | Formal | ✅ Free | ⭐⭐ Medium |
| NIV | 1984 | Dynamic | ❌ Licensed | ❌ Cannot use |
| ESV | 2001 | Formal | ❌ Licensed | ❌ Cannot use |

---

## 🎯 My Recommendation

**For your project, use KJV:**

1. It's completely free and public domain
2. Most widely known translation
3. Easy to download with my script
4. No legal concerns
5. Excellent quality

**Simply run:**
```bash
python3 download_kjv.py
```

**Then test:**
```bash
python3 bible_display.py
```

---

## 🔧 Advanced: Download Other Free Translations

### World English Bible (WEB)

The WEB is a modern English translation in public domain:

**Download from:**
- https://ebible.org/web/ (Official source)
- https://github.com/thiagobodruk/bible (JSON format)

**Using the thiagobodruk repository:**
```bash
# Download directly
wget https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_web.json

# Or clone entire repo
git clone https://github.com/thiagobodruk/bible.git
cd bible/json
# You'll find en_web.json here
```

### American Standard Version (ASV)

**Download from Bible SuperSearch:**
```bash
wget https://sourceforge.net/projects/biblesuper/files/All%20Bibles%20-%20JSON/asv.json
```

---

## 📱 Using With Your Display

After downloading any translation:

1. **Place the file in `bible_data/` directory**
   ```bash
   mv downloaded_bible.json bible_data/translation_name.json
   ```

2. **Update `config.json`:**
   ```json
   {
     "translation": "KJV",
     ...
   }
   ```

3. **Test the display:**
   ```bash
   python3 bible_display.py
   ```

---

## ❓ FAQ

### Can I use NIV on my personal display?
Technically, for **private, personal, non-commercial use**, you might have some flexibility, but the safest and legal approach is to use public domain translations. NIV cannot be legally redistributed or downloaded as a complete database.

### What's the best translation for readability?
- **Modern English:** WEB (World English Bible)
- **Classic/Traditional:** KJV (King James Version)
- **Literal:** YLT (Young's Literal Translation)

### How big are these files?
- KJV: ~4.5 MB
- WEB: ~4.2 MB
- ASV: ~4.4 MB

All easily fit on a Raspberry Pi.

### Can I have multiple translations?
Yes! Download multiple JSON files:
```
bible_data/
  ├── kjv.json
  ├── web.json
  └── asv.json
```

Switch by editing `config.json`.

---

## 🆘 Troubleshooting

### Download script fails
- Check internet connection
- Try a different mirror/source
- Download manually from GitHub

### Wrong format after download
- Let me know the source - I can create a converter
- Check the JSON structure matches expected format

### File too large
- All public domain Bibles should be <5MB
- If larger, you may have extra data (footnotes, etc.)

---

## 📞 Need Help?

If you encounter issues:
1. Try the automatic `download_kjv.py` script first
2. Check the format matches the expected structure
3. Look at the sample files I provided
4. Ask me for help with specific sources!

---

## ✅ Summary

**Easiest Path:**
1. Run: `python3 download_kjv.py`
2. Wait 1-2 minutes
3. Run: `python3 bible_display.py`
4. Done!

**Alternative Path:**
1. Visit: https://github.com/aruljohn/Bible-kjv
2. Download ZIP
3. Convert using provided script
4. Test display

**For NIV:** Unfortunately not available for free download. Use KJV or WEB instead - both are excellent translations!
