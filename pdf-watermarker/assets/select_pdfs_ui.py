from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pdfsDialog(object):
    def setupUi(self, pdfsDialog):
        pdfsDialog.setObjectName("pdfsDialog")
        pdfsDialog.resize(390, 240)

        self.pdfLlistWidget = QtWidgets.QListWidget(pdfsDialog)
        self.pdfLlistWidget.setGeometry(QtCore.QRect(10, 10, 370, 181))
        self.pdfLlistWidget.setObjectName("pdfLlistWidget")

        self.addButton = QtWidgets.QPushButton(pdfsDialog)
        self.addButton.setGeometry(QtCore.QRect(20, 195, 55, 20))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setObjectName("addButton")

        self.removeButton = QtWidgets.QPushButton(pdfsDialog)
        self.removeButton.setGeometry(QtCore.QRect(75, 195, 75, 20))
        self.removeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.removeButton.setObjectName("removeButton")

        self.okButton = QtWidgets.QPushButton(pdfsDialog)
        self.okButton.setGeometry(QtCore.QRect(280, 215, 90, 25))
        self.okButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setObjectName("okButton")

        self.folderButton = QtWidgets.QPushButton(pdfsDialog)
        self.folderButton.setGeometry(QtCore.QRect(270, 195, 105, 25))
        self.folderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.folderButton.setObjectName("folderButton")

        self.addDirectoryButton = QtWidgets.QPushButton(pdfsDialog)
        self.addDirectoryButton.setGeometry(QtCore.QRect(35, 220, 100, 20))
        self.addDirectoryButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addDirectoryButton.setObjectName("addDirectoryButton")

        self.retranslateUi(pdfsDialog)
        QtCore.QMetaObject.connectSlotsByName(pdfsDialog)

    def retranslateUi(self, pdfsDialog):
        _translate = QtCore.QCoreApplication.translate
        pdfsDialog.setWindowTitle(
            _translate("pdfsDialog", "Select pdfs to be watermarked")
        )
        self.addButton.setText(_translate("pdfsDialog", "Add pdf"))
        self.removeButton.setText(_translate("pdfsDialog", "Remove pdf"))
        self.okButton.setText(_translate("pdfsDialog", "Watermark pdfs"))
        self.folderButton.setText(_translate("pdfsDialog", "Select output folder"))
        self.addDirectoryButton.setText(_translate("pdfsDialog", "Add all from folder"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    pdfsDialog = QtWidgets.QDialog()
    ui = Ui_pdfsDialog()
    ui.setupUi(pdfsDialog)
    pdfsDialog.show()
    sys.exit(app.exec_())
