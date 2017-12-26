# ConfWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ConfWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class ConfWidget(QWidget):
	"""docstring for ConfWidget"""
	def __init__(self, catagory, **args):
		super(ConfWidget, self).__init__()
		# props
		self.layout = QVBoxLayout()
		self.widgets = []
		# init ui
		self.setContentsMargins(0, 0, 0, 0)
		self.initUI(catagory, args)

	def initUI(self, catagory, args):
		self.addBtn = QPushButton('Add')
		self.addBtn.clicked.connect(lambda: print('hello %s' % args))
		self.layout.addWidget(self.addBtn)
		if 'args' in args:
			args = args['args']
			if catagory in args:
				btn = QPushButton(catagory)
				self.layout.addWidget(btn)
				self.widgets.append(btn)
				btn = QPushButton(catagory)
				self.layout.addWidget(btn)
				self.widgets.append(btn)

	def reset(self):
		for widget in self.widgets:
			widget.deleteLater()
		self.widgets = []