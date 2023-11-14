import numpy as np
import pandas as pd
from scipy.stats import linregress, pearsonr, skewtest, kurtosistest, skew, kurtosis, zscore, kstest

def calc_point_insight(d, no_aggr):
    # TODO check if non-negative
    ins_type = ''
    ins_score = 0
    if len(d) < 3 or np.sum(d) == 0 or np.std(d) == 0 or no_aggr:
        return ins_type, ins_score  # too few data or all zero
    
    sorted_d = np.sort(d)[::-1]    
    if dominance_detection(sorted_d):
        ins_type = 'dominance'
        ins_score = sorted_d[0]/np.sum(d)
    elif top2_detection(sorted_d):
        ins_type = 'top2'
        ins_score = sorted_d[0]/np.sum(d)
    return ins_type, ins_score

    # dominance = dominance_detection(d)
    # top1, top2 = top2_detection(d)
    # if top1 > 0.34 and top2 > 0.23:
    #     ins_type = 'top2'
    #     ins_score = top2
    # elif dominance > 0.5 and dominance < 1:
    #     ins_type = 'dominance'
    #     ins_score = dominance
    # else: 
    #     outlier = z_score_outlier_detection(d)
    #     if len(outlier) == 0:
    #         if not np.all(d == 0) and np.std(d) < 0.5*np.mean(d) and len(d) > 5 and np.std(d) > 0:
    #             # not all zero and std is relatively small and length is long enough
    #             ins_type = 'evenness'
    #             ins_score = np.mean(d) / np.std(d)

    #     elif len(outlier) == 1:
    #             ins_type = 'outlier'
    #             ins_score = (d.max()-d.mean())/d.std()
    
    # return ins_type, ins_score

def calc_outlier(d):
    ins_type = ''
    ins_score = 0
    if len(d) < 8 or np.sum(d) == 0 or np.std(d) == 0:
        return ins_type, ins_score  # too few data or all zero
    sorted_d = np.sort(d)[::-1] 
    if outlier_detection(d, 2):
        ins_type = 'outlier'
        # max_score = outlier_score(sorted_d[0], d)
        # min_score = outlier_score(sorted_d[-1], d)
        # ins_score = max_score if max_score > min_score else min_score
        ins_score = (sorted_d[0]-sorted_d.mean())/sorted_d.std()
    return ins_type, ins_score

def calc_outlier_temporal(d):
    ins_type = ''
    ins_score = 0
    if len(d) < 5 or np.sum(d) == 0 or np.std(d) == 0:
        return ins_type, ins_score  # too few data or all zero
    sorted_d = np.sort(d)[::-1] 
    if outlier_detection(d, 1.5):
        ins_type = 'outlier-temporal'
        # max_score = outlier_score(sorted_d[0], d)
        # min_score = outlier_score(sorted_d[-1], d)
        # ins_score = max_score if max_score > min_score else min_score
        ins_score = (sorted_d[0]-sorted_d.mean())/sorted_d.std()
    return ins_type, ins_score

def dominance_detection(d):
    if (d < 0).any():   # ignore when having negative values
        return False
    # d is already sorted descending
    zero_count = np.sum(d==0)
    sum_d = np.sum(d)
    if d[0]/sum_d > 0.5 and d[0]/sum_d < 1 and d[1]/sum_d < 0.3 and len(d)-zero_count >= 3:
        return True
    else:
        return False

def top2_detection(d):
    if (d < 0).any():   # ignore when having negative values
        return False
    # d is already sorted descending
    zero_count = np.sum(d==0)
    sum_d = np.sum(d)
    if d[0]/sum_d > 0.3 and d[1]/sum_d > 0.3 and d[2]/sum_d < 0.3 and len(d)-zero_count >= 3:
        return True
    else:
        return False

def outlier_detection(d, threshold=3):
    zero_count = np.sum(d==0)
    if check_zero(d) > 0.1 or len(d)-zero_count < 4:   # too many zeros
        return False
    # d = d[d != 0]   # remove zero
    Q1 = d.quantile(0.25)
    Q3 = d.quantile(0.75)
    IQR = Q3 - Q1
    lower_threshold = Q1 - threshold * IQR
    upper_threshold = Q3 + threshold * IQR
    outliers = d[(d < lower_threshold) | (d > upper_threshold)]
    if len(outliers) != 0 and len(outliers) < 3:
        return True
    else:
        return False

