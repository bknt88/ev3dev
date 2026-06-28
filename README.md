# EV3 PDA

Modular, Object-Oriented (OOP) applications built on **Pybricks MicroPython (v2.0)** for the LEGO Mindstorms EV3. This project turns the EV3 brick into an intelligent personal digital assistance. It fetches real-time public data via internet, renders clean ASCII weather art, stock info using standard monospace typography, and vocalizes meteorological summaries.

---

## Applications
1. **speaker.py** A speaker test to quickly check the basic sanity of the env
2. **weather_report.py** Realtime weather on major cities
3. **mp3_player.py** To be released, a simple mp3 player that put some music on the box

---

## Hardware Setup & Prerequisites

1.  **LEGO Mindstorms EV3 Brick** running `ev3dev` Debian Linux.
2.  **Internet Connection**: Enabled via USB Network Tethering (RNDIS) or a compatible USB Wi-Fi dongle.
3.  **Local Development Machine**: Configured with `rsync` for rapid transmission.

## Disabling the software interrupt
The default sample rate is 100Hz on the sensors, which is not neccessary when we don't have high speed sensors.
Before lowering the sample rate using the script, we must change the script's permission since writing linux sys files needs sudo.
Run this command from your computer terminal over SSH (where you can type the password) to open the safe sudo editor:
sudo visudo
Scroll all the way to the very bottom of the file using your arrow keys, and add this exact line on its own new line:
robot ALL=(ALL) NOPASSWD: /usr/bin/tee /sys/bus/iio/devices/trigger0/sampling_frequency
If visudo opened in nano: Press Ctrl + O, Enter, then Ctrl + X.
If visudo opened in vi/vim: Type :wq and press Enter.

## 🛠️ Deployment Workflow (The Geek Pipeline)

This repository is optimized for a modern **"Write Locally ➔ Deploy Instantly via rsync ➔ Execute Remotely"** pipeline. 

### 1. Synchronize Code to EV3
Run this command from your host machine's terminal to sync code updates in milliseconds without resetting connections:
```bash
rsync -avz --progress ev3dev/ robot@<YOUR_EV3_IP>:/home/robot/ev3dev/
```

### 2. Run the Programs
Taking the weather_report.py as an example. After boot up, in the file browser, find and run the weather_report.py or 
SSH into your EV3 brick and trigger execution inside the full-privilege display/audio wrapper:
```bash
brickrun src/weather_report.py
```

---

## Core API Implementation Specs

### Weather report
Fetches verbal descriptors directly from cloud endpoints to bypass string tokenization bottlenecks:
```bash
http://wttr.in/{City}?format=%C,+%t,+humidity+%h,+wind+%w
```
*Vocalized Output:* `"In Stockholm, the condition is Clear, and the temperature is +18C, humidity 65%, wind 11km/h."`
Fetches a lightweight, current-condition-only terminal panel stripped of ANSI escape codes (`&T` parameter) to fit inside the EV3 LCD boundaries cleanly:
```bash
http://wttr.in/{City}?0&T
```

---

## 📜 License
This project is open-source and available under the MIT License.
