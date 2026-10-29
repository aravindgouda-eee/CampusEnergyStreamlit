# ⚡ Campus Energy Monitoring System

A web-based energy analytics dashboard built with **Python, Streamlit, FastAPI, and SQLite** to visualize campus energy readings, monitor solar generation and grid consumption, and analyze temperature trends.

## 🌐 Live Demo

- **Live Dashboard:** https://campusenergyapp-fdacxobjfoxf2egqlrqlax.streamlit.app
- **FastAPI Backend:** https://campusenergymonitoring.fastapicloud.dev
- **API Documentation:** https://campusenergymonitoring.fastapicloud.dev/docs
- **GitHub Repository:** https://github.com/aravindgouda-eee/CampusEnergyStreamlit

## 📌 Project Overview

The Campus Energy Monitoring System provides a dashboard for exploring campus energy data through interactive visualizations and summary metrics. The Streamlit frontend retrieves readings from the deployed FastAPI backend and presents them in an accessible web interface.

The current implementation uses simulated sample readings for demonstration. It is not yet connected to live campus energy meters or physical sensors.

## ✨ Key Features

- **Energy Summary:** Displays average solar output, average grid usage, average temperature, and peak solar output.
- **Power Trend Analysis:** Visualizes solar generation and grid consumption over time.
- **Temperature Monitoring:** Displays temperature variations across the selected period.
- **Date Range Filtering:** Filters readings to examine a chosen time period.
- **Daily Energy Summary:** Presents daily aggregated energy data.
- **Energy Readings Table:** Displays individual timestamped readings.
- **API Integration:** Retrieves data from the deployed FastAPI backend.
- **Refresh Controls:** Allows users to request refreshed dashboard data.
- **Cloud Deployment:** Makes the dashboard accessible through a public URL.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming |
| Streamlit | Interactive dashboard frontend |
| FastAPI | Backend REST API |
| SQLite | Database for energy readings |
| Pandas | Data processing and tabular presentation |
| Plotly | Interactive charts |
| HTTPX | HTTP requests to the backend |
| GitHub | Source code management |
| Streamlit Community Cloud | Frontend hosting |
| FastAPI Cloud | Backend hosting |

## 🏗️ System Architecture

```text
Simulated Energy Readings
          |
          v
     SQLite Database
          |
          v
      FastAPI Backend
          |
          | HTTP API requests
          v
    Streamlit Dashboard
          |
          v
 Summary Metrics, Charts,
 Daily Summary and Readings
```

The dashboard communicates with the backend through HTTP requests. The backend provides the readings and daily summaries used by the frontend.

## 📊 Dashboard Metrics

The dashboard includes:

- Average Solar Output (kW)
- Average Grid Usage (kW)
- Average Temperature (°C)
- Peak Solar Output (kW)
- Solar and Grid Power Trends
- Temperature Trends
- Daily Energy Summary
- Timestamped Energy Readings

Metric values depend on the selected date range and the data returned by the backend.

## 🚀 Run the Dashboard Locally

### Prerequisites

- Python 3.10 or a compatible Python version
- Git (optional, if cloning the repository)
- Internet access to reach the deployed FastAPI backend

### 1. Clone the repository

```bash
git clone https://github.com/aravindgouda-eee/CampusEnergyStreamlit.git
cd CampusEnergyStreamlit
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

The application will provide a local URL, typically:

`http://localhost:8501`

The dashboard uses the configured FastAPI backend URL to retrieve its data.

## 🔌 Backend API

The deployed backend provides these endpoints:

| Endpoint | Purpose |
|---|---|
| `/` | Backend home endpoint |
| `/health` | Health check |
| `/readings` | Retrieve energy readings |
| `/summary/daily` | Retrieve daily energy summaries |
| `/dashboard` | Existing HTML dashboard |
| `/docs` | Interactive API documentation |

**Backend URL:** https://campusenergymonitoring.fastapicloud.dev

## 🧪 Testing and Validation

The application can be tested by:

1. Opening the live dashboard.
2. Checking that summary metrics load.
3. Changing the date range.
4. Inspecting the power and temperature charts.
5. Reviewing the daily summary and individual readings.
6. Using the refresh control.
7. Checking the backend endpoints and API documentation.

## 🔒 Data and Limitations

- The current readings are simulated sample data.
- Live sensor integration has not yet been implemented.
- Dashboard data availability depends on the deployed backend.
- Actual campus energy monitoring will require validated meter or sensor inputs and suitable data acquisition hardware.

## 🔮 Future Enhancements

- Integration with real energy meters and IoT sensors.
- Automated data collection and scheduled updates.
- Energy consumption forecasting.
- Abnormal consumption and peak-demand alerts.
- Role-based access and authentication.
- Historical comparisons and downloadable reports.
- Improved database indexing and audit logging.

## 🎯 Project Objective

To develop a web-based campus energy analytics application that demonstrates database-backed data management, REST API integration, interactive visualization, and cloud deployment.

---

**Project:** Campus Energy Monitoring System  
**Frontend:** Streamlit  
**Backend:** FastAPI  
**Database:** SQLite  
**Data Source:** Simulated sample readings for demonstration