def z_score_outlier_detection(data, threshold=3.5):
    """
    使用Z-score方法进行离群值检测
    :param data: 数据集
    :param threshold: Z-score阈值，默认为3
    :return: 离群值的索引
    """
    mean = np.mean(data)
    std = np.std(data)
    if std == 0:
        return []
    else:
        z_scores = [(x - mean) / std for x in data]
        return np.where(np.abs(z_scores) > threshold)[0]

def calc_shape_insight(d):
    ins_type = ''
    ins_score = 0
    trend = test_slope(d)
    if trend > 0.7:
        ins_score = trend
        ins_type = 'trend'
        # print("data\n", d, "\n", ins_type, ins_score)

    return ins_type, ins_score

def test_slope(d):
    if np.std(d) == 0: # all the same, no slope
        return 0
    # Fit X to a line by linear regression
    _, _, r_value, p_value, _ = linregress(np.arange(len(d)), d)
    trend = r_value ** 2 * (1 - p_value) 
    return trend
    # # Calculate the p-value
    # n = len(d)
    # t_statistic = slope / (np.std(d) / np.sqrt(n))
    # degrees_of_freedom = n - 2
    # p_value = 2 * (1 - t.cdf(abs(t_statistic), df=degrees_of_freedom))

def check_is_temporal(data):  
    # a really naive way to check temporal
    if len(data.index[0]) < 4:
        return False
    eg_index = str(data.index[0])[:4]
    if eg_index.isdigit():
        if int(eg_index) >=1800 and int(eg_index)<=2300 and len(data.index[0]) <= 10:
            return True
        else:
            return False
    else:
        return False

def check_zero(d):
    return np.sum(d==0) / len(d)

def calc_compound_insight(d):
    ins_type = ''
    ins_score = 0
    if d.shape[0] <= 10 or (d.shape[0] <= 20 and not check_is_temporal(d)):
        return ins_type, ins_score # too few data
    if check_zero(d.iloc[:,0]) > 0.5 or check_zero(d.iloc[:,1]) > 0.5:
        return ins_type, ins_score # too many zero
    corr, p_value = correlation_detection(d.iloc[:,0], d.iloc[:,1])
    score = corr ** 2 * (1 - p_value)
    # if check_is_temporal(d):
    #     if abs(corr) > 0.7 and p_value < 0.05:
    #         ins_score = abs(corr)
    #         ins_type = 'correlation-temporal' 
    # else:   # different threshold for non-temporal data
    #     if abs(corr) > 0.75 and p_value < 0.05:
    #         ins_score = abs(corr)
    #         ins_type = 'correlation'
    if score > 0.7:
        ins_type = 'correlation-temporal' if check_is_temporal(d) else 'correlation'
        ins_score = score

    return ins_type, ins_score

def correlation_detection(x, y):
    if len(np.unique(x)) > 1 and len(np.unique(y)) > 1:
        corr_coef, p_value = pearsonr(x, y) 
    else:
        corr_coef = 0
        p_value = 1
    return corr_coef, p_value

def calc_distribution_insight(d):
    if d.shape[0] <= 20:
        return '', 0
    ins_type = ''
    ins_score = 0
    _, p_s = skewtest(d)
    s = skew(d)
    _, p_k = kurtosistest(d)
    k = kurtosis(d)
    # e = abs(d.std() / d.mean())         # evenness
    _, p_e = kstest(d, 'uniform', args=(0, 1))
    has_skew = p_s < 0.03 and abs(s) > 2
    has_kurtosis = p_k < 0.05 and abs(k) > 3 and abs(s) < 3
    has_evenness = p_e > 0.01
    
    if has_skew and has_kurtosis:
        ins_type = 'skewness' if p_s < p_k else 'kurtosis'
        ins_score = (1-p_s) * abs(s) if p_s < p_k else (1-p_k) * abs(k)
    elif has_skew:
        ins_type = 'skewness'
        ins_score = (1-p_s) * abs(s)
    elif has_kurtosis:
        ins_type = 'kurtosis'
        ins_score = (1-p_k) * abs(k)
    elif has_evenness:
        ins_type = 'evenness'
        ins_score = p_e
    return ins_type, ins_score

    
    # if abs(s) >= thres_s and abs(k) < thres_k:
    #     return 'skewness', abs(s)/10
    # elif abs(s) < thres_s and abs(k) >= thres_k:
    #     return 'kurtosis', abs(k)/10
    # else:
    #     return '', 0

def outlier_score(data_point, data):
    z_scores = zscore(data)
    min_z = np.min(z_scores)
    max_z = np.max(z_scores)
    outlier_score = (data_point - min_z) / (max_z - min_z)
    return outlier_score


