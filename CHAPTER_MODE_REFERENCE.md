# Chapter Mode Quick Reference

## 🎯 Three Display Modes

### 1. Verse Mode (Original)
```json
{"display_mode": "verse"}
```
- Random verse every hour
- 24 different verses per day

### 2. Sequential Chapters
```json
{
  "display_mode": "chapter",
  "chapter_mode": "sequential"
}
```
- 4 chapters per day in order
- Read through entire Bible
- Tracks progress

### 3. Random Chapters
```json
{
  "display_mode": "chapter",
  "chapter_mode": "random"
}
```
- 4 random chapters per day
- Changes every 6 hours

---

## 📅 Chapter Schedule

| Period | Time | Example |
|--------|------|---------|
| Ch 1/4 | 00:00-05:59 | Genesis 1 |
| Ch 2/4 | 06:00-11:59 | Genesis 2 |
| Ch 3/4 | 12:00-17:59 | Genesis 3 |
| Ch 4/4 | 18:00-23:59 | Genesis 4 |

---

## ⚙️ Config.json Template

```json
{
  "translation": "KJV",
  "display_mode": "chapter",
  "chapter_mode": "sequential",
  "chapters_per_day": 4,
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```

---

## 🔄 Switch Modes

```bash
# Edit config
nano config.json

# Change display_mode:
# - "verse" = hourly verses
# - "chapter" = 4 chapters/day

# If chapter mode, change chapter_mode:
# - "sequential" = in order
# - "random" = random

# Save and test
python3 bible_display.py
```

---

## 📁 Files

| File | Purpose |
|------|---------|
| `bible_display.py` | Main script (use enhanced version) |
| `config.json` | Settings |
| `chapter_state.json` | Progress tracker (auto-created) |
| `bible_display.log` | Event log |

---

## 🛠️ Common Commands

```bash
# Test display
python3 bible_display.py

# Check log
tail bible_display.log

# View progress (sequential mode)
cat chapter_state.json

# Reset progress
rm chapter_state.json

# Edit settings
nano config.json
```

---

## ⏰ Cron Jobs

### Hourly (works for all modes)
```
0 * * * * /usr/bin/python3 /path/to/bible_display.py
```

### Every 6 hours (chapter mode only)
```
0 */6 * * * /usr/bin/python3 /path/to/bible_display.py
```

---

## 🧪 Quick Test

```bash
# Test verse mode
echo '{"translation":"KJV","display_mode":"verse"}' > config.json
python3 bible_display.py

# Test sequential chapters
echo '{"translation":"KJV","display_mode":"chapter","chapter_mode":"sequential"}' > config.json
python3 bible_display.py
python3 bible_display.py  # Should advance to next chapter
cat chapter_state.json     # Check progress

# Test random chapters
echo '{"translation":"KJV","display_mode":"chapter","chapter_mode":"random"}' > config.json
python3 bible_display.py
```

---

## 🎓 Reading Progress

### Sequential Mode Timeline

- **4 chapters/day** × **7 days** = 28 chapters/week
- **Bible has 1,189 chapters**
- **1,189 ÷ 4** = ~297 days
- **Complete Bible in ~10 months!**

### Book Order

1-39: Old Testament (Genesis → Malachi)
40-66: New Testament (Matthew → Revelation)

---

## 💡 Pro Tips

**Want to start from Psalms?**
```bash
echo '{"book_index":19,"chapter_index":0,"last_date":""}' > chapter_state.json
```

**Want to start from New Testament?**
```bash
echo '{"book_index":39,"chapter_index":0,"last_date":""}' > chapter_state.json
```

**Switch between modes anytime** - just edit config.json!

---

## ⚠️ Remember

- Chapters change every **6 hours**
- Verses change every **1 hour**
- Same content shows for the full period
- Sequential mode saves progress automatically
- Random mode gives new random each period

---

## 📖 Full Documentation

- **CHAPTER_MODE_GUIDE.md** - Complete guide
- **UPGRADE_GUIDE.md** - Upgrade instructions
- **INSTALLATION.md** - Setup guide

---

**Quick help:** `tail bible_display.log`
