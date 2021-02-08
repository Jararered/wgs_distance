import math


def great_circle(coordinate_system, radius1, radius2, polar1, polar2, azimuth1, azimuth2, axial1, axial2, elevation1,
                 elevation2):
    if coordinate_system == 0:
        radius = 6378137.0
        distance = radius * math.acos(
            math.cos(polar1) * math.cos(polar2) + math.sin(polar1) * math.sin(polar2) * math.cos(azimuth2 - azimuth1))

    if coordinate_system == 1:
        print(coordinate_system)
        radius = (radius1 + radius2) / 2
        print(radius)
        distance = radius * math.acos(
            math.cos(polar1) * math.cos(polar2) + math.sin(polar1) * math.sin(polar2) * math.cos(azimuth2 - azimuth1))
        print(distance)

    if coordinate_system == 2:
        print(coordinate_system)
        radius = math.sqrt(((axial1 + axial2) / 2) ** 2 + ((elevation1 + elevation2) / 2) ** 2)
        print(radius)
        distance = radius * math.acos(
            math.cos(math.atan2(axial1, elevation1)) * math.cos(math.atan2(axial2, elevation2)) + math.sin(
                math.atan2(axial1, elevation1)) * math.sin(math.atan2(axial2, elevation2)) * math.cos(
                azimuth2 - azimuth1))
        print(distance)

    return distance
