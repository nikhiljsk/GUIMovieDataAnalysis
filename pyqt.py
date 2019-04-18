import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QPushButton,QLineEdit,QFormLayout
from PyQt5.QtCore import *
class MainScreen(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(700, 700)
        MainWindow.setWindowTitle("Movie Data Analysis")
        #MainWindow.setText("Welcome")
        newfont = QtGui.QFont("Times", 20, QtGui.QFont.Bold) 
        
        self.centralwidget = QWidget(MainWindow)
        self.Go = QPushButton('Go', self.centralwidget)
        self.Go.setFont(newfont)
        self.Go.move(290, 350)
        self.Go.resize(100,50)
        MainWindow.setCentralWidget(self.centralwidget)


class Dashboard(object):
    def setupUI(self, MainWindow):
        
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(700, 700)
        MainWindow.setWindowTitle("Dashboard")
        self.centralwidget = QWidget(MainWindow)
        self.textButton = QPushButton("Text Input", self.centralwidget)
        self.textButton.move(150, 250)
        self.textButton.resize(150,150)
        
        
        self.imageButton = QPushButton("Image Input", self.centralwidget)
        self.imageButton.move(350, 250)
        self.imageButton.resize(150,150)
        MainWindow.setCentralWidget(self.centralwidget)
        
class ImageUi(object):
    def setupUI(self,MainWindow):
        MainWindow.win = QWidget()
        MainWindow.layout =  QFormLayout()
        MainWindow.textbox = QLineEdit(self)
        MainWindow.textbox.move(20, 20)
        MainWindow.textbox.resize(280,400)
        MainWindow.textbox.setAlignment(QtCore.Qt.AlignLeft)
        MainWindow.textbox.setFont(QtGui.QFont("Arial",20))
        MainWindow.layout.addRow("Query",self.textbox)
        MainWindow.win.setLayout(self.layout)
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(700, 700)
        MainWindow.setWindowTitle("Image Menu")
        self.centralwidget = QWidget(MainWindow)
        
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.MainScreen = MainScreen()
        self.Dashboard = Dashboard()
        self.ImageUi = ImageUi()
        self.startMainScreen()


    def startDashboard(self):
        self.Dashboard.setupUI(self)
        self.Dashboard.textButton.clicked.connect(self.startImageUi)
#        self.Dashboard.textButton.setEnabled(False)
#        self.Dashboard.imageButton.setEnabled(False)
        self.show()

    def startMainScreen(self):
        newfont = QtGui.QFont("Times", 50, QtGui.QFont.Bold) 
        label = QLabel("Welcome",self)
        label.resize(550,150)
        label.move(250,250)
        label.setFont(newfont)
        self.MainScreen.setupUI(self)
        self.MainScreen.Go.clicked.connect(self.startDashboard)
        self.MainScreen.Go.clicked.connect(label.hide)
        self.show()
    
    def startImageUi(self):
        #self.close()
        self.win = QWidget()
        self.layout =  QFormLayout()
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,400)
        self.textbox.setAlignment(QtCore.Qt.AlignLeft)
        self.textbox.setFont(QtGui.QFont("Arial",20))
        self.layout.addRow("Query",self.textbox)
        #self.layout.addButton("Ok")
        self.win.setLayout(self.layout)
        self.win.setWindowTitle("PyQt")
        #self.ImageUi.setupUI(self)
        self.win.show()
        
        
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())