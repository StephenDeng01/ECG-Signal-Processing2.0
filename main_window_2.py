"""
在这里编写新一代的界面
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from function import HHT, HHT_o,  WVD, CWT, STFT, filtration, json_to_data
from plot_utils import CWT_plot, HHT_plot, STFT_plot, WVD_plot, Signal_plot
from PyQt5 import QtWidgets, QtGui, QtCore
from UI.main_ui import Ui_Form


class Mainwindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.fs = 360

        # 建立文件连接函数
        self.lineEdit.mousePressEvent = self.showFileSelectorDialog
        # self.lineEdit_2.mousePressEvent = self.showDirectorySelectorDialog

        # # 将每一个视口都装入列表中：
        # self.graphicsViews = []
        # self.graphicsViews.append(self.graphicsView)
        # self.graphicsViews.append(self.graphicsView_2)
        # self.graphicsViews.append(self.graphicsView_3)
        # self.graphicsViews.append(self.graphicsView_4)
        # self.graphicsViews.append(self.graphicsView_5)
        # self.graphicsViews.append(self.graphicsView_6)
        #
        # # 安装事件过滤器到QGraphicsView，其实就是赋值了一个属性
        # self.graphicsView.viewport().installEventFilter(self)
        # self.graphicsView_2.viewport().installEventFilter(self)
        # self.graphicsView_3.viewport().installEventFilter(self)
        # self.graphicsView_4.viewport().installEventFilter(self)
        # self.graphicsView_5.viewport().installEventFilter(self)
        # self.graphicsView_6.viewport().installEventFilter(self)

        # 绑定按钮的点击事件到函数
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        # 初始化处理方式
        self.processing_method = None

    # 事件绑定还没写，先占位

    def set_processing_method(self):
        sender = self.sender()
        self.processing_method = sender.objectName()  # 新增一个类的属性，处理方式，把处理方式返回给对象

    def showFileSelectorDialog(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "选择输入文件", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
        self.input_path = file_path  # 把获取到的路径赋值给属性
        if file_path:
            self.lineEdit.setText(file_path)  # 让选择文件的路径在输入框中显示出来

    def showDirectorySelectorDialog(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "", options=options)
        self.output_path = directory  # 把获取到的目录赋值给output_path
        if directory:
            self.lineEdit_2.setText(directory)

    def get_input(self):
        input_path = self.lineEdit.text().strip()
        output_path = self.lineEdit_2.text().strip()
        return input_path, output_path

    def validate_inputs(self):
        # 检验输入的信息是否合规
        input_path, output_path = self.get_input()
        if not input_path:
            self.show_message("输入错误!", "请重新选择有效的输入文件。")
            return False
        return True

    def getSignal(self):
        object = json_to_data.JsonToData(self.input_path)
        self.signal = object.json_to_data()
        object = filtration.Filtration(signal=self.signal, fs=self.fs)
        self.clean_signal = object.filtration()

    def handleFil(self):
        plot = Signal_plot.QuzaoPlot(signal=self.clean_signal)
        output_file = plot.QuzaoPlot()
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.graphicsView.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.graphicsView.resizeEvent = self.resizeEvent


    def handleHHTp(self):
        hhtp = HHT.HHT(signal=self.clean_signal, fs=self.fs)
        frequencies, times, Sxx = hhtp.hht()
        plot = HHT_plot.HHT_plot(frequencies=frequencies, times=times, Sxx=Sxx)
        output_file = plot.HHT_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView_2.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.graphicsView_2.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.graphicsView_2.resizeEvent = self.resizeEvent

    def handleHHT_o(self):
        hhto = HHT_o.HHT_o(signal=self.clean_signal, fs=self.fs)
        frequencies, times, Sxx = hhto.hht_o()
        plot = HHT_plot.HHT_plot(frequencies=frequencies, times=times, Sxx=Sxx)
        output_file = plot.HHT_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView_6.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.graphicsView_6.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.graphicsView_6.resizeEvent = self.resizeEvent

    def handleWVD(self):
        wvd = WVD.WVD(signal=self.clean_signal)
        fs = self.fs
        tfr, t, f = wvd.WVD()
        plot = WVD_plot.WVD_plot(tfr=tfr, t=t, f=f, fs=fs)
        output_file = plot.WVD_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView_3.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.graphicsView_3.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.graphicsView_3.resizeEvent = self.resizeEvent

    def handleSTFT(self):
        stft = STFT.STFT(signal=self.clean_signal, fs=self.fs)
        frequencies, times, Zxx = stft.stft_use()
        plot = STFT_plot.STFT_plot(frequencies=frequencies, times=times, Zxx=Zxx)
        output_file = plot.STFT_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView_4.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.graphicsView_4.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.graphicsView_4.resizeEvent = self.resizeEvent

    def handleCWT(self):
        cwt = CWT.CWT(signal=self.clean_signal, fs=self.fs)
        coefficients, frequencies = cwt.cwt()
        plot = CWT_plot.CWT_plot(frequencies=frequencies, coefficients=coefficients,
                                 signal=self.clean_signal, fs=self.fs)
        output_file = plot.CWT_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView_5.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.graphicsView_5.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.graphicsView_5.resizeEvent = self.resizeEvent

    # 显示警告信息
    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def on_pushButton_clicked(self):
        # 这里是按钮点击后要执行的代码
        self.getSignal()
        self.handleFil()
        self.handleHHTp()
        self.handleWVD()
        self.handleSTFT()
        self.handleCWT()
        self.handleHHT_o()

        # 事件过滤器方法

    # def eventFilter(self, source, event):
    #     if event.type() == QtCore.QEvent.MouseButtonPress:
    #         if event.button() == QtCore.Qt.LeftButton:
    #             for index, graphicsView in enumerate(self.graphicsViews):
    #                 if source == graphicsView.viewport():
    #                     pos = event.pos()
    #                     print(f"Mouse clicked at {pos} in graphicsView {index + 1}")
    #                     self.handleGraphicsViewClick(index + 1)
    #                     break
    #         return True  # 返回 True 表示事件已经被处理，不再继续传递
    #     return super(Mainwindow, self).eventFilter(source, event)
    #
    # def handleGraphicsViewClick(self, view_index):
    #     # 根据点击的视窗调用不同的函数
    #     if view_index == 1:
    #         if not self.validate_inputs():
    #             return
    #         self.handleFil()
    #     if view_index == 2:
    #         if not self.validate_inputs():
    #             return
    #         self.handleHHTp()
    #     if view_index == 3:
    #         if not self.validate_inputs():
    #             return
    #         self.handleWVD()
    #     if view_index == 4:
    #         if not self.validate_inputs():
    #             return
    #         self.handleSTFT()
    #     if view_index == 5:
    #         if not self.validate_inputs():
    #             return
    #         self.handleCWT()
    #     if view_index == 6:
    #         if not self.validate_inputs():
    #             return
    #         self.handleHHT_o()


