import math


def vincenty(phi1, l1, phi2, l2):
    semi_major = 6378137.0
    semi_minor = 6356752.314245
    flattening = (semi_major - semi_minor) / semi_major

    u1 = math.atan((1 - flattening) * math.tan(phi1))
    u2 = math.atan((1 - flattening) * math.tan(phi2))
    l21 = l2 - l1

    lamda1 = l21
    delta = 1

    while delta > 10e-12:
        sigma = math.atan2((math.sqrt((math.cos(u2) * math.sin(lamda1)) ** 2 + (
                    math.cos(u1) * math.sin(u2) - math.sin(u1) * math.cos(u2) * math.cos(lamda1)) ** 2)),
                           (math.sin(u1) * math.sin(u2) + math.cos(u1) * math.cos(u2) * math.cos(lamda1)))
        alpha = math.asin((math.cos(u1) * math.cos(u2) * math.sin(lamda1)) / (math.sin(sigma)))
        sigma_m = (1 / 2) * math.acos(math.cos(sigma) - ((2 * math.sin(u1) * math.sin(u2)) / ((math.cos(alpha)) ** 2)))
        c = (flattening / 16) * ((math.cos(alpha)) ** 2) * (4 + flattening * (4 - 3 * ((math.cos(alpha)) ** 2)))
        lamda2 = l21 + (1 - c) * flattening * math.sin(alpha) * (sigma + c * math.sin(sigma) * (
                    math.cos(2 * sigma_m) + c * math.cos(sigma) * (-1 + 2 * ((math.cos((2 * sigma_m))) ** 2))))
        delta = abs(lamda2 - lamda1)
        lamda1 = lamda2

    u = math.sqrt(((math.cos(alpha)) ** 2) * ((semi_major ** 2 - semi_minor ** 2) / (semi_minor ** 2)))
    a = 1 + ((u ** 2) / 16384) * (4096 + (u ** 2) * (-768 + (u ** 2) * (320 - 175 * (u ** 2))))
    b = ((u ** 2) / 1024) * (256 + (u ** 2) * (-128 + (u ** 2) * (74 - 47 * (u ** 2))))
    delta_sigma = b * math.sin(sigma) * (math.cos(2 * sigma_m) + (1 / 4) * b * (
                math.cos(sigma) * (-1 + 2 * ((math.cos(2 * sigma_m)) ** 2)) - (b / 6) * math.cos(2 * sigma_m) * (
                    -3 + 4 * ((math.sin(sigma)) ** 2)) * (-3 + 4 * ((math.cos(2 * sigma_m)) ** 2))))
    distance = semi_minor * a * (sigma - delta_sigma)
    print(distance)

    return distance
