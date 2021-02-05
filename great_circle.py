import math


def great_circle(polar1,polar2,azimuth1,azimuth2):
    # Given two points in spherical coordinates, each containing a radius, polar angle, and azimuth angle, the arc
    #   length between them on a sphere can be calculated.
    # Unpacking inputs:

    radius = 6378137

    # Because the assumption that these two points are on the same spherical plane, derivation can be done on a more
    #   basic unit circle.
    # On a unit circle, the arc length between two points is the same as the angle formed between those two points from
    #   the center of the circle.
    #
    # Utilizing the spherical law of cosines, a spherical triangle can be defined such that:
    # cos(A) = -cos(B)cos(C) + sin(B)sin(C)cos(a)
    # Rearranging this to solve for A, or the distance between the two points considered:
    # A = cos-1(-cos(B)cos(C) + sin(B)sin(C)cos(a))
    # Multiplying this unit circle distance by the radius of earth yields the arc distance between the two points.

    distance = radius*math.acos(
        math.cos(polar1) * math.cos(polar2) + math.sin(polar1) * math.sin(polar2) * math.cos(azimuth2 - azimuth1))

    return distance
