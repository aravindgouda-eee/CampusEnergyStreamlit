
import csv
import sqlite3

# Connect to the database we created
connection = sqlite3.connect("campus_energy.db")
cursor = connection.cursor()

# Read the CSV dataset
with open("energy_readings.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute(
            """
            INSERT INTO energy_readings (
                timestamp,
                solar_output_kw,
                grid_usage_kw,
                temperature_c
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                row["timestamp"],
                float(row["solar_output_kw"]),
                float(row["grid_usage_kw"]),
                float(row["temperature_c"])
            )
        )

# Save all inserted readings
connection.commit()
connection.close()

print("CSV data imported successfully!")
