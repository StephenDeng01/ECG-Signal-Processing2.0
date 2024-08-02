"""
这里画wvd变换的matplotlib图像
"""

import os
import matplotlib.pyplot as plt

# 设置绘图大小
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class WVD_plot:
    def __init__(self, tfr, t, f, fs, output_path):
        self.tfr = tfr
        self.t = t
        self.f = f
        self.fs = fs
        self.output_path = output_path

    def WVD_plot(self):
        # 绘制 WVD 频谱图
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(self.t, self.f, self.tfr, shading='gouraud', cmap='inferno')
        plt.colorbar(label='强度')
        plt.title('WVD 时频图')
        plt.xlabel('时间 (s)')
        plt.ylabel('频率 (Hz)')

        plt.ylim([0, 0.5 * self.fs])  # 根据需要调整频率范围
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        base_filename = os.path.join(self.output_path, "WVD")
        file_extension = ".png"
        output_file = base_filename + file_extension
        counter = 1

        while os.path.exists(output_file):
            output_file = f"{base_filename}_{counter}{file_extension}"
            counter += 1
        plt.savefig(output_file)
        return output_file
