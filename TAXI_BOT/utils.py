import requests
import math
import db
import random
import string


def geocode(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{address}, Toshkent, Uzbekistan",
        "format": "json",
        "limit": 1,
        "accept-language": "ru"
    }
    headers = {"User-Agent": "TaxiBot/1.0"}
    r = requests.get(url, params=params, headers=headers).json()
    if r:
        return {
            "lat": float(r[0]["lat"]),
            "lon": float(r[0]["lon"]),
            "address": r[0]["display_name"]
        }
    return None


def get_distance(from_lat, from_lon, to_lat, to_lon):
    R = 6371
    d_lat = math.radians(to_lat - from_lat)
    d_lon = math.radians(to_lon - from_lon)
    a = (math.sin(d_lat / 2) ** 2 +
         math.cos(math.radians(from_lat)) *
         math.cos(math.radians(to_lat)) *
         math.sin(d_lon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    km = round(R * c * 1.3, 1)
    minutes = round(km * 2.5)
    return {"km": km, "minutes": minutes}


def calculate_price(tariff_key, distance_km):
    tariff = db.get_tariffs_by_key(tariff_key)
    # id, key, name_uz, name_ru, name_en, desc_uz, desc_ru, desc_en, base_price, per_km, is_active
    total = tariff[8] + tariff[9] * distance_km
    return int(total)


def reverse_geocode(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json",
        "accept-language": "uz"
    }
    headers = {"User-Agent": "TaxiBot/1.0"}
    r = requests.get(url, params=params, headers=headers).json()

    if "display_name" in r:
        address = r.get("address", {})
        road = address.get("road", "")
        suburb = address.get("suburb", "")
        city = address.get("city", "Toshkent")

        if road:
            return f"{road}, {suburb}" if suburb else road
        elif suburb:
            return suburb
        else:
            return r["display_name"].split(",")[0]
    return f"{lat}, {lon}"

def generate_login(name:str) -> str:
    base = name.lower().replace(" ", "_")
    suffix = random.randint(100, 999)
    return f"{base}_{suffix}"
def generate_password(length=8) -> str:
    chars = string.ascii_letters + string.digits
    return  ''.join(random.choices(chars, k=length))

import math

def haversine(lat1, lon1, lat2, lon2):
    r = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return r * c