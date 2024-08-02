"""
这里写小波分析
"""

import numpy as np
import pywt


class CWT:
    def __init__(self, signal, fs):
        self.signal = signal
        self.fs = fs

    def cwt(self):
        # 定义小波函数和尺度范围
        wavelet = 'cmor1.5-1.0'  # 使用复 Morlet 小波,分析ECG信号比较好
        scales = np.arange(1, 128)  # 定义尺度范围
        # 计算CWT
        coefficients, frequencies = pywt.cwt(self.signal, scales, wavelet, sampling_period=1 / self.fs)
        return coefficients, frequencies