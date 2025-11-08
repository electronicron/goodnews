# How to Download Bible Translations - Simple Guide

## The Short Answer

**NIV cannot be downloaded for free** because it's copyrighted. 

**But don't worry!** You have excellent alternatives:

---

## ✅ Best Option: Download KJV (Just 3 Steps!)

### Step 1: Transfer files to your Raspberry Pi
Make sure you have these files on your Pi:
- `download_kjv.py` ← This is the magic script!
- All other project files

### Step 2: Run the download script
```bash
python3 download_kjv.py
```

This will:
- Download all 66 books of the Bible (31,102 verses!)
- Take about 1-2 minutes
- Create `bible_data/kjv.json` automatically
- Everything is automatic!

### Step 3: Test your display
```bash
python3 bible_display.py
```

**That's it!** Your display now has the complete King James Bible.

---

## 🎯 What You Get with KJV

- **Complete Bible:** All 66 books, 31,102 verses
- **Free Forever:** Public domain, no copyright issues
- **Most Popular:** The classic English translation
- **Beautiful Language:** Poetic and traditional
- **File Size:** About 4.5 MB

---

## 📖 Alternative: World English Bible (Modern English)

If you prefer modern English instead of the older KJV language:

```bash
python3 download_web.py
```

Then edit `config.json` and change:
```json
{
  "translation": "WEB",
  ...
}
```

**WEB Features:**
- Modern, easy-to-read English
- Public domain (free)
- Accurate translation
- Similar to NIV in readability

---

## 📊 Quick Comparison

| Translation | Style | Example Verse (John 3:16) |
|-------------|-------|---------------------------|
| **KJV** (1611) | Traditional | "For God so loved the world, that he gave his only begotten Son..." |
| **WEB** (Modern) | Modern | "For God so loved the world, that he gave his only born Son..." |
| **NIV** (Can't use) | Modern | Not available for download |

---

## ❓ Why Can't I Download NIV?

The NIV is owned by Biblica and HarperCollins Christian Publishing. It's copyrighted and cannot be freely distributed. 

While some repositories may have NIV text, using it without proper licensing would violate copyright.

**Legal free alternatives:**
- ✅ KJV - King James Version (1611)
- ✅ WEB - World English Bible (modern)
- ✅ ASV - American Standard Version (1901)
- ✅ YLT - Young's Literal Translation

---

## 🚀 Complete Process (From Start to Finish)

### On Your Computer:
```bash
# Copy files to Raspberry Pi
scp download_kjv.py pi@raspberrypi.local:~/
scp download_web.py pi@raspberrypi.local:~/
```

### On Your Raspberry Pi:
```bash
# Download KJV (recommended)
python3 download_kjv.py

# OR download WEB (modern English)
python3 download_web.py

# Test the display
python3 bible_display.py

# Check what was displayed
cat bible_display.log
```

---

## 💡 Pro Tips

### Want both translations?
Download both and switch between them:

```bash
# Download both
python3 download_kjv.py
python3 download_web.py
```

Now you'll have:
- `bible_data/kjv.json`
- `bible_data/web.json`

Switch by editing `config.json`:
```json
{
  "translation": "KJV",    ← Change this to "WEB" to switch
  ...
}
```

### Check what you have:
```bash
ls -lh bible_data/
```

You should see your JSON files!

---

## 🔍 Verify Your Download

After running the download script:

```bash
# Check file exists
ls -lh bible_data/kjv.json

# Check file size (should be ~4.5 MB)
du -h bible_data/kjv.json

# Peek at the contents
head -n 20 bible_data/kjv.json
```

---

## 🎨 Real Example

Here's what happens when you run the download:

```
$ python3 download_kjv.py

======================================================================
KJV Bible Downloader
======================================================================

This will download the complete King James Version Bible
and format it for your e-paper display.

Step 1: Downloading KJV Bible data from GitHub...
Source: https://github.com/aruljohn/Bible-kjv

Downloading 66 books...
This may take a minute or two...

  [ 1/66] Downloading Genesis... ✓
  [ 2/66] Downloading Exodus... ✓
  [ 3/66] Downloading Leviticus... ✓
  ...
  [66/66] Downloading Revelation... ✓

Successfully downloaded 66 books with 31,102 verses!

Step 2: Saving to bible_data/kjv.json...
✓ Complete!

======================================================================
Download Complete!
======================================================================

File: bible_data/kjv.json
Size: 4.5 MB
Books: 66
Verses: 31,102

What's next?
1. Test the display: python3 bible_display.py
2. Update config.json if needed (should already be set to KJV)
```

---

## 🆘 Troubleshooting

### "No module named 'urllib'"
This should not happen - urllib is built into Python. Try:
```bash
python3 --version  # Should be 3.7 or higher
```

### "Connection refused" or "Download failed"
- Check internet connection: `ping google.com`
- Try again in a few minutes
- GitHub might be temporarily down

### "Permission denied"
Make script executable:
```bash
chmod +x download_kjv.py
```

### Downloaded but display shows errors
Check the log:
```bash
cat bible_display.log
```

Make sure config.json has the right translation:
```bash
cat config.json
```

---

## 📚 Want More Translations?

See the complete guide: [BIBLE_DOWNLOADS.md](computer:///mnt/user-data/outputs/BIBLE_DOWNLOADS.md)

It includes:
- All available free translations
- Manual download instructions
- Format conversion tools
- API alternatives

---

## ✅ Summary

**For NIV specifically:** Unfortunately, you cannot download NIV freely due to copyright. 

**Best solution:** Use the KJV download script I provided!

```bash
python3 download_kjv.py    # Downloads complete KJV Bible
python3 bible_display.py   # Test your display
```

**That's all you need!** The KJV is an excellent translation and is completely free to use.

---

## 🎉 You're Almost Done!

After downloading:
1. ✅ You have a complete Bible (31,102 verses)
2. ✅ It's legal and free forever
3. ✅ It works with your display
4. ✅ You can switch translations anytime

Now just set up the automatic daily updates (see INSTALLATION.md) and enjoy your daily Bible verses! 🙏
