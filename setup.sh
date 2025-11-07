#!/bin/bash
# Setup script for Daily Bible Verse Display
# This script will install all necessary dependencies and set up the display

set -e  # Exit on any error

echo "======================================"
echo "Daily Bible Verse Display Setup"
echo "======================================"
echo ""

# Check if running on Raspberry Pi
if ! grep -q "Raspberry Pi" /proc/cpuinfo; then
    echo "Warning: This doesn't appear to be a Raspberry Pi"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Step 1: Updating system packages..."
sudo apt-get update

echo ""
echo "Step 2: Installing system dependencies..."
sudo apt-get install -y python3-pip python3-pil python3-numpy git

echo ""
echo "Step 3: Enabling SPI interface..."
# Enable SPI if not already enabled
if ! grep -q "dtparam=spi=on" /boot/config.txt; then
    echo "Enabling SPI in /boot/config.txt..."
    echo "dtparam=spi=on" | sudo tee -a /boot/config.txt
    echo "Note: You'll need to reboot for SPI to be enabled"
    NEED_REBOOT=1
else
    echo "SPI is already enabled"
fi

echo ""
echo "Step 4: Installing Python dependencies..."
pip3 install --break-system-packages -r requirements.txt

echo ""
echo "Step 5: Installing Waveshare e-Paper library..."
if [ ! -d "waveshare_epd" ]; then
    echo "Downloading Waveshare e-Paper library..."
    git clone https://github.com/waveshare/e-Paper.git waveshare_temp
    cp -r waveshare_temp/RaspberryPi_JetsonNano/python/lib/waveshare_epd .
    rm -rf waveshare_temp
    echo "Waveshare library installed!"
else
    echo "Waveshare library already exists"
fi

echo ""
echo "Step 6: Creating bible_data directory..."
mkdir -p bible_data

echo ""
echo "Step 7: Downloading NIV Bible data..."
# Download Bible data
cd bible_data

if [ ! -f "niv.json" ]; then
    echo "Downloading NIV translation..."
    # We'll provide instructions to manually download or use a simple format
    cat > niv.json << 'EOF'
{
  "translation": "NIV",
  "note": "This is a placeholder. Please download actual Bible data.",
  "books": []
}
EOF
    echo "Placeholder created. You'll need to add actual Bible data."
    NEED_BIBLE_DATA=1
else
    echo "Bible data already exists"
fi

cd "$SCRIPT_DIR"

echo ""
echo "Step 8: Making scripts executable..."
chmod +x bible_display.py
chmod +x setup.sh

echo ""
echo "Step 9: Testing display (dry run)..."
echo "Attempting to run the display script..."
# Don't fail if this doesn't work yet
python3 bible_display.py || echo "Script run completed (may have errors if Bible data not loaded)"

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""

if [ "$NEED_REBOOT" = "1" ]; then
    echo "⚠️  IMPORTANT: You need to REBOOT for SPI to be enabled:"
    echo "    sudo reboot"
    echo ""
fi

if [ "$NEED_BIBLE_DATA" = "1" ]; then
    echo "⚠️  BIBLE DATA NEEDED:"
    echo "    You need to download actual Bible data files."
    echo "    See INSTALLATION.md for instructions."
    echo ""
fi

echo "Next steps:"
echo "1. Download Bible translation data (see INSTALLATION.md)"
echo "2. Test the display: python3 bible_display.py"
echo "3. Set up automatic daily updates (see INSTALLATION.md)"
echo ""
echo "Configuration file: config.json"
echo "Log file: bible_display.log"
echo ""
