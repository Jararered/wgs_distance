    The great circle calculation assumes that the earth
is a perfect sphere,  and that there is a great circle
path connecting each of the two points,  as well as a
great circle for each point and the point at the
geographic north pole.

    Using this assumption,  the spherical law of
cosines can be used on the spherical triangle formed
between each of these three points, allowing for the
arc length between each of the two specified points
to be found.

    As per WGS-84 standards,  the earth is in fact an
ellipsoid,  however with the great circle approach,
the standard radius used is 6378.1370 km.

    In spherical coordinates,  the polar and azimuth
angles can be used directly,  while in cylindrical
coordinates,  a transformation must be done.

    Converting the from the axial radius and height in
cylindrical coordinates to spherical coordinates
is a simple distance formula calculation to find the
radius in spherical coordinates,  and the
inverse tangent of the axial radius over the height
outputs the spherical elevation/inclination.
The azimuth in both coordinate systems retains
it's definition, and does not need a transformation.
