# Application.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'Application.py'
'@author LiuChen'

import sys
from tkinter import *

from src.ui.component import *

# CONSTANTS

# COLOR

# SIZE
WIDTH  = 1200
HEIGHT = 560
DEV_X  = 100
DEV_Y  = DEV_X
SIZE   = '%sx%s+%s+%s'

class Application(Tk):
	"""docstring for Application"""
	def __init__(self):
		super(Application, self).__init__()
		# prop
		self.tLoad = None
		# Basic conf
		screenWidth, screenHeight = self.maxsize()
		self.size = SIZE % (str(WIDTH), str(HEIGHT), int((screenWidth - WIDTH) / 2), int((screenHeight - HEIGHT) / 2))
		self.geometry(self.size)
		print(sys.path)
		self.title('Campaign Eidtor')
		self.resizable(False, False)
		# self.overrideredirect(True)

		self.createWidgets()

	def createWidgets(self):
		# Control
		self.control = FControl(master = self, openLoad = self.openTLoad, save = self.save, quit = self.destroy, 
			row = 0, column = 0, width = WIDTH, height = 30)
		# Header
		self.header = FHeader(master = self, row = 1, column = 0, width = WIDTH, height = 30)

		# Container
		self.container = Frame()

		# Footer
		self.footer = Frame()
	
	def initData(self, name):
		if self.tLoad:
			self.tLoad = None
			print(name)
			# TODO init data

	def openTLoad(self):
		print(self.tLoad)
		if not self.tLoad:
			self.tLoad = TLoad(initData = self.initData, devX = WIDTH / 2 + DEV_X, devY = HEIGHT / 2 + DEV_Y)
			self.tLoad.mainloop()
		pass

	def save(self):
		pass

	def destroy(self):
		# TODO SAVE TEMPLATE
		if self.tLoad:
			self.tLoad.destroy()
		super().destroy()

if __name__ == '__main__':
	app = Application()
	app.mainloop()