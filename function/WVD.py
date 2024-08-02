"""
这个文件写威格纳-维尔分布（Wigner-Ville Distribution, WVD）
"""
import numpy as np
from tftb.processing import WignerVilleDistribution


class WVD:
    def __init__(self, signal):
        self.signal = signal

    def WVD(self):
        # 降低分辨率，进行下采样
        downsample_factor = 4
        signal_downsampled = self.signal[::downsample_factor]
        # 创建Wigner-Ville分布对象
        wvd = WignerVilleDistribution(signal_downsampled, time_bandwidth=1.0)
        # 计算WVD
        tfr, t, f = wvd.run()
        tfr = np.abs(tfr)
        return tfr, t, f  # 分别是时间-频率矩阵（时间-频率表示）、时间向量和频率向量