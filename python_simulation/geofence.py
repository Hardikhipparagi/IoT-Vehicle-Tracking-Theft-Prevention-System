from geopy.distance import geodesic

SAFE_LOCATION = (18.5204, 73.8567)

SAFE_RADIUS = 200

def check_geofence(lat, lon):

    current = (lat, lon)

    distance = geodesic(
        SAFE_LOCATION,
        current
    ).meters

    if distance > SAFE_RADIUS:
        return True, distance

    return False, distance