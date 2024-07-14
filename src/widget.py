from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QComboBox
from PySide6 import QtGui
#from PySide6.QtCore import
from api import file_data_dict

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        #Title above window
        self.setWindowTitle("PyExchange")

        #Label for USD input
        label1 = QLabel("Enter USD Amount: ")
        self.usd = QLineEdit()
        #Makes sure the input is a number
        self.usd.setValidator(QtGui.QDoubleValidator(0.99, 99.99, 2))

        #Button to show conversion direction
        self.dirButton = QPushButton()
        self.dirButton.setIcon(QtGui.QIcon('src\dirLTR.png'))

        #Shows conversion result
        self.currency2 = QLineEdit()

        #Button to enable conversion
        convButton = QPushButton("Convert!")
        convButton.clicked.connect(self.conversion_clicked)

        #Layout of label, usd, conv arrow, value
        hLayout = QHBoxLayout()
        hLayout.addWidget(label1)
        hLayout.addWidget(self.usd)
        hLayout.addWidget(self.dirButton)
        hLayout.addWidget(self.currency2)

        #Drop down to select Iso code
        self.comboBox = QComboBox(self)
        #Loops through iso codes and adds them to combo box
        for iso_code, conv_rate in file_data_dict['conversion_rates'].items():
            self.comboBox.addItem(f"{iso_code}")
        
        #Layout of input, combobox of iso codes, and conv button
        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.comboBox)
        vLayout.addWidget(convButton)

        self.setLayout(vLayout)

    #Slots
    def conversion_clicked(self):
        iso = self.comboBox.currentText()
        conv = file_data_dict['conversion_rates'].get(iso)
        #print(f"{iso}, {conv}")
        convertedValue = float(self.usd.text()) * float(conv)
        self.currency2.setText(f"{convertedValue:.2f}")