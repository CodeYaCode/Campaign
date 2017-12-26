# ContainerLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ContainerLayout.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *

from src.ui.layout.PlayerLayout import PlayerLayout

class ContainerLayout(QVBoxLayout):
	"""docstring for ContainerLayout"""
	def __init__(self, **args):
		super(ContainerLayout, self).__init__()
		# props
		self.players = []
		
	def addPlayer(self, conf = ''):
		player = PlayerLayout()
		self.players.append(player)
		player.initData(args = conf)
		self.addLayout(player)

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
			self.removeItem(p)
			p.reset()
		pass