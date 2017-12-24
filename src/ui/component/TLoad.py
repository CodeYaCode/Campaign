# FLoad.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'FControl.py'
'@author LiuChen'

import sys
import os
from tkinter import *

# COLOR
CLOSE_BTN_COLOR    = '#F54545'
ARCHIVE_BTN_COLOR  = '#317EF3'

# SIZE
BTN_WIDTH = 20

class TLoad(Tk):
	"""docstring for FLoad"""
	def __init__(self, **args):
		super(TLoad, self).__init__()
		# prop
		self.initData = args['initData']
		self.devX = int(args['devX'] - BTN_WIDTH)
		self.devY = int(args['devY'])
		# basic conf
		self.geometry('+%s+%s' % (self.devX, self.devY))
		self.title('Archive')
		self.overrideredirect(True)
		# get archive
		self.archive = self.getArchive()
		# set components
		self.createWidgets()

	def getArchive(self):
		rootPath = sys.path[0] + '/src/archive'
		# rootPath = '../../archive/'
		print('current archive path:', rootPath)
		for a, b, c in os.walk(rootPath):
			return c

	def createWidgets(self):
		Button(self, text = 'CLOSE', width = BTN_WIDTH * 2, relief = GROOVE, fg = 'white', bg = CLOSE_BTN_COLOR, 
			command = lambda: self.click('')).grid(row = 0)
		self.archiveBtn = {}
		row = 1
		if not self.archive:
			Label(self, text = 'No load.').grid()
			return
		for name in self.archive:
			name = name.split('.')[0]
			btn = Button(self, text = 'Load %s' % (name), width = BTN_WIDTH * 2, relief = GROOVE, fg = 'white', bg = ARCHIVE_BTN_COLOR, 
				command = lambda name=name: self.click(name))
			self.archiveBtn[name] = btn
			btn.grid(row = row, column = 0)
			row = row + 1

	def click(self, name):
		if name:
			name = self.archiveBtn[name]['text'].split(' ')[1]
		self.initData(name)
		self.destroy()

	def destroy(self):
		super().destroy()

if __name__ == '__main__':
	TLoad().mainloop()
