# Project Files Documentation

Complete list of all files in this repository with descriptions.

## 📂 Core Application Files

### `bible_display.py`
**Main display script**
- Displays Bible verses on e-paper screen
- Handles hourly verse selection using date+hour seed
- Manages e-paper display hardware
- Creates images with verse text, reference, and date
- Logs all operations to `bible_display.log`
- **Size:** ~8.6 KB
- **Lines:** ~294

### `config.json`
**Configuration file**
- Sets Bible translation (KJV, WEB, ASV, YLT)
- Controls font sizes for reference and text
- Sets display rotation (0, 90, 180, 270 degrees)
- Easy to edit without touching code
- **Format:** JSON

### `requirements.txt`
**Python dependencies**
- Pillow (image processing)
- spidev (SPI communication)
- RPi.GPIO (GPIO control)
- **Required before running:** `pip install -r requirements.txt`

### `setup.sh`
**Automated setup script**
- Updates system packages
- Installs Python dependencies
- Enables SPI interface
- Downloads Waveshare e-Paper library
- Creates necessary directories
- Makes scripts executable
- **Usage:** `chmod +x setup.sh && ./setup.sh`

---

## 📥 Bible Download Scripts

### `download_all_bibles.py`
**Master download script**
- Downloads all 4 translations in one go
- Shows progress for each translation
- Provides summary of downloads
- Takes 2-5 minutes total
- **Usage:** `python3 download_all_bibles.py`
- **Downloads:** KJV, WEB, ASV, YLT

### `download_kjv_improved.py`
**King James Version downloader**
- Downloads complete KJV (1611/1769)
- 66 books, ~31,102 verses
- Uses GetBible API
- Improved version (single file download)
- **Usage:** `python3 download_kjv_improved.py`

### `download_web_improved.py`
**World English Bible downloader**
- Downloads complete WEB (2020)
- Modern English translation
- 66 books, ~31,086 verses
- Easiest to read
- **Usage:** `python3 download_web_improved.py`

### `download_asv.py`
**American Standard Version downloader**
- Downloads complete ASV (1901)
- Scholarly translation
- 66 books, ~31,102 verses
- Classic English
- **Usage:** `python3 download_asv.py`

### `download_ylt.py`
**Young's Literal Translation downloader**
- Downloads complete YLT (1898)
- Most literal translation
- 66 books, ~31,098 verses
- Word-for-word accuracy
- **Usage:** `python3 download_ylt.py`

### Legacy Download Scripts (Reference Only)

#### `download_kjv.py`
- Old version (downloads 66 files individually)
- Slower and less reliable
- Use `download_kjv_improved.py` instead

#### `download_web.py`
- Old version
- Use `download_web_improved.py` instead

#### `download_bible.py`
- Creates sample data with ~50 popular verses
- For quick testing only
- Use full download scripts for production

---

## 📚 Documentation Files

### `README.md`
**Main project README (this will be GitHub README)**
- Project overview
- Quick start guide
- Feature list
- Hardware requirements
- Links to detailed documentation
- **Audience:** GitHub visitors, new users

### `INSTALLATION.md`
**Complete installation guide**
- Detailed step-by-step instructions
- Hardware connection diagrams
- Software installation
- Bible data download instructions
- Troubleshooting section
- **Audience:** Beginners, first-time setup
- **Size:** ~12 KB

### `HOURLY_SETUP.md`
**Hourly update configuration**
- How to set up automatic hourly updates
- Cron job examples
- Systemd timer setup
- Different schedule options
- Troubleshooting automation
- **Audience:** Users setting up automation
- **Size:** ~8.2 KB

### `TRANSLATIONS_GUIDE.md`
**Bible translation comparison**
- Details on all 4 translations
- Comparison table
- Sample verses
- Download instructions
- Translation switching guide
- **Audience:** Users choosing translations
- **Size:** ~9.0 KB

### `QUICK_REFERENCE.md`
**Command cheat sheet**
- Common commands
- Quick troubleshooting
- File locations
- System commands
- **Audience:** Daily users, quick lookup
- **Size:** ~5.0 KB

### `QUICK_START_DOWNLOADS.md`
**Bible download quick guide**
- Simple download instructions
- Which script to use
- Comparison of old vs new scripts
- **Audience:** Users downloading Bibles
- **Size:** ~4.4 KB

### `BIBLE_DOWNLOADS.md`
**Comprehensive Bible download guide**
- All available sources
- Copyright information
- Format conversion
- Multiple download methods
- Alternative translations
- **Audience:** Advanced users
- **Size:** ~8.0 KB

### `DOWNLOAD_SIMPLE.md`
**Simplified download guide**
- 3-step process
- For absolute beginners
- Why can't download NIV
- **Audience:** Non-technical users
- **Size:** ~6.0 KB

### `CORRECTION_DARBY_YLT.md`
**Correction notice**
- Explains Darby (French) vs YLT (English) issue
- Why YLT replaced Darby
- Comparison between them
- **Audience:** Users who saw original recommendation
- **Size:** ~3.6 KB

---

## 🔧 System Files

### `.gitignore`
**Git ignore rules**
- Excludes Python cache files
- Excludes downloaded Bible data (too large)
- Excludes log files
- Excludes IDE settings
- Includes system files to ignore

### `LICENSE`
**MIT License**
- Open source license
- Allows free use, modification, distribution
- Includes notices for Bible translations
- Third-party library acknowledgments

---

## 📁 Directory Structure

