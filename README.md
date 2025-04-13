# 🚤 Mini WAM-V Catamaran ASV (Raspberry Pi Edition)

This is a personal project I built to experiment with autonomous marine robotics. It’s a small twin-hull catamaran, inspired by the WAM-V (Wave Adaptive Modular Vessel) design. The boat is powered by a Raspberry Pi and features live motor control and GPS logging. Eventually, I’d like to expand it to support full autonomy and obstacle avoidance.

---

## ✨ Project Goals

- Build a stable, WAM-V-style catamaran using simple materials
- Learn more about GPIO motor control and GPS integration with Raspberry Pi
- Simulate real-world marine robotics challenges like station keeping, wave resistance, and remote navigation

---

## 🔧 Features

- Twin-hull (catamaran) layout for added stability
- Differential drive control using Python
- GPS module for location tracking and data logging
- Modular wiring and code (easy to expand or tweak)
- Works outdoors in real water (pool/lake tested)

---

## 🧠 Skills Practiced

- GPIO-based DC motor control (L298N + Raspberry Pi)
- Serial communication (GPS via UART)
- Parsing NMEA GPS strings in Python
- Data logging to CSV
- Physical prototyping with marine considerations

---

## 🛒 Parts Used

| Item | Notes |
|------|-------|
| Raspberry Pi | I used a Pi 3B+ but any model with GPIO/UART should work |
| 2x DC motors + propellers | Basic TT motors with gearboxes and plastic props |
| L298N motor driver | Dual H-bridge to control motors |
| NEO-6M GPS module | For real-time GPS readings |
| Pool noodles | Used for the pontoons |
| Small plywood or acrylic sheet | As the main platform |
| IP67 container | Protects Pi and electronics |
| 18650 battery + holder | Power source |
| Breadboard, jumper wires, hot glue, zip ties | Mounting and prototyping materials |

---

## 🛠 Wiring Summary

| Component        | Raspberry Pi GPIO |
|-----------------|-------------------|
| Left motor      | GPIO 17 & 18      |
| Right motor     | GPIO 22 & 23      |
| GPS TX → Pi RX  | GPIO 15 (UART RX) |
| GPS RX → Pi TX  | GPIO 14 (UART TX) |
| GPS VCC & GND   | 3.3V or 5V, Ground |
| L298N ENA/ENB   | Connected to 5V   |

You’ll need to enable UART using `sudo raspi-config` → Interface Options → Serial Port.

---

## 🐍 Code: `boat.py`

Basic version: moves forward for 30 seconds while logging GPS data to a CSV file.

```python
from gpiozero import Motor
import serial
import time
import csv

left_motor = Motor(forward=17, backward=18)
right_motor = Motor(forward=22, backward=23)
gps_serial = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

with open('gps_log.csv', 'w', newline='') as csvfile:
    log = csv.writer(csvfile)
    log.writerow(["Time", "Latitude", "Longitude"])

    def parse_gpgga(sentence):
        parts = sentence.split(",")
        if len(parts) > 5 and parts[2] and parts[4]:
            lat = float(parts[2])/100.0
            lon = float(parts[4])/100.0
            return (lat, lon)
        return (None, None)

    try:
        print("Running motors + logging GPS...")
        start_time = time.time()
        left_motor.forward()
        right_motor.forward()

        while time.time() - start_time < 30:
            line = gps_serial.readline().decode('utf-8', errors='ignore')
            if "$GPGGA" in line:
                lat, lon = parse_gpgga(line)
                if lat and lon:
                    print(f"GPS: {lat}, {lon}")
                    log.writerow([time.strftime("%H:%M:%S"), lat, lon])

        left_motor.stop()
        right_motor.stop()
        print("Done.")

    except KeyboardInterrupt:
        left_motor.stop()
        right_motor.stop()
        print("Stopped manually.")
