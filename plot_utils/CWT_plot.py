"""
这里写连续小波变换（CWT）的成图代码
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# 设置绘图大小
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class CWT_plot:
    def __init__(self, coefficients, frequencies, signal, fs):
        self.coefficients = coefficients
        self.frequencies = frequencies
        # self.output_path = output_path
        self.signal = signal
        self.fs = fs

    def CWT_plot(self):
        # 绘制CWT频谱图
        plt.figure(figsize=(12, 6))
        plt.imshow(np.abs(self.coefficients), extent=[0, (len(self.signal) / self.fs), 1, 128], cmap='inferno', aspect='auto',
                   vmax=abs(self.coefficients).max(), vmin=0)
        plt.title('CWT 处理')
        plt.xlabel('Time (s)')
        plt.ylabel('频率')
        plt.colorbar(label='振幅')
        plt.ylim([0, 120])  # 根据需要调整频率范围
        # 保存图形到一个临时文件中
        file_path = '.\\plot.png'
        plt.savefig(file_path)

        # 关闭图形以释放内存
        plt.close()

        return file_path
