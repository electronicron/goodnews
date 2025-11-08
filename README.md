# Automated Bible Verse E-Paper Display

Display a different Bible verse every hour on your Raspberry Pi with Waveshare e-paper display!

![Project Type](https://img.shields.io/badge/project-Raspberry%20Pi-red)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Overview

This project turns your Raspberry Pi Zero 2 with a Waveshare 2.13" e-paper display into an automated Bible verse display that shows a new verse every hour. Perfect for homes, offices, or as a thoughtful gift!

### Features

- ✅ **Hourly updates** - New verse every hour (configurable)
- ✅ **Multiple translations** - KJV, WEB, ASV, YLT (all public domain)
- ✅ **Low power** - E-paper only uses power during updates
- ✅ **Offline** - Works without internet after setup
- ✅ **Easy setup** - Automated installation scripts
- ✅ **Beginner friendly** - Detailed documentation with hand-holding

## 🖼️ What It Does

- Displays a random Bible verse on an e-paper screen
- Updates automatically every hour (or daily, or any schedule you choose)
- Shows the verse reference, text, and date
- Changes verse at the top of each hour
- Same verse displays consistently throughout the hour

## 🛠️ Hardware Requirements

- **Raspberry Pi Zero 2 W** (or any Raspberry Pi model)
- **Waveshare 2.13" e-Paper Display V4**
- MicroSD card (8GB or larger)
- Power supply for Raspberry Pi
- Internet connection for initial setup

## 🚀 Quick Start

### 1. Clone Repository

```bash
cd ~
git clone https://github.com/yourusername/bible-epaper-display.git
cd bible-epaper-display
```

### 2. Run Setup

```bash
chmod +x setup.sh
./setup.sh
```

### 3. Download Bible Data

Choose one:

```bash
# Download all 4 translations (recommended)
python3 download_all_bibles.py

# Or download individually
python3 download_kjv_improved.py  # King James Version
python3 download_web_improved.py  # World English Bible (modern)
python3 download_asv.py           # American Standard Version
python3 download_ylt.py           # Young's Literal Translation
```

### 4. Test Display

```bash
python3 bible_display.py
```

### 5. Set Up Automatic Updates

**Using Cron (Easiest):**
```bash
crontab -e
# Add: 0 * * * * /usr/bin/python3 /home/pi/bible-epaper-display/bible_display.py
```

**Using Systemd (Recommended):**
See [HOURLY_SETUP.md](HOURLY_SETUP.md) for detailed instructions.

## 📚 Available Bible Translations

All translations are public domain and free to use:

| Translation | Year | Style | Best For |
|-------------|------|-------|----------|
| **WEB** | 2020 | Modern English | Daily reading ⭐ |
| **KJV** | 1611 | Traditional | Classic style |
| **ASV** | 1901 | Scholarly | Bible study |
| **YLT** | 1898 | Most literal | Word-for-word study |

Switch translations by editing `config.json`:

```json
{
  "translation": "WEB",
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
```

## 📁 Project Structure

```
bible-epaper-display/
├── bible_display.py              # Main display script
├── config.json                   # Configuration file
├── requirements.txt              # Python dependencies
├── setup.sh                      # Automated setup script
├── download_all_bibles.py        # Download all translations
├── download_kjv_improved.py      # Download KJV
├── download_web_improved.py      # Download WEB
├── download_asv.py               # Download ASV
├── download_ylt.py               # Download YLT
├── README.md                     # This file
├── INSTALLATION.md               # Detailed installation guide
├── HOURLY_SETUP.md              # Hourly update setup
├── TRANSLATIONS_GUIDE.md         # Translation comparison
├── QUICK_REFERENCE.md           # Command cheat sheet
└── docs/                        # Additional documentation
```

## 📖 Documentation

- **[INSTALLATION.md](INSTALLATION.md)** - Complete setup guide (start here!)
- **[HOURLY_SETUP.md](HOURLY_SETUP.md)** - Configure hourly updates
- **[TRANSLATIONS_GUIDE.md](TRANSLATIONS_GUIDE.md)** - Bible translation details
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Common commands
- **[QUICK_START_DOWNLOADS.md](QUICK_START_DOWNLOADS.md)** - Bible download guide

## 🔧 Configuration Options

Edit `config.json` to customize:

```json
{
  "translation": "WEB",           // Bible translation (KJV, WEB, ASV, YLT)
  "font_size_reference": 14,      // Verse reference size
  "font_size_text": 12,           // Verse text size
  "display_rotation": 0           // Rotation (0, 90, 180, 270)
}
```

## 🕐 Update Schedules

### Hourly Updates (Default)
```bash
crontab -e
# Add: 0 * * * * /usr/bin/python3 /path/to/bible_display.py
```

### Daily Updates
```bash
crontab -e
# Add: 0 6 * * * /usr/bin/python3 /path/to/bible_display.py
```

### Every 30 Minutes
```bash
crontab -e
# Add: 0,30 * * * * /usr/bin/python3 /path/to/bible_display.py
```

See [HOURLY_SETUP.md](HOURLY_SETUP.md) for more scheduling options.

## 🐛 Troubleshooting

### Display Not Working
- Check GPIO connections
- Verify SPI is enabled: `lsmod | grep spi`
- Run: `sudo raspi-config` → Interface Options → SPI → Enable

### Script Errors
- Check logs: `cat bible_display.log`
- Test manually: `python3 bible_display.py`
- Verify paths in systemd service files

### No Bible Data
- Download Bible files: `python3 download_all_bibles.py`
- Check: `ls bible_data/`
- Verify `config.json` has correct translation name

See [INSTALLATION.md](INSTALLATION.md) for detailed troubleshooting.

## 💡 Tips

- **Start with WEB** - Modern English, easiest to read
- **Test manually first** - Before setting up automation
- **Check logs** - `bible_display.log` shows what happened
- **Use systemd** - More reliable than cron for services
- **Backup config** - Save your working configuration

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Share your setup photos!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Bible Translations
All included Bible translations (KJV, WEB, ASV, YLT) are in the public domain.

### Third-Party Libraries
- **Waveshare e-Paper library** - See their repository for license
- **Pillow** - PIL Software License
- **Python** - PSF License

## 🙏 Acknowledgments

- **Waveshare** - For e-paper display hardware and libraries
- **GetBible.net** - For providing public domain Bible translations
- **Bible translation teams** - For their faithful work

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions
- **Documentation**: Check the docs/ folder

## 🌟 Show Your Support

If this project helped you, please:
- ⭐ Star this repository
- 📸 Share photos of your setup
- 🐛 Report bugs or suggest features
- 📖 Improve documentation

## 📸 Gallery

Share your setup! Open an issue or PR to add your photo here.

---

**Made with ❤️ for daily Bible reading**

Enjoy your automated Bible verse display! 🙏📖
