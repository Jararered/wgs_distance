def great_circle(inputs):

    # Given two points in spherical coordinates, each containing a radius, polar angle, and azimuth angle, the arc length between them on a sphere can be calculated.
    # Unpacking inputs
    polar1 = inputs.polar1
    polar2 = inputs.polar2
    azimuth1 = inputs.azimuth1
    azimuth2 = inputs.azimuth2

    # Because the assumption that these two points are on the same spherical plane, derivation can be done on a more basic unit circle.
    # On a unit circle, the arc length between two points is the same as the angle formed between those two points from the center of the circle.
    #
    # Utilizing the spherical law of cosines, a spherical triangle can be defined such that:
    # sin(A)/sin(a) = sin(B)/sin(b) = sin(C)/sin(c)
    #

