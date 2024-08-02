"""
这里编写主窗口
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from function import HHT, WVD, CWT, STFT, filtration, json_to_data
from plot_utils import CWT_plot, HHT_plot, STFT_plot, WVD_plot
from PyQt5 import QtWidgets, QtGui, QtCore
from UI.main_ui import Ui_Form
import numpy as np

fs = 360

class Mainwindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)
        self.setupUi(self)
        self.fs = 360

        # 建立文件连接函数
        self.lineEdit.mousePressEvent = self.showFileSelectorDialog
        self.lineEdit_2.mousePressEvent = self.showDirectorySelectorDialog

        # 建立按钮连接函数
        self.CWT.clicked.connect(self.handleCWT)
        self.HHT.clicked.connect(self.handleHHTp)
        self.STFT.clicked.connect(self.handleSTFT)
        self.WVD.clicked.connect(self.handleWVD)

    # 事件绑定还没写，先占位

    def set_processing_method(self):
        sender = self.sender()
        self.processing_method = sender.objectName()   # 新增一个类的属性，处理方式，把处理方式返回给对象

    def showFileSelectorDialog(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "选择输入文件", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
        self.input_path = file_path   # 把获取到的路径赋值给属性
        if file_path:
            self.lineEdit.setText(file_path)   # 让选择文件的路径在输入框中显示出来

    def showDirectorySelectorDialog(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self, "选择输出文件夹", "", options=options)
        self.output_path = directory   # 把获取到的目录赋值给output_path
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
            self.show_message("输入错误，请重新选择有效的文件。")
            return False
        if not output_path:
            self.show_message("输入错误，请选择有效的目录。")
            return False
        return True

    def getSignal(self):
        object = json_to_data.JsonToData(self.input_path)
        self.signal = object.json_to_data()

    def handleHHTp(self):
        self.getSignal()
        object = filtration.Filtration(signal=self.signal, fs=self.fs)
        clean_signal = object.filtration()
        hhtp = HHT.HHT(signal=clean_signal, fs=fs)
        frequencies, times, Sxx = hhtp.hht()
        plot = HHT_plot.HHT_plot(frequencies=frequencies, times=times, Sxx=Sxx, output_path=self.get_input()[1])
        output_file = plot.HHT_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.plotView.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.plotView.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.plotView.resizeEvent = self.resizeEvent

    def handleWVD(self):
        self.getSignal()
        object = filtration.Filtration(signal=self.signal, fs=self.fs)
        clean_signal = object.filtration()
        wvd = WVD.WVD(signal=clean_signal)
        fs = self.fs
        tfr, t, f = wvd.WVD()
        plot = WVD_plot.WVD_plot(tfr=tfr, t=t, f=f, fs=fs, output_path=self.get_input()[1])
        output_file = plot.WVD_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.plotView.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.plotView.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.plotView.resizeEvent = self.resizeEvent

    def handleSTFT(self):
        self.getSignal()
        object = filtration.Filtration(signal=self.signal, fs=self.fs)
        clean_signal = object.filtration()
        stft = STFT.STFT(signal=clean_signal, fs=self.fs)
        frequencies, times, Zxx = stft.stft_use()
        plot = STFT_plot.STFT_plot(frequencies=frequencies, times=times, Zxx=Zxx, output_path=self.get_input()[1])
        output_file = plot.STFT_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.plotView.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.plotView.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.plotView.resizeEvent = self.resizeEvent

    def handleCWT(self):
        self.getSignal()
        object = filtration.Filtration(signal=self.signal, fs=self.fs)
        clean_signal = object.filtration()
        cwt = CWT.CWT(signal=clean_signal, fs=self.fs)
        coefficients, frequencies = cwt.cwt()
        plot = CWT_plot.CWT_plot(frequencies=frequencies, coefficients=coefficients, output_path=self.get_input()[1],
                        signal=clean_signal, fs=fs)
        output_file = plot.CWT_plot()
        self.scene = QtWidgets.QGraphicsScene()
        self.plotView.setScene(self.scene)
        pixmap = QtGui.QPixmap(output_file)
        self.pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(self.pixmapItem)
        self.plotView.fitInView(self.pixmapItem, QtCore.Qt.KeepAspectRatio)
        # 设置 QGraphicsView 的 resize 事件，以便在窗口调整大小时保持图片的比例
        self.plotView.resizeEvent = self.resizeEvent

    # 显示警告信息
    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

