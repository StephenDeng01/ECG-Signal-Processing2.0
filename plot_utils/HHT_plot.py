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
    def __init__(self, frequencies, times, Sxx, output_path):
        self.frequencies = frequencies
        self.times = times
        self.Sxx = Sxx
        self.output_path = output_path


    def HHT_plot(self):
        # 绘制彩色频谱图
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(self.times, self.frequencies, 10 * np.log10(self.Sxx), shading='gouraud', cmap='inferno')
        plt.colorbar(label='振幅（mV）')
        plt.title('信号频谱图')
        plt.xlabel('时间 (s)')
        plt.ylabel('频率 (Hz)')
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        base_filename = os.path.join(self.output_path, "HHT")
        file_extension = ".png"
        output_file = base_filename + file_extension
        counter = 1

        while os.path.exists(output_file):
            output_file = f"{base_filename}_{counter}{file_extension}"
            counter += 1
        plt.savefig(output_file)
        return output_file
