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
HEIGHT = 100
DEV_X  = 100
DEV_Y  = DEV_X
SIZE   = '%sx%s+%s+%s' % (str(WIDTH), str(HEIGHT), DEV_X, DEV_Y)

class Application(Tk):
	"""docstring for Application"""
	def __init__(self):
		super(Application, self).__init__()
		# prop
		self.tLoad = None
		# Basic conf
		self.geometry(SIZE)
		self.title('Campaign eidtor')
		# self.overrideredirect(True)

		self.createWidgets()
		# Button(text='click', command=self.left).grid()

	def createWidgets(self):
		# Control
		self.control = FControl(openLoad = self.openTLoad, save = self.save, quit = self.exit)

	
	def initData(self):
		if self.tLoad:
			self.tLoad.quit()
			self.tLoad = None

	def openTLoad(self):
		if not self.tLoad:
			self.tLoad = TLoad(callback = self.initData)
			self.tLoad.mainloop()
		pass

	def save(self):
		pass

	def exit(self):
		# TODO SAVE TEMPLATE
		self.quit()

if __name__ == '__main__':
	app = Application()
	app.mainloop()