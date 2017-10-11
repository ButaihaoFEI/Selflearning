import json
import math

class Agent:

    def __init__(self,position,**agent_attributes):
        for attr_name, attr_value in agent_attributes.items():
            setattr(self,attr_name, attr_value)
            # self.attr_name = attr_value

class Position:

    def __init__(self,longitude_degree,latitude_degree):
        self.longitude_degree = longitude_degree
        self.latitude_degree = latitude_degree

    @property
    def longitude(self):
        return self.longitude_degree * math.pi / 180

    @property
    def latitude(self):
        return self.latitude_degree * math.pi / 180

class Zone:

    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1
    HEIGHT_DEGREES = 1
    ZONES = []

    def __init__(self,corner1,corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.inhabitants = 0

    @classmethod
    def initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(longitude, latitude)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                zone = Zone(bottom_left_corner,top_right_corner)
                cls.ZONES.append(zone)
        print(len(cls.ZONES))

def main():
    for agent_attributes in json.load(open("la_poo_avec_python-master/agents-100k.json")):
        longitude = agent_attributes.pop("longitude")
        latitude = agent_attributes.pop("latitude")
        position = Position(longitude,latitude)
        agent = Agent(position,**agent_attributes)  # 不确定有多少数量的参数，字典用两颗星

        Zone.initialize_zones()

main()