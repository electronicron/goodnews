# Upgrade to Enhanced Version - Chapter Display Mode

## 🎉 What's New

Your Bible display now supports **chapter mode** in addition to verse mode!

### New Features
- ✅ **Display full chapters** (4 per day)
- ✅ **Sequential reading** - Read through the entire Bible
- ✅ **Random chapters** - Discover different parts of Scripture  
- ✅ **Progress tracking** - Never lose your place
- ✅ **Flexible modes** - Switch between verse and chapter anytime

---

## 🚀 Quick Upgrade

### Step 1: Backup Your Current Files

```bash
cd /home/goodnews/goodnews  # or your project directory

# Backup current files
cp bible_display.py bible_display_original.py
cp config.json config_original.json

echo "✅ Backup complete!"
```

### Step 2: Replace with Enhanced Version

```bash
# Replace main script
cp bible_display_enhanced.py bible_display.py

# Replace config (or edit your existing one)
cp config_enhanced.json config.json

echo "✅ Upgrade complete!"
```

### Step 3: Test It

```bash
# Test verse mode (original behavior)
python3 bible_display.py

# Check the log
tail bible_display.log
```

---

## ⚙️ Configuration Changes

### OLD config.json (Original)
```json
{
  "translation": "KJV",
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```

### NEW config.json (Enhanced)
```json
{
  "translation": "KJV",
  "display_mode": "verse",       ← NEW!
  "chapter_mode": "sequential",  ← NEW!
  "chapters_per_day": 4,         ← NEW!
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```

### New Options Explained

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `display_mode` | `verse` or `chapter` | `verse` | Main display mode |
| `chapter_mode` | `sequential` or `random` | `sequential` | Chapter selection |
| `chapters_per_day` | `4` | `4` | Chapters per day (fixed) |

---

## 🔄 How to Use Each Mode

### Mode 1: Keep Original Behavior (Verse Mode)

**No changes needed!** The default is verse mode.

```json
{
  "display_mode": "verse"
}
```

This works exactly like before - random verse every hour.

---

### Mode 2: Sequential Chapter Reading

**Read through the Bible in order:**

```bash
nano config.json
```

Set:
```json
{
  "display_mode": "chapter",
  "chapter_mode": "sequential"
}
```

**How it works:**
- 4 chapters per day
- Day 1: Genesis 1, 2, 3, 4
- Day 2: Genesis 5, 6, 7, 8
- Continues through entire Bible
- Completes Bible in ~10 months

---

### Mode 3: Random Chapter Mode

**Explore different chapters:**

```bash
nano config.json
```

Set:
```json
{
  "display_mode": "chapter",
  "chapter_mode": "random"
}
```

**How it works:**
- Random chapter every 6 hours
- 4 different chapters per day
- Great for variety

---

## 📅 Chapter Schedule

When in chapter mode, the day divides into 4 periods:

| Period | Time | When It Changes |
|--------|------|----------------|
| 1 | 00:00 - 05:59 | Midnight |
| 2 | 06:00 - 11:59 | 6 AM |
| 3 | 12:00 - 17:59 | Noon |
| 4 | 18:00 - 23:59 | 6 PM |

The display shows: "Ch 1/4", "Ch 2/4", etc.

---

## 🔧 Update Your Cron Job

### If Using Hourly Updates (Works for Both Modes)

**No changes needed!** Your existing cron job works perfectly:

```bash
crontab -l
# Should show: 0 * * * * /usr/bin/python3 /home/goodnews/goodnews/bible_display.py
```

The script is smart - it shows the same chapter for the full 6-hour period.

### Optional: Update Only Every 6 Hours (Chapter Mode Only)

If you're ONLY using chapter mode, you can reduce updates:

```bash
crontab -e

# Change from:
0 * * * * /usr/bin/python3 /home/goodnews/goodnews/bible_display.py

# To:
0 */6 * * * /usr/bin/python3 /home/goodnews/goodnews/bible_display.py
```

Updates at: 00:00, 06:00, 12:00, 18:00

---

## 🗂️ New Files Created

### chapter_state.json (Auto-created)

When using sequential mode, this file tracks your progress:

```json
{
  "book_index": 0,
  "chapter_index": 4,
  "last_date": "2025-11-08"
}
```

**Location:** Same directory as bible_display.py

**You can:**
- Delete it to start over
- Edit it to jump to a specific book
- Leave it alone (recommended)

---

## ✅ Upgrade Checklist

- [ ] Backup original files
- [ ] Copy `bible_display_enhanced.py` to `bible_display.py`
- [ ] Update `config.json` with new options
- [ ] Test with: `python3 bible_display.py`
- [ ] Check log: `tail bible_display.log`
- [ ] Verify display updates
- [ ] Choose your preferred mode
- [ ] Enjoy!

---

## 🎯 Which Mode Should I Use?

### Use Verse Mode If You Want:
- ✅ Random inspiration every hour
- ✅ Original behavior
- ✅ Variety throughout the day

