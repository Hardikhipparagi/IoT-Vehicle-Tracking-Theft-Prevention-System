import pandas as pd

data = pd.read_csv("data/gps_data.csv")

for _, row in data.iterrows():

    lat = row["latitude"]
    lon = row["longitude"]

    maps_url = f"https://www.google.com/maps?q={lat},{lon}"

    print("\nVehicle Position")
    print("Latitude:", lat)
    print("Longitude:", lon)
    print("Speed:", row["speed"])
    print("Google Maps:", maps_url)