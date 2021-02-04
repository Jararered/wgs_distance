from lambert import *
from vincenty import *
from vincentymod import *
import math
from PyQt5.QtWidgets import *

app = QApplication([])
window = QTableWidget()
window.setWindowTitle("WGS-84 Distance")

col1 = QVBoxLayout()

a = 6378137.0
b = 6356752.314245

# Inputs for geographic coordinate system
col1.latInput1 = QLineEdit()
col1.longInput1 = QLineEdit()

col1.latInput2 = QLineEdit()
col1.longInput2 = QLineEdit()

# Inputs for spherical/cylindrical coordinate system
col1.radiusInput1 = QLineEdit()
col1.azimuthInput1 = QLineEdit()
col1.heightInput1 = QLineEdit()
col1.polarInput1 = QLineEdit()
col1.radiusInput2 = QLineEdit()
col1.azimuthInput2 = QLineEdit()
col1.heightInput2 = QLineEdit()
col1.polarInput2 = QLineEdit()
col1.axialInput1 = QLineEdit()
col1.axialInput2 = QLineEdit()

col1.radiusInput1.setReadOnly(True)
col1.radiusInput2.setReadOnly(True)
col1.radiusInput1.setStyleSheet("QLineEdit" "{" "background : lightgrey;" "}")
col1.radiusInput2.setStyleSheet("QLineEdit" "{" "background : lightgrey;" "}")

# Coordinate system selection box
col2 = QVBoxLayout()
col2.coordinate = QComboBox()
col2.coordinate.addItem("Geographic (Latitude, Longitude)")
col2.coordinate.addItem("Spherical (r, \u03b8, \u03c6)")
col2.coordinate.addItem("Cylindrical (\u03c1, \u03c6, z)")


# Updates the column of inputs each time the coordinate system selection changes
def update_inputs():
    # Removes inputs for previously selected coordinate system
    # This may be a hack-y way of doing this
    for i in reversed(range(col1.count())):
        col1.itemAt(i).widget().setParent(None)

    # Inputs for geographic coordinate system
    if col2.coordinate.currentIndex() == 0:
        col1.addWidget(QLabel("Latitude 1: (degrees)"))
        col1.addWidget(col1.latInput1)
        col1.addWidget(QLabel("Longitude 1: (degrees)"))
        col1.addWidget(col1.longInput1)
        col1.addWidget(QLabel("Latitude 2: (degrees)"))
        col1.addWidget(col1.latInput2)
        col1.addWidget(QLabel("Longitude 2: (degrees)"))
        col1.addWidget(col1.longInput2)

    # Inputs for spherical coordinate system
    if col2.coordinate.currentIndex() == 1:
        col1.addWidget(QLabel("Radius 1: (meters)"))
        col1.addWidget(col1.radiusInput1)
        col1.addWidget(QLabel("Polar 1: (degrees)"))
        col1.addWidget(col1.polarInput1)
        col1.addWidget(QLabel("Azimuth 1: (degrees)"))
        col1.addWidget(col1.azimuthInput1)
        col1.addWidget(QLabel("Radius 2: (meters)"))
        col1.addWidget(col1.radiusInput2)
        col1.addWidget(QLabel("Polar 2: (degrees)"))
        col1.addWidget(col1.polarInput2)
        col1.addWidget(QLabel("Azimuth 2: (degrees)"))
        col1.addWidget(col1.azimuthInput2)

    # Inputs for cylindrical coordinate system
    if col2.coordinate.currentIndex() == 2:
        col1.addWidget(QLabel("Radius 1: (meters)"))
        col1.addWidget(col1.axialInput1)
        col1.addWidget(QLabel("Azimuth 1: (degrees)"))
        col1.addWidget(col1.azimuthInput1)
        col1.addWidget(QLabel("Elevation 1: (meters)"))
        col1.addWidget(col1.heightInput1)
        col1.addWidget(QLabel("Radius 2: (meters)"))
        col1.addWidget(col1.axialInput2)
        col1.addWidget(QLabel("Azimuth 2: (degrees)"))
        col1.addWidget(col1.azimuthInput2)
        col1.addWidget(QLabel("Elevation 2: (meters)"))
        col1.addWidget(col1.heightInput2)


