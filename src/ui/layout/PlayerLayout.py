# PlayerLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'PlayerLayout.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *

from src.ui.layout.ConfLayout import ConfLayout

class PlayerLayout(QHBoxLayout):
	"""docstring for PlayerLayout"""
	def __init__(self, **args):
		super(PlayerLayout, self).__init__()

		self.layouts = []
		# TODO
		# create an empty players

	def initData(self, **args):
		self.reset()
		if 'args' in args:
			args = args['args']
		if 'player' in args:
			playerLayout = ConfLayout(catagory = 'player', args = args)
			self.addLayout(playerLayout)
			self.layouts.append(playerLayout)
			if 'generals' in args:
				generalLayout = ConfLayout(catagory = 'generals', args = args)
				self.addLayout(generalLayout)
				self.layouts.append(generalLayout)
			if 'buildings' in args:
				buildingLayout = ConfLayout(catagory = 'buildings', args = args)
				self.addLayout(buildingLayout)
				self.layouts.append(buildingLayout)

	def reset(self):
		for layout in self.layouts:
			self.removeItem(layout)
			layout.reset()
		self.layouts = []