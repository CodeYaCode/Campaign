# DetailWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'DetailWidget.py'
'@author LiuChen'

import sys

# from PyQt5.QtWidgets import QWidget, QGridLayout, QDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPalette
from PyQt5.QtGui import *

# from src.conf.propConf import propConf

class DetailDialog(QDialog):
	"""docstring for DetailWidget"""
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.resize(240, 200)
		# 表格布局，用来布局QLabel和QLineEdit及QSpinBox
		grid = QGridLayout()
		grid.addWidget(QLabel(u'姓名', parent=self), 0, 0, 1, 1)
		self.leName = QLineEdit(parent=self)
		grid.addWidget(self.leName, 0, 1, 1, 1)
		grid.addWidget(QLabel(u'年龄', parent=self), 1, 0, 1, 1)
		self.sbAge = QSpinBox(parent=self)
		grid.addWidget(self.sbAge, 1, 1, 1, 1)
		# 创建ButtonBox，用户确定和取消
		buttonBox = QDialogButtonBox(parent=self)
		buttonBox.setOrientation(QtCore.Qt.Horizontal) # 设置为水平方向
		buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok) # 确定和取消两个按钮
		# 连接信号和槽
		buttonBox.accepted.connect(self.accept) # 确定
		buttonBox.rejected.connect(self.reject) # 取消
		# 垂直布局，布局表格及按钮
		layout = QVBoxLayout()
		# 加入前面创建的表格布局
		layout.addLayout(grid)
		# 放一个间隔对象美化布局
		spacerItem = QSpacerItem(20, 48, QSizePolicy.Minimum, QSizePolicy.Expanding)
		layout.addItem(spacerItem)
		# ButtonBox
		layout.addWidget(buttonBox)
		self.setLayout(layout)

