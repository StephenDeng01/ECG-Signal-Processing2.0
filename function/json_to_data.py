"""
在这里将json文件中的数据提取成易于处理的数据类型
"""

import numpy as np
import json
import os

class JsonToData:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = {}

    def json_to_data(self):
        with open(self.json_file, 'r') as f:
            print(self.json_file)
            self.data = json.load(f)
            real_data_all = self.data['data']
            keys = list(real_data_all.keys())
            for key in keys:
                Y = real_data_all[key]
                Y = Y.split(' ')
                Y_num = []
                for i in Y:
                    i = int(i)
                    i = np.float64(i)
                    Y_num.append(i)
                real_data_all[key] = np.array(Y_num)

            return real_data_all['II']   # 只使用第II维心电信号图
