"""
这里画hhtp变换的matplotlib图像
"""

import os
import matplotlib.pyplot as plt
import numpy as np

# 设置绘图大小
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class HHT_plot:
    def __init__(self, frequencies, times, Sxx):
        self.frequencies = frequencies
        self.times = times
        self.Sxx = Sxx
        # self.output_path = output_path


    def HHT_plot(self):
        # 绘制彩色频谱图
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(self.times, self.frequencies, 10 * np.log10(self.Sxx), shading='gouraud', cmap='inferno')
        plt.colorbar(label='振幅（mV）')
        plt.title('信号频谱图')
        plt.xlabel('时间 (s)')
        plt.ylabel('频率 (Hz)')
        # 保存图形到一个临时文件中
        file_path = '.\\plot.png'
        plt.savefig(file_path)

        # 关闭图形以释放内存
        plt.close()

        return file_path
