# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class MainStyle(QWidget):
    def __init__(self, parent=None):
        super(MainStyle, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(200, 300)
        self.btn_close = QPushButton()
        self.btn_close.setStyleSheet("""QPushButton{background-image:url(./img/btn_close_normal.png);width:39px;height:18px;padding-top:0px;border:0px;}
                                    QPushButton:hover{background-image:url(./img/btn_close_highlight.png);}
                                    QPushButton:pressed{background-image:url(./img/btn_close_down.png);}""")

        self.btn_min = QPushButton()
        self.btn_min.setStyleSheet("QPushButton{background-image:url(./img/btn_close_normal1.png);width:39px;height:18px;padding-top:0px;border:0px;}")

        self.btn_setting = QPushButton()
        self.btn_setting.setStyleSheet("""QPushButton{background-image:url(./img/icon_cog.png);width:16px;height:16px;padding-top:0px;border:0px;margin-right:15px;}
                                        QPushButton:hover{background-image:url(./img/icon_cogs.png);}""")

        self.btn_photo = QPushButton()
        self.btn_photo.setStyleSheet("""QPushButton{background-image:url(./img/photo.png);width:32px;height:26px; border-radius: 10px;
                                        margin-right:60px;}""")   # border-radius 元素添加圆角边框！

        #按钮样式一
        btn_one=QPushButton("按钮样式一", self)
        btn_one.setGeometry(0, 100,100, 200)
        btn_one.setStyleSheet("QPushButton{background-color:blue;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        #按钮样式二
        btn_two=QPushButton("按钮样式二", self)
        btn_two.setGeometry(100,100, 101, 200)
        btn_two.setStyleSheet("QPushButton{background-color:#D30000;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")

        # 顶部布局
        self.topBarLayout = QHBoxLayout()
        self.topBarLayout.addStretch()
        self.topBarLayout.addWidget(self.btn_photo,0,Qt.AlignRight | Qt.AlignHCenter)
        self.topBarLayout.addWidget(self.btn_setting,0,Qt.AlignRight | Qt.AlignHCenter)
        self.topBarLayout.addWidget(self.btn_min,0,Qt.AlignRight | Qt.AlignTop)
        self.topBarLayout.addWidget(self.btn_close,0,Qt.AlignRight | Qt.AlignTop)
        #main布局
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.topBarLayout,0)
        self.mainLayout.addStretch()
        self.mainLayout.addStretch()
        self.setLayout(self.mainLayout)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)

        btn_two.clicked.connect(self.close)




    def paintEvent(self,event):
        self.painter = QtGui.QPainter()
        self.painter.begin(self)
        self.painter.drawPixmap(self.rect(), QPixmap("./img/mianbg.png"))
        self.painter.end()

    #支持窗口拖动,重写两个方法
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainStyle()
    main.show()
    app.exec_()