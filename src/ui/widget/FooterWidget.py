# FooterWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'FooterWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

class FooterWidget(QWidget):
	"""docstring for FooterWidget"""
	def __init__(self, **args):
		super(FooterWidget, self).__init__()
		
		# props

		# main layout
		self.mainLayout = QHBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.mainLayout.addWidget(QPushButton('Hello'))
		self.mainLayout.addStretch()

	def initData(self, **args):
		print('TODO FOOTER')
		pass