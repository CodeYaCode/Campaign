# PlayerConfWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'PlayerConfWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QInputDialog, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

from src.conf.propConf import propConf

# COLOR
DELETE_BTN_COLOR = '#F54545'

# QSS
DELETE_BTN_QSS = '''
	width: 60px;
	height: 20px;
	border: 0;
	color: white;
	background-color: %s
''' % (DELETE_BTN_COLOR)

class PlayerConfWidget(QWidget):
	"""docstring for PlayerConfWidget"""
	def __init__(self, **args):
		super(PlayerConfWidget, self).__init__()
		# props
		# main layout
		self.mainLayout = QHBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.widgets = []
		# basic conf
		pal = QPalette(self.palette());
		pal.setColor(QPalette.Background, QColor('#DDD'));
		self.setAutoFillBackground(True);
		self.setPalette(pal);
		# init ui
		self.initUI(args)

	def initUI(self, args):
		conf = propConf['player']
		args = args['args']
		brief = conf['brief']
		print(brief)
		for key in brief.keys():
			value = brief[key]
			name = '%s : %s  '
			if 'player' in args:
				p = args['player']
				name = name % (value, str(p[key]))
			else:
				name = 'New player'
			label = QLabel(name)
			self.mainLayout.addWidget(label)
			self.widgets.append(label)
			
		self.mainLayout.addStretch()

		# self.saveBtn = QPushButton('Save')
		# self.saveBtn.setStyleSheet('border-radius: 0;background-color: %s' % (SAVE_BTN_COLOR))
		# self.mainLayout.addWidget(self.saveBtn)

		self.deleteBtn = QPushButton('Delete')
		self.deleteBtn.setStyleSheet(DELETE_BTN_QSS)
		self.mainLayout.addWidget(self.deleteBtn)

	def reset(self):
		for widget in self.widgets:
			self.mainLayout.removeWidget(widget)
			widget.deleteLater()
		self.widgets = []