```
bible-epaper-display/
├── Core Files
│   ├── bible_display.py          # Main application
│   ├── config.json                # Configuration
│   ├── requirements.txt           # Dependencies
│   └── setup.sh                   # Setup automation
│
├── Download Scripts
│   ├── download_all_bibles.py     # Download all 4 translations
│   ├── download_kjv_improved.py   # KJV downloader
│   ├── download_web_improved.py   # WEB downloader
│   ├── download_asv.py            # ASV downloader
│   ├── download_ylt.py            # YLT downloader
│   ├── download_kjv.py            # Legacy (reference)
│   ├── download_web.py            # Legacy (reference)
│   └── download_bible.py          # Sample data creator
│
├── Documentation
│   ├── README.md                  # Main README (GitHub)
│   ├── INSTALLATION.md            # Setup guide
│   ├── HOURLY_SETUP.md           # Automation guide
│   ├── TRANSLATIONS_GUIDE.md      # Translation details
│   ├── QUICK_REFERENCE.md        # Command cheat sheet
│   ├── QUICK_START_DOWNLOADS.md  # Download quick start
│   ├── BIBLE_DOWNLOADS.md        # Comprehensive download guide
│   ├── DOWNLOAD_SIMPLE.md        # Simple download guide
│   └── CORRECTION_DARBY_YLT.md   # Correction notice
│
├── System Files
│   ├── .gitignore                 # Git ignore rules
│   ├── LICENSE                    # MIT License
│   └── PROJECT_FILES.md          # This file
│
└── Runtime Directories (created during setup)
    ├── bible_data/                # Bible JSON files
    │   ├── kjv.json              # (downloaded, not in repo)
    │   ├── web.json              # (downloaded, not in repo)
    │   ├── asv.json              # (downloaded, not in repo)
    │   └── ylt.json              # (downloaded, not in repo)
    ├── waveshare_epd/            # Waveshare library (downloaded)
    ├── bible_display.log         # Runtime log file
    └── last_displayed.png        # Debug image
```

---

## 📊 File Statistics

### By Category

| Category | Files | Total Size |
|----------|-------|------------|
| Core Application | 4 | ~13 KB |
| Download Scripts | 8 | ~50 KB |
| Documentation | 9 | ~66 KB |
| System Files | 3 | ~4 KB |
| **Total** | **24** | **~133 KB** |

### Documentation Hierarchy

```
README.md (Start here!)
├── INSTALLATION.md (For setup)
│   ├── Hardware setup
│   ├── Software installation
│   └── QUICK_REFERENCE.md (Commands)
│
├── Bible Downloads
│   ├── QUICK_START_DOWNLOADS.md (Simple guide)
│   ├── TRANSLATIONS_GUIDE.md (Details)
│   └── BIBLE_DOWNLOADS.md (Advanced)
│
└── HOURLY_SETUP.md (Automation)
```

---

## 🎯 Which File Do I Need?

### First Time Setup
1. `README.md` - Overview
2. `INSTALLATION.md` - Step-by-step setup
3. `setup.sh` - Run this script
4. `download_all_bibles.py` - Get Bible data
5. `HOURLY_SETUP.md` - Automate updates

### Switching Translations
1. `TRANSLATIONS_GUIDE.md` - Compare translations
2. `download_*.py` - Download needed translation
3. `config.json` - Edit this to switch

### Troubleshooting
1. `QUICK_REFERENCE.md` - Common commands
2. `INSTALLATION.md` - Troubleshooting section
3. `bible_display.log` - Check logs

### Daily Use
1. `QUICK_REFERENCE.md` - Command reference
2. `config.json` - Adjust settings
3. `bible_display.log` - Monitor operation

---

## 🔄 File Updates

### Core files that may need updates:
- `bible_display.py` - Bug fixes, features
- `config.json` - User customization
- `requirements.txt` - Dependency versions

### Files that shouldn't need changes:
- Documentation (unless correcting errors)
- Download scripts (unless API changes)
- License files

---

## 📝 Notes

### Files NOT in Repository

These files are generated during setup or runtime:

- `bible_data/*.json` - Too large for GitHub (4-5 MB each)
- `waveshare_epd/` - Downloaded during setup
- `bible_display.log` - Generated at runtime
- `last_displayed.png` - Debug output
- `__pycache__/` - Python cache

### Legacy Files

Kept for reference but superseded by improved versions:
- `download_kjv.py` → Use `download_kjv_improved.py`
- `download_web.py` → Use `download_web_improved.py`
- `download_bible.py` → Use full download scripts

---

## 🎁 Optional Files You Can Add

### Systemd Service Files
Create in `/etc/systemd/system/`:
- `bible-display.service` - Service definition
- `bible-display.timer` - Timer configuration

See HOURLY_SETUP.md for templates.

### Cron Configuration
Add to crontab:
```
0 * * * * /usr/bin/python3 /path/to/bible_display.py
```

---

## 📦 Complete GitHub Upload Checklist

- ✅ Core application files (4 files)
- ✅ Download scripts (8 files)
- ✅ Documentation (9 files)
- ✅ System files (.gitignore, LICENSE, PROJECT_FILES.md)
- ✅ README.md as main GitHub README
- ⬜ Create `bible_data/.gitkeep` (empty directory placeholder)
- ⬜ Screenshots (if available)
- ⬜ Hardware photos (optional)

---

**Total Files to Upload: 24**

All files are ready in `/mnt/user-data/outputs/` directory!
