
import sqlite3
from fastapi import FastAPI, HTTPException
from pathlib import Path
from fastapi.responses import FileResponse

app = FastAPI(
    title="Campus Energy Monitoring API",
    description="API for campus energy readings",
    version="1.0.0"
)

DATABASE = Path(__file__).parent / "campus_energy.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


@app.get("/")
def home():
    return {
        "message": "Campus Energy Monitoring API is running!"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/readings")
def get_readings(limit: int = 10):
    if limit < 1 or limit > 672:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 672"
        )

    connection = get_connection()

    try:
        rows = connection.execute(
            """
            SELECT id, timestamp, solar_output_kw,
                   grid_usage_kw, temperature_c
            FROM energy_readings
            ORDER BY timestamp
            LIMIT ?
            """,
            (limit,)
        ).fetchall()

        return {
            "count": len(rows),
            "readings": [dict(row) for row in rows]
        }
    finally:
        connection.close()

@app.get("/summary/daily")
def daily_summary():
    connection = get_connection()

    try:
        rows = connection.execute(
            """
            SELECT
                substr(timestamp, 1, 10) AS date,
                COUNT(*) AS readings_count,
                ROUND(MAX(temperature_c), 2) AS max_temperature_c,
                ROUND(MIN(temperature_c), 2) AS min_temperature_c,
                ROUND(AVG(temperature_c), 2) AS avg_temperature_c,
                ROUND(AVG(solar_output_kw), 2) AS avg_solar_power_kw,
                ROUND(AVG(grid_usage_kw), 2) AS avg_grid_power_kw
            FROM energy_readings
            GROUP BY substr(timestamp, 1, 10)
            ORDER BY date
            """
        ).fetchall()

        return {
            "days": len(rows),
            "daily_summary": [dict(row) for row in rows]
        }
    finally:
        connection.close()
@app.get("/dashboard", include_in_schema=False)
def dashboard():
    html_file = Path(__file__).parent / "static" / "dashboard.html"
    return FileResponse(html_file)
