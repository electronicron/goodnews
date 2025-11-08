# Chapter Display Mode - Complete Guide

## 📖 Overview

The enhanced version of Bible Display now supports **two display modes**:

1. **Verse Mode** (original) - Random verse every hour
2. **Chapter Mode** (NEW!) - 4 chapters per day, sequential or random

---

## 🆕 What's New

### Chapter Display Features

- ✅ **4 chapters per day** - Divided into 6-hour periods
- ✅ **Sequential mode** - Read through Bible in order
- ✅ **Random mode** - Random chapter each period
- ✅ **Progress tracking** - Sequential mode remembers where you left off
- ✅ **Smart display** - Shows first verses + verse count for long chapters

---

## ⚙️ Configuration

Edit `config.json`:

```json
{
  "translation": "KJV",
  "display_mode": "verse",       ← "verse" or "chapter"
  "chapter_mode": "sequential",  ← "sequential" or "random"
  "chapters_per_day": 4,         ← Always 4 (future expansion)
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```

### Configuration Options

| Option | Values | Description |
|--------|--------|-------------|
| `display_mode` | `verse` or `chapter` | Main display mode |
| `chapter_mode` | `sequential` or `random` | How chapters are selected |
| `chapters_per_day` | `4` | Number of chapters per day |
| `translation` | `KJV`, `WEB`, `ASV`, `YLT` | Bible translation |

---

## 📅 Chapter Schedule (4 per day)

The day is divided into **4 periods of 6 hours each**:

| Period | Time | Example Chapter |
|--------|------|----------------|
| **1** | 00:00 - 05:59 | Genesis 1 |
| **2** | 06:00 - 11:59 | Genesis 2 |
| **3** | 12:00 - 17:59 | Genesis 3 |
| **4** | 18:00 - 23:59 | Genesis 4 |

The display shows which period you're in: "Ch 1/4", "Ch 2/4", etc.

---

## 🔄 Display Modes Explained

### Mode 1: Verse Mode (Original)

**Configuration:**
```json
{
  "display_mode": "verse"
}
```

**How it works:**
- New random verse every hour
- Same verse for full hour
- Changes at top of each hour (1:00, 2:00, etc.)

**Example:**
```
Romans 8:28

For we know that all things work 
together for good to them that 
love God, to them who are the 
called according to his purpose.

                    11/08/2025
```

---

### Mode 2: Chapter Mode - Sequential

**Configuration:**
```json
{
  "display_mode": "chapter",
  "chapter_mode": "sequential"
}
```

**How it works:**
- Reads through Bible in order
- 4 chapters per day (every 6 hours)
- Remembers progress in `chapter_state.json`
- Continues from where you left off
- Automatically wraps to Genesis after Revelation

**Example Day:**
- **00:00-05:59:** Genesis 1
- **06:00-11:59:** Genesis 2
- **12:00-17:59:** Genesis 3
- **18:00-23:59:** Genesis 4

**Next Day:**
- **00:00-05:59:** Genesis 5
- And so on...

**Display example:**
```
Genesis 1

1. In the beginning God created 
the heaven and the earth. 2. And 
the earth was without form, and 
void... (31 verses total)

              11/08/2025 • Ch 1/4
```

---

### Mode 3: Chapter Mode - Random

**Configuration:**
```json
{
  "display_mode": "chapter",
  "chapter_mode": "random"
}
```

**How it works:**
- Random chapter each 6-hour period
- Same chapter for entire 6-hour period
- Different chapter in next period
- Uses date+period as seed for consistency

**Example Day:**
- **00:00-05:59:** Psalms 23
- **06:00-11:59:** John 3
- **12:00-17:59:** Proverbs 16
- **18:00-23:59:** Matthew 5

**Display example:**
```
Psalms 23

1. The LORD is my shepherd; I 
shall not want. 2. He maketh me 
to lie down in green pastures...
(6 verses total)

              11/08/2025 • Ch 2/4
```

