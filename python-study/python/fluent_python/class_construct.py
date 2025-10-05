# 表示地理位置的经纬度
class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

moscow = Coordinate(55.76, 37.62)
location = Coordinate(55.76, 37.62)
print(location == moscow)
print((location.lat, location.lon) == (moscow.lat, moscow.lon))

moscow = Coordinate(55.76, 37.62)
print(moscow == Coordinate(lat=55.76, lon=37.62))


from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'