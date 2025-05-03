import requests

API_KEY = "5edfcff0-94a7-4c66-bbc0-f743141f39c6"


def get_coordinates(address):
    geocoder_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }

    try:
        response = requests.get(geocoder_url, params=params)
        response.raise_for_status()

        data = response.json()
        toponym = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        lon, lat = toponym["Point"]["pos"].split()
        return lat, lon
    except Exception:
        return None, None


def get_ll_span(address):
    geocoder_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json"
    }

    try:
        response = requests.get(geocoder_url, params=params)
        response.raise_for_status()

        data = response.json()
        toponym = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

        # Координаты центра
        lon, lat = toponym["Point"]["pos"].split()

        # Размеры объекта
        envelope = toponym["boundedBy"]["Envelope"]
        lower = list(map(float, envelope["lowerCorner"].split()))
        upper = list(map(float, envelope["upperCorner"].split()))
        delta_lon = str(abs(upper[0] - lower[0]))
        delta_lat = str(abs(upper[1] - lower[1]))

        return f"{lon},{lat}", f"{delta_lon},{delta_lat}"
    except Exception:
        return None, None
