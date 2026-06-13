from geopy.distance import geodesic

SAFE_LOCATION = (18.5204, 73.8567)
SAFE_RADIUS = 200

def detect_theft(lat, lon):

    distance = geodesic(
        SAFE_LOCATION,
        (lat, lon)
    ).meters

    if distance > SAFE_RADIUS:
        return "THEFT ALERT"

    return "SAFE"