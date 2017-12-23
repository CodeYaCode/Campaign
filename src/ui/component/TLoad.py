# FLoad.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'FControl.py'
'@author LiuChen'

import sys
import os
from tkinter import *

# COLOR
ARCHIVE_BTN_COLOR  = '#317EF3'

# SIZE
BTN_WIDTH = 20

class TLoad(Tk):
	"""docstring for FLoad"""
	def __init__(self, callback = None):
		super(TLoad, self).__init__()
		# prop
		self.callback = callback
		# get archive
		self.archive = self.getArchive()
		# set components
		self.createWidgets()		

	def getArchive(self):
		rootPath = sys.path[0] + '/src/archive'
		# rootPath = '../../archive'
		print('current archive path:', rootPath)
		for a, b, c in os.walk(rootPath):
			return c

	def createWidgets(self):
		self.archiveBtn = []
		row = 0
		if not self.archive:
			return 
		for name in self.archive:
			name = name.split('.')[0]
			btn = Button(self, text = name, width = BTN_WIDTH, relief = GROOVE, fg = 'white', bg = ARCHIVE_BTN_COLOR, command = self.callback)
			self.archiveBtn.append(btn)
			btn.grid(row = row, column = 0, sticky = W)
			row = row + 1

if __name__ == '__main__':
	TLoad().mainloop()