# Updates the column of inputs each time the coordinate system selection changes
update_inputs()
col2.coordinate.currentTextChanged.connect(update_inputs)

col2.calculation = QComboBox()
col2.calculation.addItem("Lambert")
col2.calculation.addItem("Vincenty")
col2.calculation.addItem("Vincenty (Modified)")
col2.calculateButton = QPushButton("Calculate")

col2.addStretch(1)
col2.addWidget(QLabel("Coordinate System:"))
col2.addWidget(col2.coordinate)
col2.addWidget(QLabel("Calculation Method:"))
col2.addWidget(col2.calculation)
col2.addWidget(col2.calculateButton)

col3 = QVBoxLayout()
col3.addWidget(QLabel("Distance: (meters)"))
col3.distanceBox = QLineEdit()
col3.addWidget(col3.distanceBox)
col3.notification = QLabel()
col3.addWidget(col3.notification)


# Calculation performed after clicking calculate
def calculate():
    if col1.latInput1.text().isalpha() | \
            col1.longInput1.text().isalpha() | \
            col1.latInput2.text().isalpha() | \
            col1.longInput2.text().isalpha():

        col3.notification.setText("One or more inputs are not numbers.")

    else:

        if col2.coordinate.currentIndex() == 0:
            # Saving values input by user
            lat1 = math.radians(float(col1.latInput1.text()))
            long1 = math.radians(float(col1.longInput1.text()))
            lat2 = math.radians(float(col1.latInput2.text()))
            long2 = math.radians(float(col1.longInput2.text()))

        if col2.coordinate.currentIndex() == 1:
            # Saving values input by user
            polar1 = math.radians(float(col1.polarInput1.text()))
            azimuth1 = math.radians(float(col1.azimuthInput1.text()))
            polar2 = math.radians(float(col1.polarInput2.text()))
            azimuth2 = math.radians(float(col1.azimuthInput2.text()))

            # Converting from spherical to geographic coordinates
            lat1 = (math.pi / 2) - polar1
            radius1 = math.sqrt((((a ** 2) * math.cos(lat1)) ** 2 + ((b ** 2) * math.sin(lat1)) ** 2) / (
                    (a * math.cos(lat1)) ** 2 + (b * math.sin(lat1)) ** 2))
            long1 = azimuth1
            lat2 = (math.pi / 2) - polar2
            radius2 = math.sqrt((((a ** 2) * math.cos(lat2)) ** 2 + ((b ** 2) * math.sin(lat2)) ** 2) / (
                    (a * math.cos(lat2)) ** 2 + (b * math.sin(lat2)) ** 2))
            long2 = azimuth2

            # Updating radius values
            col1.radiusInput1.setText(str(radius1))
            col1.radiusInput2.setText(str(radius2))

        if col2.coordinate.currentIndex() == 2:
            # Saving values input by user
            axial1 = float(col1.axialInput1.text())
            azimuth1 = math.radians(float(col1.azimuthInput1.text()))
            elevation1 = float(col1.heightInput1.text())
            axial2 = float(col1.axialInput2.text())
            azimuth2 = math.radians(float(col1.azimuthInput2.text()))
            elevation2 = float(col1.heightInput2.text())

            # Converting from cylindrical coordinates to geographic coordinates
            lat1 = math.atan2(elevation1, axial1)
            long1 = azimuth1
            lat2 = math.atan2(elevation2, axial2)
            long2 = azimuth2

        # Passing coordinates to chosen method of calculation
        if col2.calculation.currentText() == "Lambert":
            distance = str(lambert(lat1, long1, lat2, long2))
            col3.distanceBox.setText(distance)
        if col2.calculation.currentText() == "Vincenty":
            distance = str(vincenty(lat1, long1, lat2, long2))
            col3.distanceBox.setText(distance)
        if col2.calculation.currentText() == "Vincenty (Modified)":
            distance = str(vincentymod(lat1, long1, lat2, long2))
            col3.distanceBox.setText(distance)

        col3.notification.setText("Done.")


col2.calculateButton.clicked.connect(calculate)

# Arranging each section in the window
layout = QVBoxLayout()
layout.addLayout(col1)
layout.addLayout(col2)
layout.addLayout(col3)
window.setLayout(layout)

# Displaying the window
window.show()
app.exec()
