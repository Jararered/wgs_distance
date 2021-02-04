import math


def lambert(lat1, long1, lat2, long2):
    semi_major = 6378137.0
    semi_minor = 6356752.314245
    flattening = (semi_major - semi_minor) / semi_major

    rlat1 = math.atan((1 - flattening) * math.tan(lat1))
    rlat2 = math.atan((1 - flattening) * math.tan(lat2))
    p = (rlat1 + rlat2) / 2
    q = (rlat2 - rlat1) / 2
    sigma = math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(long2 - long1)))
    x = (sigma - math.sin(sigma)) * ((((math.sin(p)) ** 2) * (math.cos(q)) ** 2) / ((math.cos(sigma / 2)) ** 2))
    y = (sigma + math.sin(sigma)) * ((((math.cos(p)) ** 2) * (math.sin(q)) ** 2) / ((math.sin(sigma / 2)) ** 2))

    distance = semi_major * (sigma - (flattening / 2) * (x + y))
    print(distance)
    return distance
