# Daily Bible Verse Display - Installation Guide

## Overview
This guide will help you set up your Raspberry Pi Zero 2 with a Waveshare 2.13" V4 e-paper display to show a different Bible verse each day.

## What You'll Need
- Raspberry Pi Zero 2 W (with Raspberry Pi OS installed)
- Waveshare 2.13" e-Paper Display V4
- SD card (8GB or larger)
- Power supply for Raspberry Pi
- Computer to access the Pi (via SSH or directly with keyboard/monitor)

---

## Part 1: Initial Raspberry Pi Setup

### 1.1 Install Raspberry Pi OS
If you haven't already:
1. Download Raspberry Pi Imager from https://www.raspberrypi.com/software/
2. Flash Raspberry Pi OS Lite (or Desktop) to your SD card
3. Enable SSH (create empty file named `ssh` on boot partition)
4. Configure WiFi if using Pi Zero W

### 1.2 Connect to Your Raspberry Pi
**Via SSH:**
```bash
ssh pi@raspberrypi.local
# Default password is usually 'raspberry'
```

**Or** connect a keyboard and monitor directly.

### 1.3 Update Your System
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

---

## Part 2: Hardware Connection

### 2.1 Connect the E-Paper Display
The Waveshare display connects to the Raspberry Pi GPIO pins. The display should come with a ribbon cable that connects to specific pins.