### Use Sequential Chapter Mode If You Want:
- ✅ Read through entire Bible
- ✅ Systematic Bible study
- ✅ Track your progress
- ✅ Complete Bible in 10 months

### Use Random Chapter Mode If You Want:
- ✅ Explore different books
- ✅ Chapter-length readings
- ✅ Surprise and variety

**You can switch anytime!** Just edit `config.json`.

---

## 🧪 Testing Guide

### Test 1: Verify Verse Mode Still Works

```bash
# Edit config
nano config.json
# Set: "display_mode": "verse"

# Run
python3 bible_display.py

# You should see a random verse
tail bible_display.log
```

Expected log:
```
Selected verse: Romans 8:28
Display updated successfully!
```

---

### Test 2: Try Sequential Chapter Mode

```bash
# Edit config
nano config.json
# Set: "display_mode": "chapter"
# Set: "chapter_mode": "sequential"

# Run multiple times
python3 bible_display.py  # Should show Genesis 1
python3 bible_display.py  # Should show Genesis 2
python3 bible_display.py  # Should show Genesis 3

# Check state file
cat chapter_state.json
```

Expected state:
```json
{
  "book_index": 0,
  "chapter_index": 3,
  "last_date": "2025-11-08"
}
```

---

### Test 3: Try Random Chapter Mode

```bash
# Edit config
nano config.json
# Set: "display_mode": "chapter"
# Set: "chapter_mode": "random"

# Run
python3 bible_display.py

tail bible_display.log
```

Expected log:
```
Selected chapter (random): Psalms 23
Display updated successfully!
```

---

## 🔄 Reverting to Original

If you want to go back to the original version:

```bash
# Restore original files
cp bible_display_original.py bible_display.py
cp config_original.json config.json

# Remove state file (optional)
rm chapter_state.json

# Test
python3 bible_display.py
```

---

## 📊 Feature Comparison

| Feature | Original | Enhanced |
|---------|----------|----------|
| **Random verses** | ✅ Yes | ✅ Yes |
| **Hourly updates** | ✅ Yes | ✅ Yes |
| **Chapter display** | ❌ No | ✅ Yes |
| **Sequential reading** | ❌ No | ✅ Yes |
| **Progress tracking** | ❌ No | ✅ Yes |
| **Random chapters** | ❌ No | ✅ Yes |
| **All translations** | ✅ Yes | ✅ Yes |
| **Backward compatible** | - | ✅ Yes |

---

## 💡 Pro Tips

### Tip 1: Best of Both Worlds

Switch between modes based on your needs:
- **Weekdays:** Chapter mode (systematic reading)
- **Weekends:** Verse mode (variety)

Just edit config.json when you want to switch!

### Tip 2: Start from Any Book

Want to start from Psalms or New Testament?

```bash
# Edit state file
nano chapter_state.json

# Book indices:
# 0=Genesis, 18=Job, 19=Psalms, 22=Proverbs, 39=Matthew, 42=Luke, etc.

{
  "book_index": 19,  # Start at Psalms
  "chapter_index": 0,
  "last_date": ""
}
```

### Tip 3: Adjust Chapter Frequency

Want chapters more often? Less often?

Edit `bible_display_enhanced.py`:
```python
# Find: def get_chapter_period()
return hour // 6  # 4 per day (current)
return hour // 4  # 6 per day
return hour // 8  # 3 per day
```

---

## 🐛 Troubleshooting

### Issue: "No such file" error

**Solution:**
```bash
# Make sure you're in the right directory
cd /home/goodnews/goodnews

# Verify files exist
ls -la bible_display_enhanced.py
ls -la config_enhanced.json
```

### Issue: Display not updating

**Check:**
1. Script runs without errors: `python3 bible_display.py`
2. Log shows success: `tail bible_display.log`
3. Cron is running: `crontab -l`

### Issue: Chapter not changing

**Remember:**
- Chapters change every 6 hours (not every hour)
- Same chapter shows for full 6-hour period
- This is intentional!

### Issue: State file errors (sequential mode)

**Reset:**
```bash
rm chapter_state.json
python3 bible_display.py
```

---

## 📞 Need Help?

**Check:**
1. [CHAPTER_MODE_GUIDE.md](CHAPTER_MODE_GUIDE.md) - Complete feature guide
2. `bible_display.log` - Error messages
3. `config.json` - Verify settings

**Common Issues:**
- Wrong directory? → `cd /home/goodnews/goodnews`
- Syntax error in config.json? → Check commas and quotes
- Permissions? → `chmod +x bible_display.py`

---

## 🎉 You're All Set!

You now have an enhanced Bible display with:
- ✅ Original verse mode (backward compatible)
- ✅ Sequential chapter reading
- ✅ Random chapter exploration
- ✅ Progress tracking
- ✅ Flexible switching

**Choose your mode and start reading!** 🙏📖

---

## 📖 Documentation

- **CHAPTER_MODE_GUIDE.md** - Complete feature documentation
- **Original README.md** - General project info
- **INSTALLATION.md** - Setup guide
- **HOURLY_SETUP.md** - Automation guide

---

**Enjoy your enhanced Bible display!**