---

## 📊 Chapter Display Logic

### Short Chapters (≤5 verses)
Shows ALL verses in the chapter.

**Example: Philemon 1**
```
Philemon 1

1. Paul, a prisoner of Jesus...
2. To Philemon our dearly...
3. Grace to you, and peace...
4. I thank my God, making...
5. Hearing of thy love and faith...

(5 verses total)
```

### Long Chapters (>5 verses)
Shows **first 3 verses** + verse count.

**Example: Genesis 1**
```
Genesis 1

1. In the beginning God created 
the heaven and the earth. 2. And 
the earth was without form...
3. And God said, Let there be...

... (31 verses total)
```

This prevents text overflow on the small e-paper display.

---

## 🔄 Sequential Mode Progress Tracking

### How It Works

Sequential mode tracks your reading progress in `chapter_state.json`:

```json
{
  "book_index": 0,
  "chapter_index": 4,
  "last_date": "2025-11-08"
}
```

- `book_index`: Which book (0 = Genesis, 1 = Exodus, etc.)
- `chapter_index`: Which chapter in that book
- `last_date`: Last update date

### Reading Through the Entire Bible

**At 4 chapters per day:**
- 1,189 chapters in the Bible
- 1,189 ÷ 4 = ~297 days
- **Complete Bible in about 10 months!**

### Starting Over

To restart from Genesis 1:

```bash
# Delete the state file
rm chapter_state.json

# Or reset it manually
echo '{"book_index": 0, "chapter_index": 0, "last_date": ""}' > chapter_state.json
```

Next update will start from Genesis 1.

---

## 🎯 Use Cases

### Use Case 1: Daily Verse Inspiration
```json
{
  "display_mode": "verse"
}
```
**Best for:** Random encouragement throughout the day

---

### Use Case 2: Reading Through the Bible
```json
{
  "display_mode": "chapter",
  "chapter_mode": "sequential"
}
```
**Best for:** Systematic Bible reading, completing the Bible

---

### Use Case 3: Chapter Exploration
```json
{
  "display_mode": "chapter",
  "chapter_mode": "random"
}
```
**Best for:** Discovering different parts of Scripture

---

## 🔄 Switching Between Modes

### Switch to Verse Mode
```bash
nano config.json
# Set: "display_mode": "verse"
# Save and exit

# Test
python3 bible_display.py
```

### Switch to Sequential Chapters
```bash
nano config.json
# Set: "display_mode": "chapter"
# Set: "chapter_mode": "sequential"
# Save and exit

# Test
python3 bible_display.py
```

### Switch to Random Chapters
```bash
nano config.json
# Set: "display_mode": "chapter"
# Set: "chapter_mode": "random"
# Save and exit

# Test
python3 bible_display.py
```

---

## ⏰ Update Schedule

### For Hourly Updates (Verse Mode)
```bash
crontab -e
# Add: 0 * * * * /usr/bin/python3 /home/pi/bible_display.py
```

### For Chapter Mode (Updates every 6 hours)
```bash
crontab -e
# Add: 0 */6 * * * /usr/bin/python3 /home/pi/bible_display.py
```

This updates at: 00:00, 06:00, 12:00, 18:00

### Or Keep Hourly (Works for Both Modes)
```bash
crontab -e
# Add: 0 * * * * /usr/bin/python3 /home/pi/bible_display.py
```

The script is smart enough to show the same chapter for the full 6-hour period!

---

## 📁 File Changes

### New/Modified Files

1. **`bible_display.py`** - Enhanced with chapter support
2. **`config.json`** - New configuration options
3. **`chapter_state.json`** - NEW! Tracks sequential progress (auto-created)

### What Gets Created

When you use sequential mode, the script creates:
```
chapter_state.json
```

This file tracks where you are in your Bible reading.

---

## 🧪 Testing

