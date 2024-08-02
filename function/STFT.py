"""
这里写短时傅里叶变换的模块
"""

import numpy as np
from scipy.signal import stft


class STFT:
    def __init__(self, signal, fs):
        self.signal = signal
        self.fs = fs

    def stft_use(self):
        # 窗口长度
        nperseg = 256
        # 计算STFT
        frequencies, times, Zxx = stft(self.signal, fs=self.fs, nperseg=nperseg)
        Zxx = np.abs(Zxx)
        return frequencies, times, Zxx   # 频率向量（frequencies）、时间向量（times）和复数数组（Zxx）