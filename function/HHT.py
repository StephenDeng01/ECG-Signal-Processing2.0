"""
这里写希尔伯特-黄变换（HHT）
"""

import numpy as np
from PyEMD import EMD
from scipy.signal import spectrogram
import matplotlib.pyplot as plt


class HHT:
    def __init__(self, signal, fs):
        self.signal = signal
        self.fs = fs

    def hht(self):
        # 进行经验模态分解 (EMD)
        print(self.signal)
        # plt.plot_utils(range(0, len(self.signal)), self.signal)
        emd = EMD()
        imfs = emd(self.signal)
        # 初始化时间向量
        t = np.arange(len(self.signal)) / self.fs

        imfs = list(imfs)
        idx_sum = []
        for idx, i in enumerate(imfs):
            i = list(i)
            smi_on = 0
            s1 = 0
            s1_square = 0
            d = 0
            signal_square = 0
            for j in range(1, len(i)):
                smi_each = i[j - 1] * self.signal[j - 1]
                smi_on += smi_each
            for m in range(1, len(i)):
                s1_each = np.square(i[m - 1])
                s1_square += s1_each
            for n in range(1, len(self.signal)):
                signal_each = np.square(self.signal[n - 1])
                signal_square += signal_each
            S1 = np.sqrt(s1_square)
            S2 = np.sqrt(signal_square)
            d = smi_on / (S1 * S2)
            if d > 0.2:
                idx_sum.append(idx)
            i = np.array(i)
        for idx in sorted(idx_sum, reverse=True):
            del imfs[idx]
        imfs = np.array(imfs)
        print(imfs)
        # 重构信号
        reconstructed_signal = np.sum(imfs, axis=0)
        plt.plot(range(0, len(reconstructed_signal)), reconstructed_signal)
        # 计算频谱图（使用短时傅里叶变换）
        frequencies, times, Sxx = spectrogram(reconstructed_signal, fs=self.fs, nperseg=256, noverlap=128)
        return frequencies, times, Sxx