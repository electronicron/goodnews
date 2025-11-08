# Hourly Bible Verse Updates - Setup Guide

## Overview

This guide explains how to set up your e-paper display to show a **new Bible verse every hour** instead of once per day.

---

## ✅ What Changed

The script now uses both **date AND hour** to select verses:
- Same verse for the entire hour
- Different verse each hour (24 different verses per day)
- Changes automatically at the top of each hour (e.g., 1:00, 2:00, 3:00)

**Example:**
- 1:00 PM - 1:59 PM → John 3:16
- 2:00 PM - 2:59 PM → Psalm 23:1
- 3:00 PM - 3:59 PM → Proverbs 3:5
- etc.

---

## 🚀 Setup: Method 1 - Run Every Hour (Recommended)

This will update your display at the start of every hour.

### Step 1: Edit Crontab

```bash
crontab -e
```

### Step 2: Add This Line

```
0 * * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

**What this means:**
- `0 * * * *` = Run at minute 0 of every hour
- Updates at: 12:00 AM, 1:00 AM, 2:00 AM, ... 11:00 PM

### Step 3: Save and Exit
- Press **Ctrl + O** to save
- Press **Enter** to confirm
- Press **Ctrl + X** to exit

---

## ⚡ Setup: Method 2 - Run Multiple Times Per Hour

Want updates more frequently? You can update every 30 minutes, 15 minutes, etc.

### Every 30 Minutes
```
0,30 * * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

Updates at: 1:00, 1:30, 2:00, 2:30, 3:00, 3:30...

**Note:** The verse will still only change every hour (at :00), but the display will refresh every 30 minutes to ensure it's always showing.

### Every 15 Minutes
```
*/15 * * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

Updates at: 1:00, 1:15, 1:30, 1:45, 2:00...

### Every 10 Minutes
```
*/10 * * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

---

## 🎯 Cron Schedule Examples

| Schedule | Cron Expression | When It Runs |
|----------|----------------|--------------|
| Every hour | `0 * * * *` | :00 of each hour |
| Every 30 min | `0,30 * * * *` | :00 and :30 |
| Every 15 min | `*/15 * * * *` | :00, :15, :30, :45 |
| Every 10 min | `*/10 * * * *` | Every 10 minutes |
| Every 5 min | `*/5 * * * *` | Every 5 minutes |
| Twice daily | `0 6,18 * * *` | 6 AM and 6 PM |

---

## 🔧 Using Systemd Timer (Advanced)

For more control, use systemd instead of cron:

### Step 1: Edit the Timer File

```bash
sudo nano /etc/systemd/system/bible-display.timer
```

### Step 2: Change to Hourly

Replace the `OnCalendar` line with:

```ini
[Unit]
Description=Hourly Bible Verse Display Timer
Requires=bible-display.service

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
```

### Step 3: Reload and Restart

```bash
sudo systemctl daemon-reload
sudo systemctl restart bible-display.timer
sudo systemctl status bible-display.timer
```

---

## 🧪 Test Your Setup

### Test Manually First
```bash
python3 bible_display.py
```

Check the log to see what verse was selected:
```bash
tail bible_display.log
```

### Check Your Cron Job
```bash
crontab -l
```

You should see your hourly update line.

### Verify Cron is Running
```bash
sudo systemctl status cron
```

Should show "active (running)"

### Watch the Log in Real-Time
```bash
tail -f bible_display.log
```

Wait for the next hour to see if it updates automatically!

---

## 🕐 How the Hourly System Works

### The Seed Formula

The script uses this seed: `YYYYMMDDHH`

**Examples:**
- November 7, 2025 at 2 PM → `2025110714`
- November 7, 2025 at 3 PM → `2025110715`
- November 8, 2025 at 2 PM → `2025110814`

Each unique seed generates a different random verse!

### Consistency
- Same hour = same verse (even if you run the script multiple times)
- Different hour = different verse
- Same hour tomorrow = different verse (because the date changed)

---

## 📊 Display Update Frequency vs Battery Life

