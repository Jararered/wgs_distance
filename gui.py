from PyQt5.QtWidgets import *

from great_circle import *
from lambert import *
from vincenty import *
from vincenty_mod import *

app = QApplication([])
window = QWidget()
window.setFixedWidth(400)
window.setWindowTitle("WGS-84 Distance")

# Defining Layouts
sec1 = QHBoxLayout()
sec2 = QVBoxLayout()
sec3 = QVBoxLayout()

# Coordinate Layout
coord1 = QVBoxLayout()
coord2 = QVBoxLayout()
coord3 = QVBoxLayout()

# Creating input boxes
latInput1 = QLineEdit()
latInput1.setText("0.0")
longInput1 = QLineEdit()
longInput1.setText("0.0")
latInput2 = QLineEdit()
latInput2.setText("0.0")
longInput2 = QLineEdit()
longInput2.setText("0.0")
radiusInput1 = QLineEdit()
radiusInput1.setText("0.0")
azimuthInput1 = QLineEdit()
azimuthInput1.setText("0.0")
heightInput1 = QLineEdit()
heightInput1.setText("0.0")
polarInput1 = QLineEdit()
polarInput1.setText("0.0")
radiusInput2 = QLineEdit()
radiusInput2.setText("0.0")
azimuthInput2 = QLineEdit()
azimuthInput2.setText("0.0")
heightInput2 = QLineEdit()
heightInput2.setText("0.0")
polarInput2 = QLineEdit()
polarInput2.setText("0.0")
axialInput1 = QLineEdit()
axialInput1.setText("0.0")
axialInput2 = QLineEdit()
axialInput2.setText("0.0")

# Coordinate system selection box
coordinateSystem = QComboBox()
coordinateSystem.addItem("Geographic (Lat, Long)")
coordinateSystem.addItem("Spherical (r, \u03b8, \u03c6)")
coordinateSystem.addItem("Cylindrical (\u03c1, \u03c6, z)")

# Calculation method selection box
calculationMethod = QComboBox()
calculationMethod.addItem("Great Circle")
calculationMethod.addItem("Lambert")
calculationMethod.addItem("Vincenty")
calculationMethod.addItem("Vincenty (Modified)")

# Results section
calculateButton = QPushButton("Calculate")
distanceBox = QLineEdit()
notification = QLabel()


def update_inputs():
    # Removes inputs for previously selected coordinate system
    for i in reversed(range(coord1.count())):
        coord1.itemAt(i).widget().setParent(None)
    for i in reversed(range(coord2.count())):
        coord2.itemAt(i).widget().setParent(None)
    for i in reversed(range(coord3.count())):
        coord3.itemAt(i).widget().setParent(None)

    # Inputs for geographic coordinate system
    if coordinateSystem.currentIndex() == 0:
        coord1.addWidget(QLabel("Latitude 1:"))
        coord1.addWidget(latInput1)
        coord1.addWidget(QLabel("Latitude 2:"))
        coord1.addWidget(latInput2)
        coord2.addWidget(QLabel("Longitude 1:"))
        coord2.addWidget(longInput1)
        coord2.addWidget(QLabel("Longitude 2:"))
        coord2.addWidget(longInput2)

    # Inputs for spherical coordinate system
    if coordinateSystem.currentIndex() == 1:
        coord1.addWidget(QLabel("Radius 1:"))
        coord1.addWidget(radiusInput1)
        radiusInput1.setText("6378137.0")
        coord1.addWidget(QLabel("Radius 2:"))
        coord1.addWidget(radiusInput2)
        radiusInput2.setText("6378137.0")
        coord2.addWidget(QLabel("Polar 1:"))
        coord2.addWidget(polarInput1)
        coord2.addWidget(QLabel("Polar 2:"))
        coord2.addWidget(polarInput2)
        coord3.addWidget(QLabel("Azimuth 1"))
        coord3.addWidget(azimuthInput1)
        coord3.addWidget(QLabel("Azimuth 2"))
        coord3.addWidget(azimuthInput2)

    # Inputs for cylindrical coordinate system
    if coordinateSystem.currentIndex() == 2:
        coord1.addWidget(QLabel("Radius 1:"))
        coord1.addWidget(axialInput1)
        coord1.addWidget(QLabel("Radius 2:"))
        coord1.addWidget(axialInput2)
        coord2.addWidget(QLabel("Azimuth 1:"))
        coord2.addWidget(azimuthInput1)
        coord2.addWidget(QLabel("Azimuth 2:"))
        coord2.addWidget(azimuthInput2)
        coord3.addWidget(QLabel("Elevation 1:"))
        coord3.addWidget(heightInput1)
        coord3.addWidget(QLabel("Elevation 2:"))
        coord3.addWidget(heightInput2)


# Updates the column of inputs each time the coordinate system selection changes
update_inputs()
coordinateSystem.currentTextChanged.connect(update_inputs)

# Populating coordinate input section
sec1.addLayout(coord1)
sec1.addLayout(coord2)
sec1.addLayout(coord3)

