import pandas as pd
from python_simulation.geofence import check_geofence

data = pd.read_csv("data/gps_data.csv")

for _, row in data.iterrows():

    theft, distance = check_geofence(
        row["latitude"],
        row["longitude"]
    )

    if theft:
        status = "THEFT ALERT"
    else:
        status = "SAFE"

    print(
        row["timestamp"],
        status,
        round(distance,2)
    )