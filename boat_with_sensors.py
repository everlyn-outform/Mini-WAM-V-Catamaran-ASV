# boat_with_sensors.py
import time
import csv
import serial
import smbus
import RPi.GPIO as GPIO
from gpiozero import Motor
from datetime import datetime

# === GPIO Setup ===
GPIO.setmode(GPIO.BCM)
TRIG = 5
ECHO = 6
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# === Motor Setup ===
left_motor = Motor(forward=17, backward=18)
right_motor = Motor(forward=22, backward=23)

# === GPS Setup ===
gps = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

# === IMU Setup (MPU6050) ===
bus = smbus.SMBus(1)
MPU6050_ADDR = 0x68
bus.write_byte_data(MPU6050_ADDR, 0x6B, 0)

def read_imu_pitch():
    acc_y = read_word_2c(0x3D)
    acc_z = read_word_2c(0x3F)
    pitch = (acc_y / 16384.0) * 90
    return round(pitch, 2)

def read_word_2c(addr):
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr+1)
    val = (high << 8) + low
    if val >= 0x8000:
        return -((65535 - val) + 1)
    return val

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = (elapsed * 34300) / 2  # cm
    return round(distance, 2)

def parse_gpgga(line):
    try:
        parts = line.split(",")
        if parts[2] and parts[4]:
            lat = float(parts[2]) / 100.0
            lon = float(parts[4]) / 100.0
            return round(lat, 6), round(lon, 6)
    except:
        return None, None
    return None, None

# === Logging ===
log_file = "logs/gps_imu_log.csv"
with open(log_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "Latitude", "Longitude", "Pitch", "Distance_cm"])

    print("[INFO] Starting sensors + motors...")
    left_motor.forward()
    right_motor.forward()

    try:
        for _ in range(30):  # 30 data points, 1 per second
            gps_line = gps.readline().decode("utf-8", errors="ignore")
            lat, lon = parse_gpgga(gps_line) if "$GPGGA" in gps_line else (None, None)
            pitch = read_imu_pitch()
            distance = get_distance()

            timestamp = datetime.now().strftime("%H:%M:%S")

            print(f"[{timestamp}] GPS: {lat}, {lon} | Pitch: {pitch}° | Obstacle: {distance}cm")

            writer.writerow([timestamp, lat, lon, pitch, distance])
            time.sleep(1)

        left_motor.stop()
        right_motor.stop()
        print("[INFO] Done. Motors stopped.")

    except KeyboardInterrupt:
        print("[STOPPED] Keyboard interrupt received.")
        left_motor.stop()
        right_motor.stop()

    finally:
        GPIO.cleanup()
