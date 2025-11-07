# Quick Reference - Common Commands

## 🚀 Initial Setup
```bash
# Run setup script
./setup.sh

# Create sample Bible data
python3 download_bible.py

# Make scripts executable
chmod +x *.sh *.py
```

## 🖥️ Running the Display

```bash
# Run once manually
python3 bible_display.py

# View what was displayed (on Pi desktop or copy file)
feh last_displayed.png  # or use image viewer
```

## 📝 View Logs

```bash
# View all logs
cat bible_display.log

# View most recent logs
tail -n 20 bible_display.log

# Watch logs in real-time
tail -f bible_display.log
```

## ⚙️ Configuration

```bash
# Edit configuration
nano config.json

# View current config
cat config.json
```

## 🔄 Bible Translations

```bash
# Check available translations
ls bible_data/

# Add a new translation
# 1. Download JSON file
# 2. Place in bible_data/
# 3. Rename to lowercase (e.g., esv.json)
# 4. Edit config.json

# Switch translation
nano config.json  # Change "translation" value
python3 bible_display.py  # Test new translation
```

## ⏰ Automatic Updates (Cron)

```bash
# Edit cron schedule
crontab -e

# View current cron jobs
crontab -l

# Example cron entries:
# Daily at 6 AM
0 6 * * * /usr/bin/python3 /home/pi/bible_display.py

# Daily at 8:30 AM
30 8 * * * /usr/bin/python3 /home/pi/bible_display.py

# Every 12 hours
0 */12 * * * /usr/bin/python3 /home/pi/bible_display.py
```

## 🔧 Troubleshooting Commands

```bash
# Check if SPI is enabled
lsmod | grep spi

# Enable SPI (then reboot)
sudo raspi-config
# Navigate to: Interface Options → SPI → Yes

# Check GPIO permissions
groups pi  # Should include 'gpio' and 'spi'

# Add user to groups if needed
sudo usermod -a -G spi,gpio pi

# Check Python packages
pip3 list | grep -E 'Pillow|spidev|RPi.GPIO'

# Test Waveshare library
ls waveshare_epd/

# Verify Bible data
python3 -c "import json; print(json.load(open('bible_data/niv.json'))['translation'])"
```

## 🖼️ Image Testing

```bash
# View last displayed image
# Option 1: Using feh (install: sudo apt-get install feh)
feh last_displayed.png

# Option 2: Copy to your computer
scp pi@raspberrypi.local:~/last_displayed.png .

# Option 3: If using Pi Desktop
xdg-open last_displayed.png
```

## 📦 Package Management

```bash
# Update system packages
sudo apt-get update
sudo apt-get upgrade

# Install Python package
pip3 install --break-system-packages <package-name>

# Reinstall requirements
pip3 install --break-system-packages -r requirements.txt
```

## 🔄 Git Operations (if using version control)

```bash
# Clone repository
git clone <your-repo-url>
cd <repo-name>

# Pull updates
git pull

# Check status
git status
```

## 🔌 Hardware Testing

```bash
# Check GPIO pins
pinout

# Test SPI communication
ls /dev/spi*  # Should show /dev/spidev0.0

# Monitor system logs during script run
tail -f /var/log/syslog
```

## 🛑 System Control

```bash
# Reboot Pi
sudo reboot

# Shutdown Pi
sudo poweroff

# Check Pi temperature
vcgencmd measure_temp

# Check Pi memory
free -h
```

## 🎨 Customization

```bash
# List available fonts
fc-list | grep -i dejavu

# Change font size (in config.json)
nano config.json
# Modify: "font_size_text" and "font_size_reference"

# Rotate display (in config.json)
nano config.json
# Modify: "display_rotation" (0, 90, 180, 270)
```

## 📊 System Information

```bash
# Check Pi model
cat /proc/cpuinfo | grep Model

# Check OS version
cat /etc/os-release

# Check Python version
python3 --version

# Check disk space
df -h

# Check running processes
ps aux | grep python
```

## 🔍 Debugging

```bash
# Run with Python verbose output
python3 -v bible_display.py

# Check for Python errors
python3 -m py_compile bible_display.py

# Test Bible data loading
python3 -c "
import json
with open('bible_data/niv.json') as f:
    data = json.load(f)
    print(f\"Books: {len(data['books'])}\")
"

# Test image creation only (without hardware)
# Edit bible_display.py and comment out display_on_epaper() call
```

## 📱 Remote Access

```bash
# SSH into Pi
ssh pi@raspberrypi.local

# Copy files TO Pi
scp file.txt pi@raspberrypi.local:~/

# Copy files FROM Pi
scp pi@raspberrypi.local:~/file.txt .

# Copy entire directory
scp -r directory/ pi@raspberrypi.local:~/
```

## 🆘 Emergency Recovery

```bash
# If display is frozen
# Power cycle the Pi (unplug and plug back in)

# If script won't stop
ps aux | grep python  # Find PID
kill <PID>

# Remove all cron jobs (if needed)
crontab -r

# Restore default config
cat > config.json << 'EOF'
{
  "translation": "NIV",
  "font_size_reference": 14,
  "font_size_text": 12,
  "display_rotation": 0
}
EOF
```

## 📚 Helpful Resources

- Waveshare documentation: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(D)
- Raspberry Pi GPIO pinout: https://pinout.xyz/
- Cron schedule generator: https://crontab.guru/
- Bible data sources: See INSTALLATION.md

---

**Remember:** 
- Always test manually before setting up automation
- Check logs when things don't work as expected
- Make backups of working configurations
- Be patient - e-paper displays take time to update (5-15 seconds)