**Connection pins (typical for Waveshare 2.13" V4):**
- VCC → 3.3V (Pin 1)
- GND → GND (Pin 6)
- DIN → MOSI (Pin 19)
- CLK → SCLK (Pin 23)
- CS → CE0 (Pin 24)
- DC → GPIO 25 (Pin 22)
- RST → GPIO 17 (Pin 11)
- BUSY → GPIO 24 (Pin 18)

⚠️ **Important:** Connect the display while the Pi is powered OFF.

### 2.2 Enable SPI Interface
SPI must be enabled for the display to work:

```bash
sudo raspi-config
```

Navigate to:
- **Interface Options** → **SPI** → **Yes** → **OK** → **Finish**
- Reboot when prompted: `sudo reboot`

---

## Part 3: Install the Bible Display Software

### 3.1 Transfer Files to Raspberry Pi

You have several options:

**Option A: Using SCP (from your computer)**
```bash
# Navigate to where you downloaded the files
scp bible_display.py config.json requirements.txt setup.sh pi@raspberrypi.local:~/
```

**Option B: Using USB/File Transfer**
- Copy files to a USB drive
- Mount USB on Pi and copy files

**Option C: Using Git** (if files are in a repository)
```bash
git clone [your-repo-url]
cd [repo-name]
```

### 3.2 Run the Setup Script

```bash
# Navigate to the directory with your files
cd ~  # or wherever you copied the files

# Make setup script executable
chmod +x setup.sh

# Run the setup script
./setup.sh
```

The setup script will:
- Install all necessary Python packages
- Enable SPI interface
- Download Waveshare e-Paper library
- Create necessary directories
- Make scripts executable

**If the script asks you to reboot, do so:**
```bash
sudo reboot
```

---

## Part 4: Download Bible Translation Data

The Bible verse data needs to be downloaded separately. Here are your options:

### Option 1: Use Pre-formatted JSON Files (Recommended)

I'll provide a Python script to download Bible data:

Create a file called `download_bible.py`:

```python
#!/usr/bin/env python3
"""
Download Bible translation data
"""
import json
import urllib.request
import os

# Create bible_data directory if it doesn't exist
os.makedirs('bible_data', exist_ok=True)

def download_niv():
    """Download NIV translation"""
    print("Downloading NIV Bible data...")
    
    # Using Bible API to download verse by verse
    # This is a simplified example - you may want to use a different source
    url = "https://bible-api.com/john+3:16?translation=kjv"
    
    # Note: For a complete Bible, you'll need a different approach
    # See below for alternative methods
    print("Note: You'll need to obtain complete Bible JSON files")
    print("See instructions below...")

# For now, we'll provide instructions for manual download
print("""
To get complete Bible translation data:

METHOD 1: Use getbible.net API
1. Visit: https://getbible.net/
2. This provides JSON format Bibles in many translations
3. Download your preferred translation

METHOD 2: Use openbible.com data
1. Visit: https://github.com/honza/bibles
2. Download JSON format Bibles
3. Place in the bible_data/ directory

METHOD 3: Contact me for formatted data files
- I can provide pre-formatted NIV, KJV, ESV files

For testing, I'll create a sample with a few verses...
""")

# Create a sample Bible file for testing
sample_bible = {
    "translation": "NIV",
    "books": [
        {
            "name": "John",
            "chapters": [
                {
                    "chapter": 3,
                    "verses": [
                        {
                            "verse": 16,
                            "text": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Psalm",
            "chapters": [
                {
                    "chapter": 23,
                    "verses": [
                        {
                            "verse": 1,
                            "text": "The Lord is my shepherd, I lack nothing."
                        }
                    ]
                }
            ]
        },
        {
            "name": "Proverbs",
            "chapters": [
                {
                    "chapter": 3,
                    "verses": [
                        {
                            "verse": 5,
                            "text": "Trust in the Lord with all your heart and lean not on your own understanding."
                        },
                        {
                            "verse": 6,
                            "text": "In all your ways submit to him, and he will make your paths straight."
                        }
                    ]
                }
            ]
        }
    ]
}

with open('bible_data/niv.json', 'w') as f:
    json.dump(sample_bible, f, indent=2)

print("\nCreated sample NIV file with a few verses for testing!")
print("File: bible_data/niv.json")
print("\nYou can now test the display with: python3 bible_display.py")
print("\nTo add more verses, edit the niv.json file or download a complete translation.")
```

Save this and run:
```bash
python3 download_bible.py
```

### Option 2: Complete Bible JSON Format

The expected JSON format is:
```json
{
  "translation": "NIV",
  "books": [
    {
      "name": "Genesis",
      "chapters": [
        {
          "chapter": 1,
          "verses": [
            {
              "verse": 1,
              "text": "In the beginning God created the heavens and the earth."
            }
          ]
        }
      ]
    }
  ]
}
```

You can find complete Bible JSONs at:
- https://github.com/aruljohn/Bible-kjv (KJV)
- https://getbible.net/ (Multiple translations)

**Important:** Rename your downloaded file to match the translation code in lowercase (e.g., `niv.json`, `kjv.json`, `esv.json`) and place in the `bible_data/` directory.

---

## Part 5: Test the Display

### 5.1 Manual Test
```bash
python3 bible_display.py
```

You should see:
- Log messages in the terminal
- The display should update with today's verse
- A file `last_displayed.png` is saved (you can view this to see what was displayed)

### 5.2 Check the Logs
```bash
cat bible_display.log
```

---

## Part 6: Set Up Automatic Daily Updates

### 6.1 Using Cron (Recommended for Beginners)

Cron will run the script automatically every day.

Edit crontab:
```bash
crontab -e
```

Add this line at the end (updates at 6:00 AM daily):
```
0 6 * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

Change `/home/pi/` to wherever you installed the files.

**To change the time:**
- `0 6` means 6:00 AM
- `0 8` would be 8:00 AM
- `30 7` would be 7:30 AM

Save and exit (Ctrl+X, then Y, then Enter in nano).

### 6.2 Using Systemd Timer (Advanced)

If you want more control, you can use a systemd service.

Create service file:
```bash
sudo nano /etc/systemd/system/bible-display.service
```

Add:
```ini
[Unit]
Description=Daily Bible Verse Display
After=network.target

[Service]
Type=oneshot
User=pi
WorkingDirectory=/home/pi
ExecStart=/usr/bin/python3 /home/pi/bible_display.py
StandardOutput=append:/home/pi/bible_display.log
StandardError=append:/home/pi/bible_display.log

[Install]
WantedBy=multi-user.target
```

Create timer file:
```bash
sudo nano /etc/systemd/system/bible-display.timer
```

Add:
```ini
[Unit]
Description=Daily Bible Verse Display Timer
Requires=bible-display.service

[Timer]
OnCalendar=daily
OnCalendar=*-*-* 06:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable bible-display.timer
sudo systemctl start bible-display.timer
```

Check status:
```bash
sudo systemctl status bible-display.timer
```

---

## Part 7: Customization

### 7.1 Change Bible Translation

Edit `config.json`:
```bash
nano config.json
```

Change the translation:
```json
{
  "translation": "KJV",
  ...
}
```

Make sure you have `kjv.json` in the `bible_data/` directory!

### 7.2 Adjust Font Sizes

In `config.json`:
```json
{
  "font_size_reference": 16,
  "font_size_text": 14,
  ...
}
```

### 7.3 Rotate Display

If you mount the display sideways:
```json
{
  "display_rotation": 90,
  ...
}
```

Options: 0, 90, 180, 270

---

## Troubleshooting

### Display Not Working
1. **Check connections:** Ensure all wires are properly connected
2. **Verify SPI is enabled:**
   ```bash
   lsmod | grep spi
   ```
   Should show `spi_bcm2835`

3. **Check permissions:**
   ```bash
   sudo usermod -a -G spi,gpio pi
   ```

### "No module named 'waveshare_epd'"
Run the setup script again:
```bash
./setup.sh
```

### Display Shows Nothing
- Check `last_displayed.png` to see if image is being generated
- Look at `bible_display.log` for errors
- Try the Waveshare demo code to verify hardware works

### Bible Data Not Found
- Make sure JSON file is in `bible_data/` directory
- Check filename matches translation in `config.json` (lowercase)
- Verify JSON format is correct

### Script Doesn't Run Automatically
- Check crontab: `crontab -l`
- View cron logs: `grep CRON /var/log/syslog`
- Test manually first: `python3 bible_display.py`

---

## Getting Help

If you encounter issues:

1. **Check the log file:**
   ```bash
   cat bible_display.log
   ```

2. **Run in verbose mode:**
   The script already logs everything

3. **Test components separately:**
   - Test e-paper with Waveshare examples
   - Verify Bible JSON loads correctly
   - Check image generation (look at last_displayed.png)

4. **Common issues:**
   - SPI not enabled → Run `sudo raspi-config`
   - Wrong GPIO pins → Double-check wiring
   - Permissions → Run `sudo chmod +x bible_display.py`
   - Missing fonts → Install: `sudo apt-get install fonts-dejavu`

---

## Tips for Success

1. **Start simple:** Test with the sample Bible data first
2. **Check logs often:** The log file shows exactly what's happening
3. **Test manually:** Before setting up automation, make sure it works manually
4. **Backup your config:** Save copies of your working configuration
5. **Be patient:** E-paper displays are slow - updates take 5-15 seconds

---

## Power Considerations

E-paper displays only use power when updating. To save energy:

1. The display holds the image without power
2. Power down Pi when not updating (optional):
   ```bash
   sudo poweroff
   ```
3. Use a timer to power on only during update times (requires hardware timer)

---

## Maintenance

- **Weekly:** Check logs for errors
- **Monthly:** Update system packages
- **As needed:** Add new Bible translations
- **Yearly:** Clean display with soft, dry cloth

---

## What's Next?

Once your display is working:

- Add multiple Bible translations
- Customize the layout
- Add weather or other information
- Create different verse selection algorithms
- Add a physical button to manually refresh

Enjoy your daily Bible verse display! 🙏
