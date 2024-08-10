"""
这里编写入口函数
"""
import sys
from main_window_2 import Mainwindow
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
