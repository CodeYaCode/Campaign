# ContainerWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ContainerWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from src.ui.widget.PlayerWidget import PlayerWidget

class ContainerWidget(QWidget):
	"""docstring for ContainerWidget"""
	def __init__(self, **args):
		super(ContainerWidget, self).__init__()
		# props
		self.players = []
		# main layout
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		
	def addPlayer(self, conf = ''):
		player = PlayerWidget()
		self.players.append(player)
		player.initData(args = conf)
		self.mainLayout.addWidget(player)

	def initData(self, **args):
		self.reset()
		if 'args' in args:
			args = args['args']
		if 'conf' in args:
			confs = args['conf']
			for conf in confs:
				self.addPlayer(conf)

	def reset(self):
		for p in self.players:
			self.mainLayout.removeWidget(p)
			p.reset()
		pass