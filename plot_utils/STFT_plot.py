"""
这里写短时傅里叶变换（STFT）的成图代码
"""

import os
import matplotlib.pyplot as plt

class STFT_plot:
    def __init__(self, frequencies, times, Zxx):
        self.frequencies = frequencies
        self.times = times
        self.Zxx = Zxx
        # self.output_path = output_path

    def STFT_plot(self):
        # 绘制彩色频谱图
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(self.times, self.frequencies, self.Zxx, shading='gouraud', cmap='inferno')
        plt.colorbar(label='振幅（mV）')
        plt.title('信号频谱图')
        plt.xlabel('时间 (s)')
        plt.ylabel('频率 (Hz)')
        plt.ylim([0, 120])  # 根据需要调整频率范围
        # 保存图形到一个临时文件中
        file_path = '.\\plot.png'
        plt.savefig(file_path)

        # 关闭图形以释放内存
        plt.close()

        return file_path

