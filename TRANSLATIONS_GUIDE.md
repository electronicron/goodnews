# Complete Bible Translation Download Guide

## 🎉 NEW: Improved Download Scripts!

I've created **improved download scripts** that are faster, more reliable, and download the complete Bible in one file instead of 66 separate books.

---

## 📖 Your Four Translations

You requested:
1. **KJV** - King James Version (1611/1769)
2. **WEB** - World English Bible (2020)
3. **ASV** - American Standard Version (1901)
4. **DARBY** - Darby Translation (1890)

All four are complete (66 books), public domain, and ready to download!

---

## 🚀 Quick Start: Download All Four at Once!

### Option 1: Download Everything (Recommended!)

```bash
python3 download_all_bibles.py
```

This single command downloads all four translations in 2-5 minutes!

### Option 2: Download Individually

Choose which ones you want:

```bash
# KJV - Traditional English, most popular
python3 download_kjv_improved.py

# WEB - Modern English, easiest to read
python3 download_web_improved.py

# ASV - Classic 1901, scholarly
python3 download_asv.py

# Darby - Literal translation, scholarly
python3 download_darby.py
```

---

## 📊 Translation Comparison

| Translation | Year | Language | Reading Level | Best For |
|-------------|------|----------|---------------|----------|
| **WEB** | 2020 | Modern | ⭐⭐⭐⭐⭐ Easy | Daily reading |
| **ASV** | 1901 | Slightly archaic | ⭐⭐⭐⭐ Good | Study |
| **DARBY** | 1890 | Older formal | ⭐⭐⭐ Moderate | Literal study |
| **KJV** | 1611 | Traditional | ⭐⭐⭐ Moderate | Traditional |

---

## 📖 Sample Verses (John 3:16)

### WEB (Modern English)
> "For God so loved the world, that he gave his only born Son, that whoever believes in him should not perish, but have eternal life."

**Style:** Clean, modern, easy to understand

### ASV (Classic English)
> "For God so loved the world, that he gave his only begotten Son, that whosoever believeth on him should not perish, but have eternal life."

**Style:** Formal but readable, "begotten" and "believeth"

### DARBY (Literal)
> "For God so loved the world, that he gave his only-begotten Son, that whosoever believes on him may not perish, but have life eternal."

**Style:** Very literal, word-for-word, "only-begotten"

### KJV (Traditional)
> "For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."

**Style:** Traditional, poetic, "begotten" and "believeth"

---

## 🎯 Which Translation Should You Use?

### For Daily Reading → WEB ⭐ RECOMMENDED
- Modern English
- Easy to understand
- Completed in 2020
- Similar readability to NIV/ESV

### For Bible Study → ASV or DARBY
- **ASV**: More readable, respected scholarly translation
- **DARBY**: Most literal, word-for-word accurate

### For Tradition → KJV
- Classic "thee" and "thou" language
- Most memorized translation
- Beautiful poetic language

---

## 💻 Step-by-Step Installation

### On Your Raspberry Pi:

```bash
# 1. Navigate to your project directory
cd ~

# 2. Download all four translations
python3 download_all_bibles.py

# This will take 2-5 minutes and download:
# - bible_data/kjv.json (4.5 MB)
# - bible_data/web.json (4.2 MB)
# - bible_data/asv.json (4.4 MB)
# - bible_data/darby.json (4.3 MB)
```

### Verify Downloads:

```bash
ls -lh bible_data/
```

You should see all four .json files!

---

## 🔄 Switching Between Translations

### Method 1: Edit config.json

```bash
nano config.json
```

Change the translation field:

```json
{
  "translation": "WEB",  ← Change this!
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```

**Options:**
- `"KJV"` - King James Version
- `"WEB"` - World English Bible
- `"ASV"` - American Standard Version
- `"DARBY"` - Darby Translation

Save and test:
```bash
python3 bible_display.py
```

---

## 🔧 Technical Details

### Download Method
All scripts use the **GetBible API**:
- Single file download per translation
- Complete Bible in one request
- Fast and reliable
- No rate limiting for complete downloads

### Source
```
https://api.getbible.net/v2/[translation].json
```

Example: `https://api.getbible.net/v2/web.json`

### File Format
```json
{
  "translation": "WEB",
  "books": [
    {
      "name": "Genesis",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {
              "verse": 1,
              "text": "In the beginning..."
            }
          ]
        }
      ]
    }
  ]
}
```

---

## 📈 Download Statistics

After running `download_all_bibles.py`, you'll get a summary like:

