
import csv
import random
from datetime import datetime, timedelta

# Generate the same sample data each time
random.seed(42)

filename = "energy_readings.csv"

# Dataset settings
start_time = datetime(2026, 10, 1, 0, 0)
number_of_days = 7
interval_minutes = 15

# Calculate the number of readings
total_readings = number_of_days * 24 * 60 // interval_minutes

# Create and write the CSV file
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Column headings
    writer.writerow([
        "timestamp",
        "solar_output_kw",
        "grid_usage_kw",
        "temperature_c"
    ])

    # Generate each reading
    for i in range(total_readings):
        timestamp = start_time + timedelta(
            minutes=i * interval_minutes
        )

        hour = timestamp.hour + timestamp.minute / 60

        # Simulated solar output: higher around noon
        sunlight = max(0, 1 - abs(hour - 12) / 6)
        solar_output = round(
            max(0, random.uniform(15, 45) * sunlight), 2
        )

        # Simulated grid power usage
        grid_usage = round(
            random.uniform(20, 60)
            + (15 if 8 <= hour <= 18 else 0), 2
        )

        # Simulated temperature
        temperature = round(
            25 + 7 * max(0, 1 - abs(hour - 14) / 8)
            + random.uniform(-1.5, 1.5), 2
        )

        # Save the reading as one CSV row
        writer.writerow([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            solar_output,
            grid_usage,
            temperature
        ])

print(f"Dataset created: {filename}")
print(f"Total readings: {total_readings}")
print(f"Days covered: {number_of_days}")
print(f"Interval: {interval_minutes} minutes")
