import math


def great_circle(polar1, polar2, azimuth1, azimuth2):

    radius = 6378137

    distance = radius*math.acos(
        math.cos(polar1) * math.cos(polar2) + math.sin(polar1) * math.sin(polar2) * math.cos(azimuth2 - azimuth1))

    print(distance)
    return distance
