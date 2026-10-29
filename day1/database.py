
import sqlite3

# Connect to the database.
# If it doesn't exist, SQLite creates it.
connection = sqlite3.connect("campus_energy.db")

# Create a cursor to execute SQL commands.
cursor = connection.cursor()

# Create the table if it doesn't already exist.
cursor.execute("""
CREATE TABLE IF NOT EXISTS energy_readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    solar_output_kw REAL NOT NULL,
    grid_usage_kw REAL NOT NULL,
    temperature_c REAL NOT NULL
)
""")

# Save the database changes.
connection.commit()

# Close the connection.
connection.close()

print("Database created successfully!")
print("Table created: energy_readings")