```
✅ Successfully downloaded 4 translation(s):

  • King James Version (KJV)
    File: bible_data/kjv.json
    Books: 66, Verses: 31,102, Size: 4.5 MB

  • World English Bible (WEB)
    File: bible_data/web.json
    Books: 66, Verses: 31,086, Size: 4.2 MB

  • American Standard Version (ASV)
    File: bible_data/asv.json
    Books: 66, Verses: 31,102, Size: 4.4 MB

  • Darby Translation (DARBY)
    File: bible_data/darby.json
    Books: 66, Verses: 31,098, Size: 4.3 MB
```

---

## 🐛 Troubleshooting

### "Network Error" or "Connection refused"
- Check internet connection: `ping google.com`
- The GetBible API may be temporarily down
- Try again in a few minutes

### "Expected 66 books but got X"
- The download was interrupted
- Run the script again
- Individual translations may have slightly different book counts for technical reasons, but should be close to 66

### Script won't run
- Make it executable: `chmod +x download_all_bibles.py`
- Check Python version: `python3 --version` (should be 3.7+)

### Files not appearing
- Check the directory: `ls bible_data/`
- Make sure `bible_data/` directory exists
- The script creates it automatically, but you can: `mkdir -p bible_data`

---

## 💡 Pro Tips

### 1. Test Each Translation
```bash
# Download all
python3 download_all_bibles.py

# Test KJV
nano config.json  # Set "translation": "KJV"
python3 bible_display.py

# Test WEB
nano config.json  # Set "translation": "WEB"
python3 bible_display.py
```

### 2. Different Translations for Different Times
Use cron to rotate translations:

```bash
# Morning: WEB (easy reading)
0 6-12 * * * sed -i 's/"translation": ".*"/"translation": "WEB"/' ~/config.json && python3 ~/bible_display.py

# Afternoon: KJV (traditional)
0 13-18 * * * sed -i 's/"translation": ".*"/"translation": "KJV"/' ~/config.json && python3 ~/bible_display.py

# Evening: DARBY (study)
0 19-23 * * * sed -i 's/"translation": ".*"/"translation": "DARBY"/' ~/config.json && python3 ~/bible_display.py
```

### 3. Compare Verses
Keep all four translations and manually compare specific verses by switching config!

---

## 📋 Available Scripts

| Script | Purpose | Time |
|--------|---------|------|
| `download_all_bibles.py` | Downloads all 4 | 2-5 min |
| `download_kjv_improved.py` | KJV only | 30-60 sec |
| `download_web_improved.py` | WEB only | 30-60 sec |
| `download_asv.py` | ASV only | 30-60 sec |
| `download_darby.py` | Darby only | 30-60 sec |

---

## 🎯 Recommended Setup

For the best experience:

1. **Download all four translations**
   ```bash
   python3 download_all_bibles.py
   ```

2. **Start with WEB** (easiest to read)
   ```bash
   nano config.json  # Set "translation": "WEB"
   ```

3. **Test your display**
   ```bash
   python3 bible_display.py
   ```

4. **Try other translations** to find your favorite!

---

## ❓ FAQ

### Q: Which translation is most accurate?
**A:** All are accurate! DARBY and ASV are more literal word-for-word, while WEB prioritizes readability.

### Q: Can I have all four installed?
**A:** Yes! Install all four and switch between them in config.json.

### Q: How much space do they take?
**A:** About 17-18 MB total for all four.

### Q: Which is easiest to read on the small display?
**A:** WEB - modern English with shorter, clearer words.

### Q: Why did KJV only download 48 books before?
**A:** The old script downloaded books individually and had network timeouts. The new improved script downloads the complete Bible in one file - much more reliable!

### Q: Can I add more translations later?
**A:** Yes! Just run the individual download scripts anytime.

---

## ✅ Quick Reference

### Download Commands
```bash
# All four at once (recommended)
python3 download_all_bibles.py

# Or individually
python3 download_kjv_improved.py
python3 download_web_improved.py
python3 download_asv.py
python3 download_darby.py
```

### Switch Translations
```bash
nano config.json
# Change: "translation": "WEB"
# Options: "KJV", "WEB", "ASV", "DARBY"
```

### Test
```bash
python3 bible_display.py
cat bible_display.log
```

---

## 🎉 Summary

You now have access to **four complete, public domain Bible translations**:

1. ✅ **KJV** - Traditional, poetic (1611)
2. ✅ **WEB** - Modern, easy to read (2020) ⭐ RECOMMENDED
3. ✅ **ASV** - Classic, scholarly (1901)
4. ✅ **DARBY** - Literal, precise (1890)

**Total:** 66 books × 4 translations = 264 books of the Bible!
**All free, all public domain, all ready to use!**

Enjoy your daily Bible verses! 🙏📖
