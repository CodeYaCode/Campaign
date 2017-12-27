# MyWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'MyWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from ctypes.wintypes import *

sys.path.append('../..')
from src.ui.widget import *

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

class MyWidget(QWidget):
	"""docstring for MyWinget"""
	def __init__(self, **args):
		super(MyWidget, self).__init__()
		# props
		self.w = 1200
		self.h = 560
		self.title = 'Hello World'
		if 'w' in args:
			self.w = args['width']
		if 'h' in args:
			self.h = args['height']
		if 'title' in args:
			self.title = args['title']
		self.needInitWidgets = []
		# main layout
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		# init
		self.resize(self.w, self.h)
		self.setWindowTitle(self.title)
		self.setWindowFlags(Qt.FramelessWindowHint)
		# set gui content
		self.initUI()

	def initUI(self):
		# control
		self.controlWidget = ControlWidget(fClose = self.close, fLoad = self.load)
		self.mainLayout.addWidget(self.controlWidget)
		
		# container
		self.containerWidget = ContainerWidget()
		# header
		self.headerWidget = HeaderWidget(fAddPlayer = self.containerWidget.addPlayer)
		# footer
		self.footerWidget = FooterWidget()

		# need init
		self.needInitWidgets.append(self.headerWidget)
		self.needInitWidgets.append(self.containerWidget)
		self.needInitWidgets.append(self.footerWidget)

		# mainLayout add widget
		self.mainLayout.addWidget(self.headerWidget)
		self.mainLayout.addWidget(self.containerWidget)
		self.mainLayout.addStretch()
		self.mainLayout.addWidget(self.footerWidget)

		# set layout
		self.setLayout(self.mainLayout)

	def load(self, name):
		if not name:
			return
		# get the archive file
		archive = open(sys.path[0] + '/src/archive/%s.py' % (name), 'r', encoding='utf-8')
		s = self._textToObj(archive.readlines())
		campaign = eval(s)
		# set current file name
		self.controlWidget.setCurrentLabel(name)
		# init datas
		for widget in self.needInitWidgets:
			widget.initData(args = campaign)

	def _textToObj(self, text):
		result = ''
		for t in text:
			result = result + t.strip('\n').strip('\t')
		return result

	def show(self):
		super().show()
 
	def GET_X_LPARAM(self, param):
		return param & 0xffff
 
	def GET_Y_LPARAM(self, param):
		return param >> 16

	def nativeEvent1(self, eventType, message):
		# change position and size event
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

if __name__ == '__main__':
	import sys

	from PyQt5.QtWidgets import *
	app = QApplication(sys.argv)
	w = MyWidget(width = 1200, height = 560)
	w.show()
	sys.exit(app.exec_())