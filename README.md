
# 🚤 Mini WAM-V Catamaran ASV

A small-scale, twin-hull autonomous boat inspired by the WAM-V (Wave Adaptive Modular Vessel) used in marine robotics. This project mimics its stable catamaran architecture and introduces basic motor control with optional GPS-based navigation. Perfect for learning about marine robotics and showing off autonomous skills!

---

## ✨ Features

- Twin-hull (catamaran) design for stability in water
- Differential motor control (tank-style)
- Optional GPS + compass for autonomous waypoint navigation
- Shock-absorbing center platform (like real WAM-V suspension)
- Modular code for Arduino or Raspberry Pi

---

## 🧠 Skills Demonstrated

- Robotics prototyping & architecture
- Embedded programming (Arduino/Pi)
- GPS + IMU integration
- DC motor control & PWM
- Real-world mechanical design + testing

---

## 📦 Materials To Buy

| Item | Description |
|------|-------------|
| 2x Floatation Hulls | Pool noodles or sealed plastic bottles |
| Arduino Uno OR Raspberry Pi | Microcontroller for logic |
| 2x DC Motors + Props | TT Motors with props or water thrusters |
| 2x L298N Motor Driver | To control motor speed/direction |
| Waterproof Box | Electronics housing (IP67) |
| NEO-6M GPS Module *(optional)* | GPS navigation |
| MPU6050 IMU *(optional)* | Orientation sensing |
| Battery Pack | 18650 or LiPo battery with holder |
| Breadboard + Wires | For prototyping |
| Mounting Materials | Screws, zip ties, hot glue, etc. |
| Frame Platform | Light plywood or acrylic sheet |

---

## 🛠️ Wiring Diagram (Basic Arduino Setup)

- Left Motor → L298N → Arduino Pins 7/8
- Right Motor → L298N → Arduino Pins 4/5
- ENA/ENB to PWM pins (9 and 3)
- GPS TX → Arduino RX (D2), GPS RX → Arduino TX (D3)
- IMU SDA/SCL → A4/A5
- Battery Pack powers both motor driver and Arduino

---

## 💻 Sample Arduino Code

```cpp
#define ENA 9
#define IN1 8
#define IN2 7
#define ENB 3
#define IN3 5
#define IN4 4

void setup() {
  pinMode(ENA, OUTPUT); pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT); pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT);
}

void loop() {
  // Forward
  analogWrite(ENA, 200); digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  analogWrite(ENB, 200); digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
  delay(2000);

  // Stop
  analogWrite(ENA, 0); analogWrite(ENB, 0);
  delay(1000);
}
