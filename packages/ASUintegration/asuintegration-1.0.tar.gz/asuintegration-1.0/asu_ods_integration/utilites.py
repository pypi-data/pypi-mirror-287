import math
from abc import ABCMeta, abstractmethod
from typing import Set, Tuple

from model_app.waste.models import WasteSite


class GeoPoint:
    longitude: "float"
    latitude: "float"

    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __bool__(self):
        return self.latitude is not None and self.longitude is not None


def accurate_calculate_distance(point_from: "GeoPoint", point_to: "GeoPoint"):
    """
    Точный расчёт дистанции между двумя географическими координатами.
    Возвращает округлённое расстояние в метрах.
    """

    rad = 6372795  # радиус сферы (Земли)

    # координаты двух точек
    lat1 = point_from.latitude
    long1 = point_from.longitude

    lat2 = point_to.latitude
    long2 = point_to.longitude

    # в радианах
    rad_lat1 = lat1 * math.pi / 180.
    rad_lat2 = lat2 * math.pi / 180.
    rad_long1 = long1 * math.pi / 180.
    rad_long2 = long2 * math.pi / 180.

    # косинусы и синусы широт и разницы долгот
    cos_l1 = math.cos(rad_lat1)
    cos_l2 = math.cos(rad_lat2)
    sin_l1 = math.sin(rad_lat1)
    sin_l2 = math.sin(rad_lat2)
    delta = rad_long2 - rad_long1
    cos_delta = math.cos(delta)
    sin_delta = math.sin(delta)

    # вычисления длины большого круга
    y = math.sqrt(math.pow(cos_l2 * sin_delta, 2) + math.pow(cos_l1 * sin_l2 - sin_l1 * cos_l2 * cos_delta, 2))
    x = sin_l1 * sin_l2 + cos_l1 * cos_l2 * cos_delta
    ad = math.atan2(y, x)
    dist = ad * rad
    dist = round(dist)
    return dist


def geo_distance_to_meters(degree: "float", latitude: "int" = 0) -> int:
    """
    Упрощённое преобразование расстояния в расстояние в двумерной системе координат,
    для коротких дистанций с потерей точности
    """
    degree_in_meters = get_distance_of_degree_latitude(latitude)
    meters_distance = degree * degree_in_meters
    return round(meters_distance)


def meters_to_geo_distance(meters: "float", latitude: "int" = 0):
    """
    Упрощённое преобразование расстояния в географическую систему координат,
    для коротких дистанций с потерей точности
    """
    degree_in_meters = get_distance_of_degree_latitude(latitude)
    degree = meters / degree_in_meters
    return degree


def get_distance_of_degree_latitude(latitude: "int"):
    if 0 <= latitude < 3:
        distance = 111.3
    elif latitude < 8:
        distance = 110.9
    elif latitude < 13:
        distance = 109.6
    elif latitude < 18:
        distance = 107.6
    elif latitude < 23:
        distance = 104.6
    elif latitude < 28:
        distance = 102.1
    elif latitude < 33:
        distance = 96.5
    elif latitude < 38:
        distance = 91.3
    elif latitude < 43:
        distance = 85.4
    elif latitude < 48:
        distance = 78.8
    elif latitude < 53:
        distance = 71.7
    elif latitude < 58:
        distance = 64.0
    elif latitude < 63:
        distance = 55.8
    elif latitude < 68:
        distance = 47.2
    elif latitude < 73:
        distance = 38.2
    elif latitude < 78:
        distance = 28.9
    else:
        raise RuntimeError()
    distance *= 1000  # в метры
    return round(distance)


class AbstractNearestLocationFinder(metaclass=ABCMeta):
    GEO_M70 = 0.00063  # 70 метров примерно
    _analyzed_point: "GeoPoint"
    DEFAULT_RADIUS: int

    def set_point_for_analyze(self, point: "GeoPoint"):
        self._analyzed_point = point

    def find_nearby_locations(self, radius: "int" = None):

        radius = self.DEFAULT_RADIUS if not radius else radius

        # поиск квадратом, вместо географических координат, для скорости
        lat_start, lat_end, lon_start, lon_end = self.radius_to_geo_square(radius, self._analyzed_point.latitude)
        locations = self.search_nearby_locations_with_square(lat_start, lat_end, lon_start, lon_end)

        return locations

    def radius_to_geo_square(self, radius: "int", latitude) -> "Tuple[float,float,float,float]":
        """
        Определение координат квадрата в градусах, для более быстрого поиска, по пересечению.
        """
        latitude_cathetus = meters_to_geo_distance(radius, latitude=latitude)
        longitude_cathetus = meters_to_geo_distance(radius, latitude=0)

        lat_start = self._analyzed_point.latitude - longitude_cathetus
        lat_end = self._analyzed_point.latitude + longitude_cathetus
        lon_start = self._analyzed_point.longitude - latitude_cathetus
        lon_end = self._analyzed_point.longitude + latitude_cathetus

        return lat_start, lat_end, lon_start, lon_end

    @abstractmethod
    def search_nearby_locations_with_square(
            self, lat_start, lat_end, lon_start, lon_end):
        pass