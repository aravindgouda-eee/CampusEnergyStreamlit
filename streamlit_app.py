
import httpx
import pandas as pd
import plotly.express as px
import streamlit as st

API_BASE = "https://campusenergymonitoring.fastapicloud.dev"

st.set_page_config(
    page_title="Campus Energy Monitoring",
    page_icon="⚡",
    layout="wide",
)

st.title("⚡ Campus Energy Monitoring System")
st.caption("MGIT ACTORYX IITH | Energy Analytics Dashboard")

@st.cache_data(ttl=60)
def fetch_json(endpoint, params=None):
    response = httpx.get(
        f"{API_BASE}{endpoint}",
        params=params,
        timeout=20,
    )
    response.raise_for_status()
    return response.json()

def to_dataframe(payload):
    # Support either a JSON list or an object containing a list.
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict):
        records = next(
            (
                value for value in payload.values()
                if isinstance(value, list)
            ),
            [],
        )
    else:
        records = []

    return pd.DataFrame(records)

try:
    readings = to_dataframe(
        fetch_json("/readings", {"limit": 672})
    )
    daily = to_dataframe(fetch_json("/summary/daily"))

except Exception as exc:
    st.error("Unable to connect to the FastAPI backend.")
    st.caption(f"Check the API URL and server status. Details: {exc}")
    st.stop()

required = [
    "timestamp",
    "solar_output_kw",
    "grid_usage_kw",
    "temperature_c",
]

missing = [column for column in required if column not in readings.columns]

if readings.empty or missing:
    st.error(
        "The API returned no readings or an unexpected response format."
    )
    if missing:
        st.write("Missing fields:", missing)
    st.stop()

readings["timestamp"] = pd.to_datetime(
    readings["timestamp"], errors="coerce"
)

for column in [
    "solar_output_kw",
    "grid_usage_kw",
    "temperature_c",
]:
    readings[column] = pd.to_numeric(
        readings[column], errors="coerce"
    )

readings = readings.dropna(
    subset=["timestamp", "solar_output_kw",
            "grid_usage_kw", "temperature_c"]
).sort_values("timestamp")

if readings.empty:
    st.warning("No valid energy readings are available.")
    st.stop()

# Sidebar filters
st.sidebar.header("Dashboard Controls")

min_date = readings["timestamp"].min().date()
max_date = readings["timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = readings[
        readings["timestamp"].dt.date.between(start_date, end_date)
    ]
else:
    filtered = readings[
        readings["timestamp"].dt.date == date_range
    ]

st.sidebar.caption(f"API: {API_BASE}")
if st.sidebar.button("Refresh data"):
    st.cache_data.clear()
    st.rerun()

if filtered.empty:
    st.warning("No readings exist for the selected date range.")
    st.stop()

# Summary metrics
solar_avg = filtered["solar_output_kw"].mean()
grid_avg = filtered["grid_usage_kw"].mean()
temp_avg = filtered["temperature_c"].mean()
solar_peak = filtered["solar_output_kw"].max()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Average Solar Output", f"{solar_avg:.2f} kW")
c2.metric("Average Grid Usage", f"{grid_avg:.2f} kW")
c3.metric("Average Temperature", f"{temp_avg:.2f} °C")
c4.metric("Peak Solar Output", f"{solar_peak:.2f} kW")

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("Solar and Grid Power")
    power_chart = px.line(
        filtered,
        x="timestamp",
        y=["solar_output_kw", "grid_usage_kw"],
        labels={
            "timestamp": "Time",
            "value": "Power (kW)",
            "variable": "Measurement",
        },
        title="Power Trends",
    )
    st.plotly_chart(power_chart, use_container_width=True)

with right:
    st.subheader("Temperature Trend")
    temp_chart = px.line(
        filtered,
        x="timestamp",
        y="temperature_c",
        labels={
            "timestamp": "Time",
            "temperature_c": "Temperature (°C)",
        },
        title="Temperature Over Time",
    )
    st.plotly_chart(temp_chart, use_container_width=True)

# Daily summary
if not daily.empty:
    st.subheader("Daily Energy Summary")
    st.dataframe(daily, use_container_width=True, hide_index=True)

# Recent readings
st.subheader("Energy Readings")
st.caption(f"{len(filtered)} readings in the selected period")

st.dataframe(
    filtered.sort_values("timestamp", ascending=False),
    use_container_width=True,
    hide_index=True,
)

st.caption(
    "Data source: Campus Energy Monitoring FastAPI. "
    "These are sample/simulated readings, not verified live campus sensor data."
)
