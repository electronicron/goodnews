# ⚠️ IMPORTANT CORRECTION - Darby Translation

## The Problem

I accidentally recommended the **French Darby translation** instead of the English version. The code `darby` in the GetBible API points to the French translation, not English.

## The Solution: Young's Literal Translation (YLT)

After reviewing available translations, the **English Darby Translation** is not readily available in the GetBible API. 

However, **Young's Literal Translation (YLT)** is an excellent replacement that serves the same purpose:

### Why YLT is Perfect

**Young's Literal Translation** was created by Robert Young (author of Young's Analytical Concordance) with the same goals as Darby's translation:
- ✅ Extremely literal, word-for-word translation
- ✅ Maintains original word order where possible
- ✅ Scholarly and precise
- ✅ Public domain (1898)
- ✅ Complete 66 books
- ✅ Available in English

### Comparison

| Feature | Darby (English) | YLT |
|---------|----------------|-----|
| Literal approach | ✅ Yes | ✅ Yes |
| Word-for-word | ✅ Yes | ✅ Yes |
| Public domain | ✅ Yes | ✅ Yes |
| Available via API | ❌ No | ✅ Yes |
| Year | 1890 | 1898 |

## 📖 Sample Comparison (John 3:16)

### Young's Literal Translation (YLT)
> "for God did so love the world, that His Son -- the only begotten -- He gave, that every one who is believing in him may not perish, but may have life age-during."

**Note:** YLT maintains the Greek word order and uses "age-during" for "eternal"

### What Darby Would Say (if we had it)
> "For God so loved the world, that he gave his only-begotten Son, that whosoever believes on him may not perish, but have life eternal."

**Similar but slightly different word choices**

## 📥 Your Updated Download Scripts

### OLD (INCORRECT):
- ❌ `download_darby.py` - French Darby (REMOVED)

### NEW (CORRECT):
- ✅ `download_ylt.py` - English Young's Literal Translation

## 🎯 Updated Recommendation

**Your Four Translations:**

1. **KJV** - Traditional English (1611)
2. **WEB** - Modern English (2020)
3. **ASV** - Scholarly classic (1901)
4. **YLT** - Most literal (1898) ← **Replaces Darby**

## 🚀 How to Download

### Download YLT Alone:
```bash
python3 download_ylt.py
```

### Download All Four (Updated):
```bash
python3 download_all_bibles.py
```

This now downloads: **KJV + WEB + ASV + YLT**

## ⚙️ Configuration

To use YLT, edit `config.json`:

```json
{
  "translation": "YLT",
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```

## 💡 Why This Is Actually Better

YLT is arguably **more literal** than Darby and has these advantages:
- More extreme in maintaining original word order
- Unique word choices that reflect Greek/Hebrew more closely
- Well-documented and widely studied
- Easier to access (available in GetBible API)

## 📚 Alternative Options

If you specifically want a different literal translation:

### Bible in Basic English (BBE)
- Code: `bbe`
- URL: `https://api.getbible.net/v2/bbe.json`
- Simple, clear English (1,000 word vocabulary)

### Webster's Bible (WB)
- Code: `wb`  
- URL: `https://api.getbible.net/v2/wb.json`
- Based on KJV with American spellings

Let me know if you'd like scripts for these instead!

## ✅ Summary

**OLD Plan:** KJV + WEB + ASV + Darby (French ❌)
**NEW Plan:** KJV + WEB + ASV + YLT (English ✅)

**What Changed:**
- Removed: `download_darby.py` (was French)
- Added: `download_ylt.py` (English, even more literal)
- Updated: `download_all_bibles.py` (now downloads YLT)

**Your files are ready to download!** 🙏📖