| Update Frequency | E-paper Writes/Day | Battery Impact | Recommended For |
|-----------------|-------------------|----------------|-----------------|
| Every hour | 24 | Low | ✅ Recommended |
| Every 30 min | 48 | Medium | Good |
| Every 15 min | 96 | Medium-High | Acceptable |
| Every 10 min | 144 | High | Use with power |
| Every 5 min | 288 | Very High | Requires power |

**Note:** E-paper displays are very power-efficient, but frequent updates will use more power. For battery operation, hourly updates are ideal.

---

## 💡 Pro Tips

### 1. Sync to the Top of the Hour

To ensure updates happen exactly at :00:

```bash
0 * * * * sleep $((RANDOM \% 10)); /usr/bin/python3 /home/pi/bible_display.py
```

The sleep adds a small random delay to prevent all devices updating at exactly the same second if you have multiple.

### 2. Quiet Hours (No Updates at Night)

Only update during waking hours (7 AM - 10 PM):

```bash
0 7-22 * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

### 3. More Frequent During Day

Different schedules for day vs night:

```bash
# Every hour from 7 AM to 10 PM
0 7-22 * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1

# Once at midnight (to have something for overnight)
0 0 * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

### 4. Weekday vs Weekend Schedules

Different verses on weekends:

```bash
# Weekdays: Every hour from 7 AM - 6 PM
0 7-18 * * 1-5 /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1

# Weekends: Every 2 hours from 9 AM - 9 PM
0 9-21/2 * * 0,6 /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

---

## 🐛 Troubleshooting

### Cron Job Not Running

**Check cron service:**
```bash
sudo systemctl status cron
```

**View cron logs:**
```bash
grep CRON /var/log/syslog
```

### Updates Not Happening

**Check if cron is running your script:**
```bash
grep bible_display /var/log/syslog
```

**Test manually:**
```bash
python3 bible_display.py
```

**Check for errors:**
```bash
tail -n 50 bible_display.log
```

### Wrong Time Showing

**Check Pi's time:**
```bash
date
```

**If time is wrong, update:**
```bash
sudo timedatectl set-timezone America/Chicago  # Or your timezone
```

**List available timezones:**
```bash
timedatectl list-timezones
```

### Verse Not Changing

**Wait until the top of the next hour!** The verse only changes when the hour changes.

Check what hour the Pi thinks it is:
```bash
date +"%Y-%m-%d %H:%M:%S"
```

---

## 📅 Verify It's Working

### Check Today's Schedule

After setting up, wait for the next hour and check:

```bash
# See recent updates
tail -n 100 bible_display.log

# Count today's updates
grep "$(date +%Y-%m-%d)" bible_display.log | grep "Successfully updated" | wc -l
```

### Monitor Live

```bash
watch -n 60 'tail -n 5 bible_display.log'
```

This refreshes every minute so you can see updates as they happen.

---

## 🎨 Customization Ideas

### Different Verses by Time of Day

You could modify the script to select different types of verses based on time:
- Morning (6-12): Encouraging verses
- Afternoon (12-18): Wisdom verses
- Evening (18-24): Peace/rest verses

Let me know if you want help implementing this!

### Display Multiple Verses

Show 2-3 short verses instead of one longer verse.

### Include Time on Display

Modify the script to show what hour the verse is for.

---

## 📞 Need Help?

Common questions:

**Q: Will 24 updates per day wear out my display?**
A: No! E-paper displays can handle millions of updates. 24/day is nothing.

**Q: Can I update more than once per hour?**
A: Yes, but the verse only changes every hour. You can update every 15 minutes if you want, but it will show the same verse for the full hour.

**Q: Can I make it change every 30 minutes instead?**
A: Yes! I can modify the script to use 30-minute intervals. Let me know!

**Q: What if I want it to update only during certain hours?**
A: Use cron ranges like `0 7-22 * * *` for 7 AM to 10 PM only.

---

## ✅ Quick Reference

**Edit cron:**
```bash
crontab -e
```

**Hourly updates:**
```
0 * * * * /usr/bin/python3 /home/pi/bible_display.py >> /home/pi/bible_display.log 2>&1
```

**Test:**
```bash
python3 bible_display.py
```

**Check logs:**
```bash
tail bible_display.log
```

**Verify cron:**
```bash
crontab -l
```

---

Enjoy your hourly Bible verses! 🙏⏰
