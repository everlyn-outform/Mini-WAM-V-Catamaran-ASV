# generate_asvlite_input.py
import csv
from geopy.distance import geodesic

INPUT_CSV = "logs/gps_imu_log.csv"
OUTPUT_CSV = "logs/asvlite_input.csv"

print(f"[INFO] Reading {INPUT_CSV}...")

with open(INPUT_CSV, "r") as infile, open(OUTPUT_CSV, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(["Time", "X_m", "Y_m", "Pitch_deg", "Obstacle_cm"])

    origin = None
    for row in reader:
        try:
            lat = float(row["Latitude"])
            lon = float(row["Longitude"])
            pitch = float(row["Pitch"])
            obstacle = float(row["Distance_cm"])
            timestamp = row["Time"]

            if origin is None:
                origin = (lat, lon)

            # Compute X/Y offsets from origin in meters
            x = geodesic(origin, (origin[0], lon)).meters
            y = geodesic(origin, (lat, origin[1])).meters

            # Flip sign if needed (depends on direction)
            if lon < origin[1]: x *= -1
            if lat < origin[0]: y *= -1

            writer.writerow([timestamp, round(x, 2), round(y, 2), pitch, obstacle])
        except:
            continue

print(f"[DONE] ASVLite input saved to {OUTPUT_CSV}")
