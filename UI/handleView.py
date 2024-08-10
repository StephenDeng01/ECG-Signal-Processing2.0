from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsPixmapItem, QGraphicsTextItem
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QEvent
from main_ui_1 import Ui_Form


class MyForm(QWidget, Ui_Form):
    def __init__(self, output_file, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)

        # 创建场景并设置到QGraphicsView
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)

        # 标志图像是否已经显示
        self.image_displayed = False

        # 安装事件过滤器到graphicsView
        self.graphicsView.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        if source == self.graphicsView.viewport() and event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                self.handleMouseClick()
            return True
        return super(MyForm, self).eventFilter(source, event)

    def handleMouseClick(self):
        if not self.image_displayed:
            # 添加图像
            pixmap = QPixmap(self.output_file)
            self.scene.addItem(QGraphicsPixmapItem(pixmap))
            self.image_displayed = True
        else:
            self.scene.clear()
            self.image_displayed = False

    def addFixedText(self, processing_method_name):
        # 添加固定文本
        text_item = QGraphicsTextItem(processing_method_name)
        font = QFont("Arial", 16)
        text_item.setFont(font)
        text_item.setDefaultTextColor(Qt.red)  # 设置文本颜色
        text_item.setPos(10, 10)  # 设置文本位置
        self.scene.addItem(text_item)

        self.image_displayed = False