"""
这里写短时傅里叶变换（STFT）的成图代码
"""

import os
import matplotlib.pyplot as plt

class STFT_plot:
    def __init__(self, frequencies, times, Zxx, output_path):
        self.frequencies = frequencies
        self.times = times
        self.Zxx = Zxx
        self.output_path = output_path

    def STFT_plot(self):
        # 绘制彩色频谱图
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(self.times, self.frequencies, self.Zxx, shading='gouraud', cmap='inferno')
        plt.colorbar(label='振幅（mV）')
        plt.title('信号频谱图')
        plt.xlabel('时间 (s)')
        plt.ylabel('频率 (Hz)')
        plt.ylim([0, 120])  # 根据需要调整频率范围
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        base_filename = os.path.join(self.output_path, "STFT")
        file_extension = ".png"
        output_file = base_filename + file_extension
        counter = 1

        while os.path.exists(output_file):
            output_file = f"{base_filename}_{counter}{file_extension}"
            counter += 1
        plt.savefig(output_file)
        return output_file