### Test Verse Mode
```bash
# Edit config
nano config.json
# Set: "display_mode": "verse"

# Run
python3 bible_display.py

# Check log
tail bible_display.log
```

### Test Sequential Chapters
```bash
# Edit config
nano config.json
# Set: "display_mode": "chapter"
# Set: "chapter_mode": "sequential"

# Run multiple times to see progression
python3 bible_display.py  # Genesis 1
python3 bible_display.py  # Genesis 2
python3 bible_display.py  # Genesis 3
python3 bible_display.py  # Genesis 4

# Check state
cat chapter_state.json
```

### Test Random Chapters
```bash
# Edit config
nano config.json
# Set: "display_mode": "chapter"
# Set: "chapter_mode": "random"

# Run
python3 bible_display.py

# Check log
tail bible_display.log
```

---

## 📊 Comparison Table

| Feature | Verse Mode | Chapter (Sequential) | Chapter (Random) |
|---------|-----------|---------------------|------------------|
| **Update Frequency** | Every hour | Every 6 hours | Every 6 hours |
| **Content** | Single verse | Chapter excerpt | Chapter excerpt |
| **Selection** | Random | In order | Random |
| **Progress Tracking** | No | Yes | No |
| **Complete Bible** | Random sampling | Yes (~10 months) | Random sampling |
| **Best For** | Inspiration | Systematic reading | Exploration |

---

## 🎓 Advanced Tips

### Tip 1: Adjust Chapter Frequency

Want chapters more or less often? Modify the period calculation in the code:

```python
# In get_chapter_period()
return hour // 6  # 4 periods per day (current)
return hour // 4  # 6 periods per day
return hour // 8  # 3 periods per day
return hour // 12 # 2 periods per day
```

### Tip 2: Resume From Specific Book

Want to start from a specific book?

```bash
# Edit chapter_state.json
nano chapter_state.json

# Set book_index:
# 0 = Genesis, 18 = Job, 19 = Psalms, 39 = Matthew, etc.
{
  "book_index": 19,  # Start at Psalms
  "chapter_index": 0,
  "last_date": ""
}
```

### Tip 3: Show More Verses

Edit the script to show more verses:

```python
# In get_chapter_text(), find this line:
for v in verses[:3]:  # Change 3 to 5 for more verses
```

---

## 🐛 Troubleshooting

### Issue: Chapter not changing

**Check:**
1. What time period are you in? (0-5, 6-11, 12-17, 18-23)
2. Chapter only changes between periods
3. Run: `date` to verify time

**Solution:** Wait for next 6-hour period boundary.

### Issue: Sequential mode not advancing

**Check state file:**
```bash
cat chapter_state.json
```

**Reset if needed:**
```bash
rm chapter_state.json
python3 bible_display.py
```

### Issue: Text too long/cut off

**Adjust font size:**
```json
{
  "font_size_text": 10  // Smaller text
}
```

---

## 📖 Example Configurations

### Configuration 1: Daily Inspiration
```json
{
  "translation": "WEB",
  "display_mode": "verse",
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```
Cron: `0 * * * *` (every hour)

### Configuration 2: Read Through Bible
```json
{
  "translation": "KJV",
  "display_mode": "chapter",
  "chapter_mode": "sequential",
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```
Cron: `0 */6 * * *` (every 6 hours)

### Configuration 3: Chapter Exploration
```json
{
  "translation": "ASV",
  "display_mode": "chapter",
  "chapter_mode": "random",
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```
Cron: `0 */6 * * *` (every 6 hours)

---

## ✅ Quick Reference

### Commands
```bash
# Edit config
nano config.json

# Test display
python3 bible_display.py

# Check log
tail bible_display.log

# View chapter state
cat chapter_state.json

# Reset progress
rm chapter_state.json
```

### Config Values
```
display_mode: "verse" or "chapter"
chapter_mode: "sequential" or "random"
chapters_per_day: 4
```

---

Enjoy reading through the Bible on your e-paper display! 🙏📖
