import numpy as np

import DataAnalysis.barData


def dataoutliers(x):
    data_list = DataAnalysis.barData.bardata_list(x)
    # print(data_list)
    # print(sum(data_list)/len(data_list))

    data_array = np.asarray(data_list, dtype=int)  # 注意：这里要指定 dtype 的类型，否则下面替换时可能会因数据类型不同而导致替换的均值的精度不同

    mean = np.mean(data_array, axis=0)
    std = np.std(data_array, axis=0)

    floor = mean - 3 * std
    upper = mean + 3 * std

    for i, val in enumerate(data_array):
        data_array[i] = float(np.where(((val < floor) | (val > upper)), mean, val))
    data = []
    for i in range(len(data_array)):
        data.append(data_array[i])
    return data
