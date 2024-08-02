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
    def __init__(self, coefficients, frequencies, output_path, signal, fs):
        self.coefficients = coefficients
        self.frequencies = frequencies
        self.output_path = output_path
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
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        base_filename = os.path.join(self.output_path, "CWT")
        file_extension = ".png"
        output_file = base_filename + file_extension
        counter = 1

        while os.path.exists(output_file):
            output_file = f"{base_filename}_{counter}{file_extension}"
            counter += 1
        plt.savefig(output_file)
        return output_file