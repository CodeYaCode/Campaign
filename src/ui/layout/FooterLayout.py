# FooterLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'FooterLayout.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *

class FooterLayout(QHBoxLayout):
	"""docstring for FooterLayout"""
	def __init__(self, **args):
		super(FooterLayout, self).__init__()
		
		self.setContentsMargins(0, 0, 0, 0)
		self.addWidget(QPushButton('Hello'))
		self.addStretch()

	def initData(self, **args):
		print('TODO FOOTER')
		pass