import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QPushButton,QLineEdit,QFormLayout,QHBoxLayout
from PyQt5.QtCore import *
from helper_functions import process_input_text_query, process_input_image_query


class MainScreen(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(1400, 900)
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
        MainWindow.setFixedSize(1400, 900)
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
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(1400, 900)
        MainWindow.setWindowTitle("Text Input")
        newfont = QtGui.QFont("Times", 20, QtGui.QFont.Bold) 
        self.centralwidget = QWidget(MainWindow)
        self.Submit = QPushButton('Submit', self.centralwidget)
        self.Submit.setFont(newfont)
        self.Submit.move(290, 350)
        self.Submit.resize(100,50)
        MainWindow.setCentralWidget(self.centralwidget)
        
        
class TextUi(object):
    def setupUI(self,MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(1400, 900)
        MainWindow.setWindowTitle("Text Input")
        newfont = QtGui.QFont("Times", 20, QtGui.QFont.Bold) 
        self.centralwidget = QWidget(MainWindow)
        self.Submit = QPushButton('Submit', self.centralwidget)
        self.Submit.setFont(newfont)
        self.Submit.move(290, 350)
        self.Submit.resize(100,50)
        MainWindow.setCentralWidget(self.centralwidget)
class TextOutput(object):
    def setupUI(self,MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(1400, 900)
        MainWindow.setWindowTitle("Output")
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.MainScreen = MainScreen()
        self.Dashboard = Dashboard()
        self.TextUi = TextUi()
        self.TextOutput = TextOutput()
        self.ImageUi = ImageUi()
        self.startMainScreen()



    def startDashboard(self):
        self.Dashboard.setupUI(self)
        self.Dashboard.textButton.clicked.connect(self.startTextUi)
        self.Dashboard.imageButton.clicked.connect(self.startImageUi)
        #self.Dashboard.textButton.clicked.connect(self.hide)
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
    
    def startTextUi(self):
        self.close()
        self.TextUi.setupUI(self)
        self.setGeometry(100,200,500,550)
        hbox = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText("Query")
        self.label.move(50,250)
        self.lineedit = QLineEdit(self)
        hbox.addWidget(self.lineedit)
        self.lineedit.move(100,250)
        self.lineedit.resize(500,50)
        self.lineedit.setFont(QtGui.QFont("Sanserif",20))
        self.TextUi.Submit.clicked.connect(self.textSendData)
        self.TextUi.Submit.clicked.connect(self.lineedit.hide)
        self.TextUi.Submit.clicked.connect(self.label.hide)
        self.show()
        
    def textSendData(self):
        input_query = self.lineedit.text()
        output_data = process_input_text_query(input_query)
        output_data_questions = output_data[0].split("|")
        output_data_string = output_data[1].split("|")
        output_data_image_loc = output_data[2].split("|")
        output_data_image_descption = output_data[3].split("|")
        self.startTextOutput(output_data_questions,output_data_string,output_data_image_loc,output_data_image_descption)
        
    def startImageUi(self):
        self.close()
        self.ImageUi.setupUI(self)
        self.setGeometry(100,200,500,550)
        hbox = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText("Path")
        self.label.move(50,250)
        self.lineedit = QLineEdit(self)
        hbox.addWidget(self.lineedit)
        self.lineedit.move(100,250)
        self.lineedit.resize(500,50)
        self.lineedit.setFont(QtGui.QFont("Sanserif",20))
        self.ImageUi.Submit.clicked.connect(self.imageSendData)
        self.ImageUi.Submit.clicked.connect(self.lineedit.hide)
        self.ImageUi.Submit.clicked.connect(self.label.hide)
        self.show()

        
    def imageSendData(self):
        input_query = self.lineedit.text()
        output_data = process_input_image_query(input_query)
        output_data_questions = output_data[0].split("|")
        output_data_string = output_data[1].split("|")
        output_data_image_loc = output_data[2].split("|")
        output_data_image_descption = output_data[3].split("|")
        self.startTextOutput(output_data_questions,output_data_string,output_data_image_loc,output_data_image_descption)
        
        
    def startTextOutput(self,questions,string,location,description):
        #print(questions,"\n",string,"\n",location,"\n",description)
        self.close()
        self.TextOutput.setupUI(self)
        self.label = [0]*len(questions)*4
        self.image = [0]*len(questions)
        for i in range(0,4*len(questions),4):
            newfont = QtGui.QFont("Times", 15, QtGui.QFont.Bold) 
            self.label[i] = QLabel(self)
            self.label[i].setFont(newfont)
            self.label[i].resize(500,50)
            self.label[i].setText(str((i//4)+1)+"."+questions[i//4])
            self.label[i].move(40,(i)*30)
            if(string[i//4]!="None"):
                self.label[i+1] = QLabel(self)
                self.label[i+1].setFont(newfont)
                self.label[i+1].resize(500,30)
                self.label[i+1].setText(string[i//4])
                self.label[i+1].move(40,(i+1)*30)
            if(location[i//4]!="None"):
                self.label[i+2] = QLabel(self)
                self.image[i//4] = QPixmap(location[i//4])
                self.label[i+2].setPixmap(self.image[i//4])
                self.label[i+2].resize(700,450)
                self.label[i+2].move(720,(i+1)*30)
            if(description[i//4]!="None"):
                self.label[i+3] = QLabel(self)
                self.label[i+3].setFont(newfont)
                self.label[i+3].resize(500,50)
                self.label[i+3].setText(description[i//4])
                self.label[i+3].move(40,(i+3)*30)
            
        self.show()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())