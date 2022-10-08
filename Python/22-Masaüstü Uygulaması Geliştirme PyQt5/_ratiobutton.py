from PyQt5 import QtWidgets
import sys
from _ratiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioLise.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.radioIspanya.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)

        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioOrtaokul.toggled.connect(self.onClickedEgitim)
       
        self.ui.btn_UlkeSecim.clicked.connect(self.getSelectedUlke)
        self.ui.btn_EgitimSecim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen Ülke: "+ rb.text())
        
    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print("Seçilen Eğitim: "+ rb.text())
        
    def getSelectedUlke(self):
        items = self.ui.groupUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_ulke.setText("Seçilen Ülke: " + rb.text())
 
    def getSelectedEgitim(self):
        items = self.ui.groupEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_egitim.setText("Seçilen Eğitim: " + rb.text())



def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton { color: red}")
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()