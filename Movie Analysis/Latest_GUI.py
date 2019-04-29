import sys
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtGui import QPixmap,QImage,QPalette,QBrush
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
        self.Go.setStyleSheet("background-color: #F39C12;");
        self.Go.setFont(newfont)
        self.Go.move(590, 350)
        self.Go.resize(100,50)
        MainWindow.setCentralWidget(self.centralwidget)


class Dashboard(object):
    def setupUI(self, MainWindow):
        
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(1400, 900)
        MainWindow.setWindowTitle("Dashboard")
        newfont = QtGui.QFont("Times", 25, QtGui.QFont.Bold)
        self.centralwidget = QWidget(MainWindow)
        self.textButton = QPushButton("Text Input", self.centralwidget)
        self.textButton.move(450, 250)
        self.textButton.setStyleSheet('QPushButton {background-color: #F39C12; color: #000000;}')
        #self.textButton.setStyleSheet('color: red')
        #self.textButton.setStyleSheet("background-color: #F39C12;")
        self.textButton.setFont(newfont)
        self.textButton.resize(150,150)
        
        
        self.imageButton = QPushButton("Image Input", self.centralwidget)
        self.imageButton.move(650, 250)
        self.imageButton.resize(150,150)
        self.imageButton.setStyleSheet('QPushButton {background-color: #F39C12; color: #000000;}')
        #self.imageButton.setStyleSheet("background-color: #F39C12;")
        self.imageButton.setFont(newfont)
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
        self.Submit.move(640, 350)
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
        self.Submit.move(640, 350)
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
        label.setStyleSheet('color: #FFFFFF')
        label.move(550,250)
        label.setFont(newfont)
        oImage = QImage("Movie Data Analysis.png")
        #sImage = oImage.scaled(QSize(300,200))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(oImage))                     # 10 = Windowrole
        self.setPalette(palette)
 
        self.setPalette(palette)
        self.MainScreen.setupUI(self)
        self.MainScreen.Go.clicked.connect(self.startDashboard)
        self.MainScreen.Go.clicked.connect(label.hide)
        self.show()
    
    def startTextUi(self):
        self.close()
        self.TextUi.setupUI(self)
        self.setGeometry(100,200,500,550)
        hbox = QHBoxLayout()
        newfont = QtGui.QFont("Times", 25, QtGui.QFont.Bold) 
        self.label = QLabel(self)
        self.label.setText("Query")
        self.label.setFont(newfont)
        self.label.move(350,250)
        self.label.setStyleSheet('color: #FFFFFF')
        self.lineedit = QLineEdit(self)
        hbox.addWidget(self.lineedit)
        self.lineedit.move(450,245)
        self.lineedit.resize(500,50)
        self.lineedit.setStyleSheet('background-color: #F39C12;color: #000000;')
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
        newfont = QtGui.QFont("Times", 25, QtGui.QFont.Bold) 
        self.label = QLabel(self)
        self.label.setText("Path")
        self.label.setFont(newfont)
        self.label.move(350,250)
        self.label.setStyleSheet('color: #FFFFFF')
        self.lineedit = QLineEdit(self)
        hbox.addWidget(self.lineedit)
        self.lineedit.move(450,245)
        self.lineedit.resize(500,50)
        self.lineedit.setStyleSheet('background-color: #F39C12;color: #000000;')
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
            newfont = QtGui.QFont("Times", 25, QtGui.QFont.Bold) 
            self.label[i] = QLabel(self)
            self.label[i].setFont(newfont)
            self.label[i].resize(500,50)
            self.label[i].setText(str((i//4)+1)+"."+questions[i//4])
            self.label[i].setStyleSheet('color: #FFFFFF')
            self.label[i].move(40,(i)*40)
            if(string[i//4]!="None"):
                self.label[i+1] = QLabel(self)
                self.label[i+1].setFont(newfont)
                self.label[i+1].resize(500,40)
                self.label[i+1].setText(string[i//4])
                self.label[i+1].setStyleSheet('color: #FFFFFF')
                self.label[i+1].move(40,(i+1)*40)
            if(location[i//4]!="None"):
                self.label[i+2] = QLabel(self)
                self.image[i//4] = QPixmap(location[i//4])
                self.label[i+2].setPixmap(self.image[i//4])
                self.label[i+2].resize(600,450)
                self.label[i+2].setStyleSheet('color: #FFFFFF')
                self.label[i+2].move(720,(i+1)*38)
            if(description[i//4]!="None"):
                self.label[i+3] = QLabel(self)
                self.label[i+3].setFont(newfont)
                self.label[i+3].resize(500,50)
                self.label[i+3].setText(description[i//4])
                self.label[i+3].setStyleSheet('color: #FFFFFF')
                self.label[i+3].move(40,(i+3)*40)
            
        self.show()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())