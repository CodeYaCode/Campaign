# tes.py

import sys

__author__ = 'Chen Liu'

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
	app = QApplication(sys.argv)

	win = QWidget()
	win.show()

	sys.exit(app.exec_())