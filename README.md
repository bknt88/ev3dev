# EV3 IoT Weather Report System

A modular, Object-Oriented (OOP) IoT application built on **Pybricks MicroPython (v2.0)** for the LEGO Mindstorms EV3. This project turns the EV3 brick into an intelligent weather forecasting agent. It fetches real-time public weather matrices via terminal pipes, renders clean ASCII weather art using standard monospace typography, and vocalizes meteorological summaries.

---

## 💎 Core Architectural Features

*   **Modular OOP Design**: Features strict decoupling of business modules. UI rendering (`TextMenu`) and backend API operations (`WeatherFetcher`) live in separate self-contained custom libraries.
*   **Dual-API Data Polymorphism**: A single user selection triggers concurrent target data streams: an ASCII diagram cropped exclusively for physical screen output, and a text-based format containing conditions, temperature, humidity, and wind speed optimized for vocal performance.
*   **Monospace ASCII Alignment**: Overrides the standard Lucida proportional font with Linux-native `Courier` point-matrices to guarantee pixel-perfect symmetry for terminal weather art.
*   **Fail-Safe Interceptions**: Outage isolation protocols catch network drops or API server timeouts, redirecting output gracefully to dynamic localized error strings.

---

## 🕹️ Hardware Setup & Prerequisites

1.  **LEGO Mindstorms EV3 Brick** running `ev3dev` Debian Linux.
2.  **Internet Connection**: Enabled via USB Network Tethering (RNDIS) or a compatible USB Wi-Fi dongle.
3.  **Local Development Machine**: Configured with `rsync` for rapid transmission.


## 🛠️ Deployment Workflow (The Geek Pipeline)

This repository is optimized for a modern **"Write Locally ➔ Deploy Instantly via rsync ➔ Execute Remotely"** pipeline. 

### 1. Synchronize Code to EV3
Run this command from your host machine's terminal to sync code updates in milliseconds without resetting connections:
```bash
rsync -avz --progress ev3dev/ robot@<YOUR_EV3_IP>:/home/robot/ev3dev/
```

### 2. Run the Program
After boot up, in the file browser, find and run the weather_report.py or 
SSH into your EV3 brick and trigger execution inside the full-privilege display/audio wrapper:
```bash
brickrun src/weather_report.py
```

---

## ⚙️ Core API Implementation Specs

### Speech Serialization Format
Fetches verbal descriptors directly from cloud endpoints to bypass string tokenization bottlenecks:
```bash
http://wttr.in/{City}?format=%C,+%t,+humidity+%h,+wind+%w
```
*Vocalized Output:* `"In Stockholm, the condition is Clear, and the temperature is +18C, humidity 65%, wind 11km/h."`

### Screen ASCII Map Format
Fetches a lightweight, current-condition-only terminal panel stripped of ANSI escape codes (`&T` parameter) to fit inside the EV3 LCD boundaries cleanly:
```bash
http://wttr.in/{City}?0&T
```

---

## 📜 License
This project is open-source and available under the MIT License.
