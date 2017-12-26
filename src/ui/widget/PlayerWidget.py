# PlayerWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'PlayerWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout

from src.ui.widget.ConfWidget import ConfWidget

class PlayerWidget(QWidget):
	"""docstring for PlayerWidget"""
	def __init__(self, **args):
		super(PlayerWidget, self).__init__()
		# props
		self.layout = QHBoxLayout()
		self.widgets = []
		# TODO
		# create an empty players

	def initData(self, **args):
		self.reset()
		if 'args' in args:
			args = args['args']
		if 'player' in args:
			playerWidget = ConfWidget(catagory = 'player', args = args)
			self.layout.addWidget(playerWidget)
			self.widgets.append(playerWidget)
			if 'generals' in args:
				generalWidget = ConfWidget(catagory = 'generals', args = args)
				self.layout.addWidget(generalWidget)
				self.widgets.append(generalWidget)
			if 'buildings' in args:
				buildingWidget = ConfWidget(catagory = 'buildings', args = args)
				self.layout.addWidget(buildingWidget)
				self.widgets.append(buildingWidget)

	def reset(self):
		for widget in self.widgets:
			self.layout.removeItem(widget)
			widget.reset()
		self.widgets = []