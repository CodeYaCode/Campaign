# ConfWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ConfWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

from src.conf.propConf import propConf
from src.ui.widget.DetailDialog import DetailDialog

# CONSTANTS

# QSS
BTN_STYLE = '''
	QPushButton:hover:!pressed { background-color: rgb(167, 205, 255);
    border-style: outset;
    border-width: 1px; border-color: green; }
'''

class ConfWidget(QWidget):
	"""docstring for ConfWidget"""
	def __init__(self, catagory, **args):
		super(ConfWidget, self).__init__()
		# props
		# main layout
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.widgets = []
		# basic conf
		pal = QPalette(self.palette());
		pal.setColor(QPalette.Background, Qt.gray);
		self.setAutoFillBackground(True);
		self.setPalette(pal);
		# init ui
		self.initUI(catagory, args)

	def initUI(self, catagory, args):
		self.addBtn = QPushButton('Add')
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
