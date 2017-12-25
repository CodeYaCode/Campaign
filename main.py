# main.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'main.py'
'@author LiuChen'


import sys

from PyQt5.QtWidgets import *

from src import *

app = QApplication(sys.argv)

win = MyWidget(width = 1200, height = 560, title = 'Campaign Editor')
win.show()

sys.exit(app.exec_())