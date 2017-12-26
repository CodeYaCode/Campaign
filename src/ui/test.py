import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
import sip
from ctypes.wintypes import *
from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)
 
#print (help(MSG))
PADDING = 2
#UP,DOWN,LEFT,RIGHT,LEFTTOP,LEFTBOTTOM,RIGHTTOP,RIGHTBOTTOM,UNDIRECT = range(9)
HTLEFT = 10
HTRIGHT = 11
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17
HTCAPTION = 2
 
class CustomWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.initUI()
 
    def isInTitle(self, xPos, yPos):
        return yPos < 30
 
    def GET_X_LPARAM(self, param):
        return param & 0xffff
 
    def GET_Y_LPARAM(self, param):
        return param >> 16
 
    def nativeEvent(self,eventType,message):
        result = 0
        msg2 = ctypes.wintypes.MSG.from_address(message.__int__())
        minV,maxV = 1,20
        if msg2.message == 0x0084:
            #print(msg2)
            xPos = self.GET_X_LPARAM(msg2.lParam) - self.frameGeometry().x()
            yPos = self.GET_Y_LPARAM(msg2.lParam) - self.frameGeometry().y()
#             if self.childAt(xPos,yPos) == 0:
#                 result = HTCAPTION
#             else:
#                 return (False,result)
            if(xPos > minV and xPos < maxV):
                result = HTLEFT
            elif(xPos > (self.width() - maxV) and xPos < (self.width() - minV)):
                result = HTRIGHT
            elif(yPos > minV and yPos < maxV):
                result = HTTOP
            elif(yPos > (self.height() - maxV) and yPos < (self.height() - minV)):
                result = HTBOTTOM
            elif(xPos > minV and xPos < maxV and yPos > minV and yPos < maxV):
                result = HTTOPLEFT
            elif(xPos > (self.width() - maxV) and xPos < (self.width() - minV) and yPos > minV and yPos < maxV):
                result = HTTOPRIGHT
            elif(xPos > minV and xPos < maxV and yPos > (self.height() - maxV) and yPos < (self.height() - minV)):
                result = HTBOTTOMLEFT
            elif(xPos > (self.width() - maxV) and xPos < (self.width() - minV) and yPos > (self.height() - maxV) and yPos < (self.height() - minV)):
                result = HTBOTTOMRIGHT
            else:
                result = HTCAPTION
            return (True,result)
        ret= QWidget.nativeEvent(self,eventType,message)
        return ret
 
    def initUI(self):
        self.lb1 = QLabel("Ubuntu", self)
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
 
        combo.move(50, 50)
        self.lb1.move(50, 150)
 
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()
 
    def onActivated(self, text):
        self.lb1.setText(text)
        self.lb1.adjustSize()
 
 
 
 
 
if __name__ == '__main__':
    app = QApplication([])
    try:
        w = CustomWidget ()
        w.show()
    except:
        import traceback
        traceback.print_exc()
 
    app.exec_()
