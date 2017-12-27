# PlayerWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'PlayerWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from src.ui.widget.ConfWidget import ConfWidget
from src.ui.widget.PlayerConfWidget import PlayerConfWidget

class PlayerWidget(QWidget):
	"""docstring for PlayerWidget"""
	def __init__(self, **args):
		super(PlayerWidget, self).__init__()
		# props
		self.widgets = []
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		self.confLayout = QHBoxLayout()
		self.confLayout.setContentsMargins(0, 0, 0, 0)
		# TODO
		# create an empty players

	def initData(self, **args):
		self.reset()
		if 'args' in args:
			args = args['args']
		if 'player' in args:
			playerWidget = PlayerConfWidget(args = args)
			self.mainLayout.addWidget(playerWidget)
			self.widgets.append(playerWidget)
			self.mainLayout.addLayout(self.confLayout)
			if 'generals' in args:
				generalWidget = ConfWidget(catagory = 'generals', args = args)
				self.confLayout.addWidget(generalWidget)
				self.widgets.append(generalWidget)
			if 'buildings' in args:
				buildingWidget = ConfWidget(catagory = 'buildings', args = args)
				self.confLayout.addWidget(buildingWidget)
				self.widgets.append(buildingWidget)
			if 'slave_buildings' in args:
				slaveBuildingsWidget = ConfWidget(catagory = 'slave_buildings', args = args)
				self.confLayout.addWidget(slaveBuildingsWidget)
				self.widgets.append(slaveBuildingsWidget)

	def reset(self):
		for widget in self.widgets:
			self.mainLayout.removeWidget(widget)
			self.confLayout.removeWidget(widget)
			widget.reset()
		self.widgets = []