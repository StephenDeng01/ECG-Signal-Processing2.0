"""
这里画wvd变换的matplotlib图像
"""

import os
import matplotlib.pyplot as plt

# 设置绘图大小
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

class WVD_plot:
    def __init__(self, tfr, t, f, fs):
        self.tfr = tfr
        self.t = t
        self.f = f
        self.fs = fs
        # self.output_path = output_path

    def WVD_plot(self):
        # 绘制 WVD 频谱图
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(self.t, self.f, self.tfr, shading='gouraud', cmap='inferno')
        plt.colorbar(label='强度')
        plt.title('WVD 时频图')
        plt.xlabel('时间 (s)')
        plt.ylabel('频率 (Hz)')

        plt.ylim([0, 0.5 * self.fs])  # 根据需要调整频率范围
        # 保存图形到一个临时文件中
        file_path = '.\\plot.png'
        plt.savefig(file_path)

        # 关闭图形以释放内存
        plt.close()

        return file_path

