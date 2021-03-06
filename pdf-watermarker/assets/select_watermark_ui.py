from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_watermarkWindow(object):
    def setupUi(self, watermarkWindow):
        watermarkWindow.setObjectName("watermarkWindow")
        watermarkWindow.resize(450, 80)

        self.centralwidget = QtWidgets.QWidget(watermarkWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(9, 40, 281, 30))
        self.lineEdit.setObjectName("lineEdit")

        self.pathButton = QtWidgets.QPushButton(self.centralwidget)
        self.pathButton.setGeometry(QtCore.QRect(295, 40, 70, 30))
        self.pathButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pathButton.setObjectName("pathButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 12, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(370, 40, 70, 30))
        self.confirmButton.setObjectName("confirmButton")
        watermarkWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(watermarkWindow)
        QtCore.QMetaObject.connectSlotsByName(watermarkWindow)

    def retranslateUi(self, watermarkWindow):
        _translate = QtCore.QCoreApplication.translate
        watermarkWindow.setWindowTitle(
            _translate("watermarkWindow", "Select watermark")
        )
        self.pathButton.setText(_translate("watermarkWindow", "Choose pdf"))
        self.label.setText(
            _translate("watermarkWindow", "Choose a watermark file (must be a pdf)")
        )
        self.confirmButton.setText(_translate("watermarkWindow", "Confirm"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    watermarkWindow = QtWidgets.QMainWindow()
    ui = Ui_watermarkWindow()
    ui.setupUi(watermarkWindow)
    watermarkWindow.show()
    sys.exit(app.exec_())
