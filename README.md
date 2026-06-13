# IoT Vehicle Tracking & Theft Prevention System

## Overview

GPS-based vehicle monitoring and theft prevention system using Python simulation and Streamlit dashboard.

## Features

- Vehicle tracking
- GPS simulation
- Google Maps integration
- Geofence monitoring
- Theft detection
- Dashboard visualization
- CSV logging
- PDF reporting

## Tech Stack

- Python
- Pandas
- Streamlit
- Folium
- Geopy
- ReportLab

## Folder Structure

IoT-Vehicle-Tracking-Theft-Prevention-System/
│
├── dashboard/
│   └── app.py
│
├── python_simulation/
│   ├── geofence.py
│   ├── logger.py
│   └── theft_detector.py
│
├── data/
│   └── gps_data.csv
│
├── outputs/
│   ├── location_history.csv
│   └── location_report.pdf
│
├── reports/
│   └── report_generator.py
│
├── images/
│   ├── folder_structure.png
│   ├── gps_dataset.png
│   ├── terminal_output.png
│   ├── theft_detection.png
│   ├── dashboard_home.png
│   ├── dashboard_map.png
│   ├── pdf_report.png
│   └── github_repository.png
│
├── docs/
│   ├── architecture.md
│   ├── implementation_steps.md
│   └── interview_questions.md
│
├── circuit_diagram/
│   └── vehicle_tracking_circuit.png
│
├── README.md
├── requirements.txt
├── main.py
├── .gitignore
└── LICENSE

## Setup

pip install -r requirements.txt

## Run

python main.py

streamlit run dashboard/app.py

## Future Improvements

- ESP32 integration
- MQTT communication
- Blynk dashboard
- SMS alerts
- AI anomaly detection
