"""
这里输出去噪后的信号图
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# 设置绘图大小
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class QuzaoPlot:
    def __init__(self, signal):
        self.signal = signal
        self.fs = 360
        # self.output_path = output_path

    def QuzaoPlot(self):
        # 绘制彩色频谱图
        t = np.arange(len(self.signal)) / self.fs

        # 绘制 ECG 信号
        plt.figure(figsize=(12, 6))
        plt.plot(t, self.signal, label='ECG Signal')
        plt.title('心电信号图（ECG）')
        plt.xlabel('时间 (s)')
        plt.ylabel('幅值 (uV)')
        plt.legend()
        plt.grid()

        # 保存图形到一个临时文件中
        file_path = '.\\plot.png'
        plt.savefig(file_path)

        # 关闭图形以释放内存
        plt.close()

        return file_path
