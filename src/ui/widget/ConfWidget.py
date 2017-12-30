# ConfWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ConfWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from src.conf.propConf import propConf
from src.ui.widget.DetailDialog import DetailDialog

# CONSTANTS

# COLOR
ADD_BTN_COLOR  = '#5FBA7D'
# CONF_BTN_COLOR = '#F1F2F6'
CONF_BTN_COLOR = '#ABCDEF'

# QSS
ADD_BTN_QSS = '''
	height: 25px;
	border: none;
	color: white;
	background-color: %s
''' % (ADD_BTN_COLOR)

BTN_STYLE = '''
	height: 25px;
	border: 0;
	margin-top: 2px;
	color: black;
	background-color: %s
''' % (CONF_BTN_COLOR)

class ConfWidget(QWidget):
	"""docstring for ConfWidget"""
	def __init__(self, catagory, **args):
		super(ConfWidget, self).__init__()
		# props
		# main layout
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.mainLayout.setSpacing(0)

		self.widgets = []
		# basic conf
		pal = QPalette(self.palette());
		pal.setColor(QPalette.Background, QColor(23, 23, 23, 23));
		self.setAutoFillBackground(True);
		self.setPalette(pal);
		# init ui
		self.initUI(catagory, args)

	def initUI(self, catagory, args):
		self.addBtn = QPushButton('Add')
		self.addBtn.setStyleSheet(ADD_BTN_QSS)
		self.addBtn.clicked.connect(lambda: print('hello %s' % args))
		self.mainLayout.addWidget(self.addBtn)
		if 'args' in args:
			args = args['args']
			if catagory in args:
				catas = args[catagory]
				for cat in catas:
					conf = propConf[catagory]
					if 'brief' in conf:
						brief = conf['brief']
						btnName = self._getBtnName(cat, brief)
						btn = QPushButton(btnName)
					else:
						btn = QPushButton('New %s' % (catagory))
					btn.setStyleSheet(BTN_STYLE)
					btn.clicked.connect(self.openDetail)
					self.mainLayout.addWidget(btn)
					self.widgets.append(btn)

		self.mainLayout.addStretch()

	def reset(self):
		for widget in self.widgets:
			self.mainLayout.removeWidget(widget)
			widget.deleteLater()
		self.widgets = []

	# , cat, conf
	def openDetail(self, catagory):
		print('open')
		pass

	def _getBtnName(self, cat, brief):
		# cat data source 
		# brief key value
		btnName = ''
		for b in brief.keys():
			if b in cat:
				btnName += '%s:%s ' % (brief[b], cat[b])
		return btnName