# Populating coordinate system and calculation selection
sec2.addWidget(QLabel("Coordinate System:"))
sec2.addWidget(coordinateSystem)
sec2.addWidget(QLabel("Calculation Method:"))
sec2.addWidget(calculationMethod)

# Populating calculate button and distance box
sec3.addWidget(calculateButton)
sec3.addWidget(QLabel("Distance: (meters)"))
sec3.addWidget(distanceBox)
sec3.addWidget(notification)


# Calculation performed after clicking calculate
def calculate():
    if latInput1.text().isalpha() | \
            longInput1.text().isalpha() | \
            latInput2.text().isalpha() | \
            longInput2.text().isalpha():

        notification.setText("One or more inputs are not numbers.")

    else:
        lat1 = math.radians(float(latInput1.text()))
        lat2 = math.radians(float(latInput2.text()))
        long1 = math.radians(float(longInput1.text()))
        long2 = math.radians(float(longInput2.text()))
        radius1 = float(radiusInput1.text())
        radius2 = float(radiusInput2.text())
        polar1 = math.radians(float(polarInput1.text()))
        polar2 = math.radians(float(polarInput2.text()))
        axial1 = float(axialInput1.text())
        axial2 = float(axialInput2.text())
        azimuth1 = math.radians(float(azimuthInput1.text()))
        azimuth2 = math.radians(float(azimuthInput2.text()))
        elevation1 = float(heightInput1.text())
        elevation2 = float(heightInput2.text())

        if coordinateSystem.currentIndex() == 0:
            # # Saving geographic coordinates input by user
            # lat1 = math.radians(float(latInput1.text()))
            # long1 = math.radians(float(longInput1.text()))
            # lat2 = math.radians(float(latInput2.text()))
            # long2 = math.radians(float(longInput2.text()))

            # Converting to spherical coordinates
            polar1 = lat1 - (math.pi / 2)
            azimuth1 = long1
            polar2 = lat2 - (math.pi / 2)
            azimuth2 = long2

        if coordinateSystem.currentIndex() == 1:
            # # Saving spherical coordinates input by user
            # polar1 = math.radians(float(polarInput1.text()))
            # azimuth1 = math.radians(float(azimuthInput1.text()))
            # polar2 = math.radians(float(polarInput2.text()))
            # azimuth2 = math.radians(float(azimuthInput2.text()))

            # Converting from spherical to geographic coordinates
            a = 6378137.0
            b = 6356752.314245

            lat1 = (math.pi / 2) - polar1
            # radius1 = math.sqrt((((a ** 2) * math.cos(lat1)) ** 2 + ((b ** 2) * math.sin(lat1)) ** 2) / (
            #         (a * math.cos(lat1)) ** 2 + (b * math.sin(lat1)) ** 2))
            long1 = azimuth1
            lat2 = (math.pi / 2) - polar2
            # radius2 = math.sqrt((((a ** 2) * math.cos(lat2)) ** 2 + ((b ** 2) * math.sin(lat2)) ** 2) / (
            #         (a * math.cos(lat2)) ** 2 + (b * math.sin(lat2)) ** 2))
            long2 = azimuth2

            # Updating radius values
            # radiusInput1.setText(str(radius1))
            # radiusInput2.setText(str(radius2))

        if coordinateSystem.currentIndex() == 2:
            # # Saving cylindrical coordinates input by user
            # axial1 = float(axialInput1.text())
            # azimuth1 = math.radians(float(azimuthInput1.text()))
            # elevation1 = float(heightInput1.text())
            # axial2 = float(axialInput2.text())
            # azimuth2 = math.radians(float(azimuthInput2.text()))
            # elevation2 = float(heightInput2.text())

            # Converting from cylindrical coordinates to geographic coordinates
            lat1 = math.atan2(elevation1, axial1)
            long1 = azimuth1
            lat2 = math.atan2(elevation2, axial2)
            long2 = azimuth2

        # Passing coordinates to chosen method of calculation
        if calculationMethod.currentText() == "Great Circle":
            distance = str(great_circle(coordinateSystem.currentIndex(), radius1, radius2, polar1, polar2, azimuth1, azimuth2, axial1, axial2, elevation1, elevation2))
            distanceBox.setText(distance)

        if calculationMethod.currentText() == "Lambert":
            distance = str(lambert(lat1, long1, lat2, long2))
            distanceBox.setText(distance)

        if calculationMethod.currentText() == "Vincenty":
            distance = str(vincenty(lat1, long1, lat2, long2))
            distanceBox.setText(distance)

        if calculationMethod.currentText() == "Vincenty (Modified)":
            distance = str(vincenty_mod(lat1, long1, lat2, long2))
            distanceBox.setText(distance)

        notification.setText("Done.")


calculateButton.clicked.connect(calculate)

layout = QVBoxLayout()
layout.addLayout(sec1)
layout.addLayout(sec2)
layout.addLayout(sec3)
window.setLayout(layout)

# Displaying the window
window.show()
app.exec()
