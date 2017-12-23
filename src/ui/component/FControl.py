# FControl.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'FControl.py'
'@author LiuChen'

import sys
import os
from tkinter import *

sys.path.append('../..')
from src.conf.version import version
from src.ui.component.TLoad import TLoad

# CONSTANTS

# COLOR
CLOSE_BTN_COLOR = '#F54545'
LOAD_BTN_COLOR  = '#317EF3'
SAVE_BTN_COLOR  = '#5FBA7D'

# SIZE
BTN_WIDTH = 3


class FControl(Frame):
	"""docstring for FControl"""
	def __init__(self, master = None, openLoad = None, save = None, quit = None, row = 0, rowspan = 1, column = 0, columnspan = 1, **arg):
		super(FControl, self).__init__()
		Frame.__init__(self, master, arg)
		# Some conf
		self.row = row
		self.rowspan = rowspan
		self.column = column
		self.columnspan = columnspan
		self.version = version
		# Method
		self.openLoad = openLoad
		self.save = save
		self.quit = quit
		# self.width = args['width']
		self.width = 1200
		self.height = 100
		# Set components
		self.createWidgets()

	def createWidgets(self):
		# close button
		self.closeBtn = Button(text = 'X', width = BTN_WIDTH * 1, relief = GROOVE, fg = 'white', bg = CLOSE_BTN_COLOR, command = self.quit)
		self.closeBtn.grid(row = self.row, column = self.column + 0, sticky = W)

		# Load button
		self.loadBtn = Button(text = 'Load', width = BTN_WIDTH * 2, relief = GROOVE, fg = 'white', bg = LOAD_BTN_COLOR, command = self.openLoad)
		self.loadBtn.grid(row = self.row, column = self.column + 1, sticky = W)

		# Save button
		self.saveBtn = Button(text = 'Save', width = BTN_WIDTH * 4, relief = GROOVE, fg = 'white', bg = SAVE_BTN_COLOR, command = self.save)
		self.saveBtn.grid(row = self.row, column = self.column + 2, sticky = W)

		# Info label
		self.infoLabel = Label(text = 'Campaign Version: ' + self.version)
		self.infoLabel.grid(row = self.row, column = 5)

if __name__ == '__main__':
	root = Tk()
	FControl(root, row = 0, column = 0, bg = 'green')
	root.mainloop()
