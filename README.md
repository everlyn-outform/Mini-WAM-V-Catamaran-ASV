# 🚤 Mini WAM-V Catamaran ASV (Raspberry Pi Edition)

A small-scale autonomous catamaran inspired by WAM-V designs. This version is powered by a Raspberry Pi and integrates motor control, GPS logging, IMU orientation tracking, and ultrasonic obstacle detection. It also supports exporting real-world logs to **ASVLite**, a lightweight marine simulation framework, to visualize and debug missions.

---

## ✨ Project Goals

- Build a stable, dual-hull robot boat that behaves like a WAM-V
- Integrate real-time sensor data from GPS, IMU, and ultrasonic rangefinder
- Visualize and simulate boat behavior in waves using [ASVLite](https://github.com/resilient-swarms/ASVLite)
- Practice end-to-end workflow: simulate → test → deploy → analyze

---

## 🔧 Core Features

- Differential DC motor control via Raspberry Pi
- Real-time GPS logging (NEO-6M)
- Roll/pitch/acceleration via IMU (MPU6050)
- Obstacle detection with waterproof ultrasonic (JSN-SR04T)
- Logs all data into timestamped CSV
- Optional: Convert log to ASVLite sim input for visualization

---

## 🧠 Skills Practiced

- Raspberry Pi GPIO control + UART serial
- Sensor fusion prep (GPS + IMU)
- Real-world robotics stability testing
- Log-based simulation + analysis (digital twin concept)
- Embedded Python scripting for autonomy

---

## 🛒 Parts Used

| Item | Notes |
|------|-------|
| Raspberry Pi 3B+ | Any Pi with GPIO/UART works |
| 2x DC motors + props | Differential drive |
| L298N motor driver | For bi-directional motor control |
| NEO-6M GPS | For live coordinates |
| MPU6050 IMU | Detects roll, pitch, motion |
| JSN-SR04T waterproof ultrasonic | For forward obstacle detection |
| Pool noodles (or bottles) | For hulls |
| Plywood/plastic sheet | Platform base |
| Waterproof box | Protects Pi and wiring |
| 18650 battery pack | Power supply |
| Breadboard + jumpers, zip ties | Mounting + wiring

---

## 🔗 My Part Links (To Track What I Bought)

| Item | Links |
|------|-------|
| Raspberry Pi 3B+ | [paste link] |
| 2x DC motors + props | [paste link] |
| L298N motor driver | [paste link] |
| NEO-6M GPS | [paste link] |
| MPU6050 IMU | [paste link] |
| JSN-SR04T waterproof ultrasonic | [paste link] |
| Pool noodles | Dollar Store |
| Plywood/plastic sheet | [paste link] |
| Waterproof box | [paste link] |
| 18650 battery pack | [paste link] |
| Breadboard + jumpers, zip ties | Already have
