#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

# QWidgetを継承
class MyWidget(QWidget):
    # キーボードイベントをオーバーライド
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape: # キーがエスケープなら
            self.close() # 閉じる

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget() # 継承したウィジェットを使う
    window.show()
    sys.exit(app.exec_())
