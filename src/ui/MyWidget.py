# MyWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'MyWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sys.path.append('../..')
from src.ui.layout import *

class MyWidget(QWidget):
	"""docstring for MyWinget"""
	def __init__(self, **args):
		super(MyWidget, self).__init__()
		# props
		self.width = 1200
		self.height = 560
		self.title = 'Hello World'
		if 'width' in args:
			self.width = args['width']
		if 'height' in args:
			self.height = args['height']
		if 'title' in args:
			self.title = args['title']
		# init
		self.resize(self.width, self.height)
		self.setWindowTitle(self.title)
		self.setWindowFlags(Qt.FramelessWindowHint)
		# set gui content
		self.initUI()

	def initUI(self):
		# main layout
		self.mainLayout = QVBoxLayout()
		# control
		self.controlLayout = ControlLayout(self.close)
		self.mainLayout.addLayout(self.controlLayout)
		# set layout
		self.setLayout(self.mainLayout)
		pass

	def show(self):
		super().show()

if __name__ == '__main__':
	import sys

	from PyQt5.QtWidgets import *
	app = QApplication(sys.argv)
	w = MyWidget(width = 1200, height = 560)
	w.show()
	sys.exit(app.exec_())