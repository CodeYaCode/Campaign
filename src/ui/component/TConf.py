# TConf.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'TConf.py'
'@author LiuChen'

# Config universal panel

import sys
import os
from tkinter import *

sys.path.append('../../../')
from src.conf import *

# COLOR
DELETE_BTN_COLOR    = '#F54545'
SAVE_BTN_COLOR  = '#5FBA7D'

class TConf(Tk):
	"""docstring for TConf"""
	def __init__(self, **args):
		super(TConf, self).__init__()
		# prop
		self.type = args['type']
		self.id   = args['id']
		self.confs = propConf[self.type]
		self.row = args['row']
		self.column = args['column']

		# basic conf
		self.resizable(False, False)

		# set components
		self.createWidgets()

	def createWidgets(self):
		# save buttton
		self.saveBtn = Button(self, text = 'SAVE', width = 30, relief = GROOVE, fg = 'white',bg = SAVE_BTN_COLOR, command = self.destroy)
		self.saveBtn.grid(columnspan = 2)

		self.confLabels = []
		self.confEntrys  = []
		row = 1
		# add conf label and entry
		for key in self.confs.keys():
			value = self.confs[key]
			label = Label(self, text = value, width = 10, relief = GROOVE)
			label.grid(row = self.row + row, column = self.column + 0)
			entry = Entry(self, width = 20, relief = GROOVE)
			entry.grid(row = self.row + row, column = self.column + 1)
			self.confLabels.append(label)
			self.confEntrys.append(entry)
			row = row + 1

		# delete button
		self.delBtn = Button(self, text = 'DELETE', width = 30, relief = GROOVE, fg = 'white', bg = DELETE_BTN_COLOR, command = self.destroy)
		self.delBtn.grid(columnspan = 2)
		pass

	def destroy(self):

		super().destroy()

if __name__ == '__main__':
	t = TConf(type = 'general', id = 1, row = 0, column = 0)
	t.mainloop()