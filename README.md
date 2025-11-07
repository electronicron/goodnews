# Daily Bible Verse Display

Display a different Bible verse each day on your Raspberry Pi with e-paper display!

## 📖 What This Does

- Shows a random Bible verse on your e-paper display
- Changes automatically every day at 6 AM (configurable)
- Works offline after setup
- Easy to switch between Bible translations
- Low power consumption (e-paper only uses power during updates)

## 🛠️ Hardware Requirements

- Raspberry Pi Zero 2 W (or any Raspberry Pi)
- Waveshare 2.13" e-Paper Display V4
- MicroSD card (8GB+)
- Power supply

## 📦 What's Included

- `bible_display.py` - Main display script
- `config.json` - Easy configuration file
- `setup.sh` - Automated setup script
- `download_bible.py` - Helper to create sample Bible data
- `INSTALLATION.md` - Detailed step-by-step guide
- `requirements.txt` - Python dependencies

## 🚀 Quick Start

### 1. Transfer files to your Raspberry Pi
```bash
# From your computer
scp *.py *.sh *.json *.txt *.md pi@raspberrypi.local:~/
```

### 2. Connect to your Pi and run setup
```bash
ssh pi@raspberrypi.local
chmod +x setup.sh
./setup.sh
```

### 3. Create sample Bible data
```bash
python3 download_bible.py
```

### 4. Test the display
```bash
python3 bible_display.py
```

### 5. Set up automatic daily updates
```bash
crontab -e
# Add: 0 6 * * * /usr/bin/python3 /home/pi/bible_display.py
```

**For detailed instructions, see [INSTALLATION.md](INSTALLATION.md)**

## ⚙️ Configuration

Edit `config.json` to customize:

```json
{
  "translation": "NIV",           // Bible translation (NIV, KJV, ESV, etc.)
  "font_size_reference": 14,      // Size of verse reference
  "font_size_text": 12,           // Size of verse text
  "display_rotation": 0           // Rotate display (0, 90, 180, 270)
}
```

## 🔄 Switching Bible Translations

1. Make sure you have the translation JSON file in `bible_data/`
2. Edit `config.json` and change `"translation": "NIV"` to your desired translation
3. Run `python3 bible_display.py` to update

## 📁 Project Structure

```
├── bible_display.py        # Main application
├── config.json            # Configuration settings
├── setup.sh              # Setup automation script
├── download_bible.py     # Bible data helper
├── requirements.txt      # Python packages
├── INSTALLATION.md       # Detailed guide
├── README.md            # This file
└── bible_data/          # Bible translation files
    ├── niv.json
    ├── kjv.json
    └── esv.json
```

## 🐛 Troubleshooting

### Display not updating?
- Check connections to GPIO pins
- Verify SPI is enabled: `lsmod | grep spi`
- Check logs: `cat bible_display.log`

### No Bible verses showing?
- Ensure JSON file exists: `ls bible_data/`
- Check filename matches config.json
- Verify JSON format is correct

### Script not running automatically?
- Verify cron job: `crontab -l`
- Check system logs: `grep CRON /var/log/syslog`
- Test manually first

**For more help, see [INSTALLATION.md](INSTALLATION.md)**

## 📊 Features

- ✅ Random verse selection (different each day)
- ✅ Multiple Bible translation support
- ✅ Automatic daily updates
- ✅ Low power consumption
- ✅ Offline operation
- ✅ Easy configuration
- ✅ Detailed logging
- ✅ Debug image output

## 🔮 Future Ideas

- Add multiple verses per day
- Include daily devotional
- Weather information
- Calendar events
- Manual refresh button
- Web interface for configuration

## 📝 Notes

- The same verse is shown all day (based on date seed)
- Verse changes automatically at midnight
- Display only updates when script runs
- E-paper retains image without power

## 🙏 Getting Complete Bible Data

The included sample data has popular verses for testing. For complete Bibles:

1. Visit https://getbible.net/
2. Download your preferred translation in JSON format
3. Place in `bible_data/` directory
4. Rename to match translation code (e.g., `niv.json`)

See INSTALLATION.md for more sources and detailed instructions.

## 💡 Tips

- Start with sample data to verify everything works
- Keep the display out of direct sunlight
- Clean display gently with dry cloth
- Save power by updating only once daily
- Backup your configuration files

## 📄 License

Free to use for personal projects. Bible text copyright belongs to respective translation publishers.

## 🤝 Support

If you encounter issues:
1. Check the log file: `cat bible_display.log`
2. Review INSTALLATION.md troubleshooting section
3. Verify all connections and settings
4. Test components individually

---

Enjoy your daily Bible verse display! 🙏📖
