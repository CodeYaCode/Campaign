# ConfLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ConfLayout.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *

class ConfLayout(QVBoxLayout):
	"""docstring for ConfLayout"""
	def __init__(self, catagory, **args):
		super(ConfLayout, self).__init__()
		# props
		self.widgets = []
		# init ui
		self.setContentsMargins(0, 0, 0, 0)
		self.initUI(catagory, args)

	def initUI(self, catagory, args):
		self.addBtn = QPushButton('Add')
		self.addBtn.clicked.connect(lambda: print('hello %s' % args))
		self.addWidget(self.addBtn)
		if 'args' in args:
			args = args['args']
			if catagory in args:
				btn = QPushButton(catagory)
				self.addWidget(btn)
				self.widgets.append(btn)
				btn = QPushButton(catagory)
				self.addWidget(btn)
				self.widgets.append(btn)

	def reset(self):
		for widget in self.widgets:
			widget.deleteLater()
		self.widgets = []