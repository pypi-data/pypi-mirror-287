import numpy as np
import pickle

def useing_pkl(pklfile):
    with open(pklfile, 'rb') as file:
        loaded_diff = pickle.load(file)

    # 提取字典中的所有值
    values = list(loaded_diff.values())
    data = np.array(values)
    # 计算累积频率分布（CDF）
    sorted_data = np.sort(data)
    cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

    # 计算CDF的一阶导数（密度函数）
    density = np.diff(cdf) / np.diff(sorted_data)

    # 找到变化最大的地方
    max_change_index = np.argmax(density)
    max_change_value = sorted_data[max_change_index]
    bin_index = np.digitize(max_change_value, bin_edges) - 1
    frequency = hist[bin_index]

    def modify_frequency_percentage(frequency, hist):
        total_count = np.sum(hist)
        target_frequency = int(total_count * 0.05)
        if frequency > target_frequency:
            for i in range(len(hist)):
                if hist[i] > 0 and hist[i] >= frequency - target_frequency:
                    hist[i] -= (frequency - target_frequency)
                    break
            frequency = target_frequency
        return frequency

    frequency = modify_frequency_percentage(frequency, hist)
    frequency_percentage = (frequency / np.sum(hist)) * 100
    fg = frequency_percentage - 0.001
    freque_pe = abs(frequency_percentage - fg)
    return freque_pe
