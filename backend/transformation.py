import copy

def swap(ori_data, ori_key, fd_list):
    res = []
    res_keys = []
    fd_rows = []
    fd_cols = []
    if fd_list is not None:
        for x, y, label in fd_list:
            fd = set([x, y])
            if label=='row':
                fd_rows.append(fd)
            else:
                fd_cols.append(fd)

    # swap index
    # for i in range(len(ori_data.index[0])-1):
    #     for j in range(i+1, len(ori_data.index[0])):
    for i in range(len(ori_key[0])-1):
        for j in range(i+1, len(ori_key[0])):
            idx_key = copy.deepcopy(ori_key[0])
            if set([idx_key[i], idx_key[j]]) in fd_rows:  # ignore when swap between headers having fds
                continue
            tmp = idx_key[i]
            idx_key[i] = idx_key[j]
            idx_key[j] = tmp
            new_key = [idx_key, ori_key[1]]
            data = ori_data.swaplevel(i=i, j=j, axis=0).sort_index()
            res.append(data)
            res_keys.append(new_key)
    # swap column
    # for i in range(len(ori_data.columns[0])-1):
    #     for j in range(i+1, len(ori_data.columns[0])):
    for i in range(len(ori_key[1])-1):
        for j in range(i+1, len(ori_key[1])):
            data = ori_data.swaplevel(i=i, j=j, axis=1).sort_index(axis=1)
            col_key = copy.deepcopy(ori_key[1])
            tmp = col_key[i]
            col_key[i] = col_key[j]
            col_key[j] = tmp
            new_key = [ori_key[0], col_key]
            res.append(data)
            res_keys.append(new_key)
    return res, res_keys

def transpose(ori_data, ori_key, func_depends):
    res = []
    res_keys = []

    # column -> index
    if len(ori_key[1]) > 1:
        for i in range(len(ori_key[1])):
            data = ori_data.stack(i)
            if data.isna().any().any():
                continue    # ignore when having NaN
            idx_key = copy.deepcopy(ori_key[0])
            col_key = copy.deepcopy(ori_key[1])
            idx_key.append(col_key[i])
            del col_key[i]
            new_key = [idx_key, col_key]
            res.append(data)
            res_keys.append(new_key)

    # index -> column
    if len(ori_key[0]) > 1:
        for i in range(len(ori_key[0])):
            data = ori_data.unstack(i)
            if data.isna().any().any():
                continue    # ignore when having NaN
            idx_key = copy.deepcopy(ori_key[0])
            col_key = copy.deepcopy(ori_key[1])
            col_key.append(idx_key[i])
            del idx_key[i]
            new_key = [idx_key, col_key]
            res.append(data)
            res_keys.append(new_key)
    
    return res, res_keys