import numpy as np
import pandas as pd
import heapq
import copy
from insightCalculator import check_is_temporal, calc_outlier, calc_outlier_temporal,calc_point_insight, calc_shape_insight, calc_compound_insight, calc_distribution_insight

month2letter = {'JAN':'a', 'FEB':'b', 'MAR':'c', 'APR':'d', 'MAY':'e', 'JUN':'f', 'JUL':'g', 'AUG':'h', 'SEP':'i', 'OCT':'j', 'NOV':'k', 'DEC':'l'}
letter2month = {'a':'JAN', 'b':'FEB', 'c':'MAR', 'd':'APR', 'e':'MAY', 'f':'JUN', 'g':'JUL', 'h':'AUG', 'i':'SEP', 'j':'OCT', 'k':'NOV', 'l':'DEC'}

class Insight:
    def __init__(self, scope_data, breakdown=None, aggregate=None):
        self.scope_data = scope_data
        self.breakdown = breakdown  # the column index of the breakdown in block_data
        self.aggregate = aggregate  # the aggregate function to generate scope data
        
        self.type = None
        self.score = None
        self.category = None
    
    def __lt__(self, other):
        return self.score < other.score

def get_insight(header, block_data, header_split, transformed_state):
    aggregate = 'sum'
    global block_insight  # record the insights for the current block
    block_insight = {'point': [], 'shape': [], 'compound':[]}  # contains three types of insight

    # consider part of the data when transformed TODO not finished
    # if transformed_state != 0:
    #     # index header not none, column header not none
    #     if header_split!=0 and header_split!=block_data.shape[1]-1:
    #         # only consider the first layer of headers as breakdown and aggregate 
    #         get_scope_with_aggregate(block_data, 0, aggregate) # index header
    #         get_scope_with_aggregate(block_data, header_split, aggregate) # column header 

    # else:
    # if transformed_state != 0:
    #     idx, col = header
    #     # skip when block is a whole row or column
    #     if idx==() or col==():
    #         return block_insight

    # change categorical to string
    for col in block_data.columns:
        if pd.api.types.is_categorical_dtype(block_data[col]):
            block_data[col] = block_data[col].astype(str)
   
    # no breakdown, consider all data together
    get_scope_no_breakdown(block_data)
    # index header not none, column header not none(the scope includes more than one row or column )
    if header_split!=0 and header_split!=block_data.shape[1]-1:
        # only consider the first layer of headers as breakdown and aggregate 
        get_scope_with_aggregate(block_data, 0, aggregate) # index header
        get_scope_with_aggregate(block_data, header_split, aggregate) # column header
        # consider all layers and generate groups, no aggregate, compound insights
        if transformed_state == 0:
            get_scope_rearrange(header, block_data, header_split)

    return block_insight

def merge_columns(block_data, start, end, name='Merged'):
    data = copy.deepcopy(block_data)    
    merged_col = data.iloc[:, start:end].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
    merged_col.name = name
    res = pd.concat([data.iloc[:, :start], merged_col, data.iloc[:, end:]], axis=1)

    return res

def get_scope_no_breakdown(block_data):
    scope_data = None
    # merge the first [merge_num] columns as the breakdown column
    merge_num = block_data.shape[1] - 1 
    scope_data = merge_columns(block_data, 0, merge_num)
    # merged_column = block_data.iloc[:, :merge_num].apply(lambda x: ' - '.join(x.astype(str)), axis=1)
    # scope_data = pd.concat([merged_column, block_data.iloc[:, merge_num]], axis=1)

    # set the breakdown column as index
    scope_data = scope_data.set_index(scope_data.columns[0])
    scope_data = scope_data[scope_data.columns[0]]  # turn the dataframe to series
    calc_insight(scope_data, None, None, True)

def get_scope_with_aggregate(block_data, breakdown, aggregate):
    scope_data = block_data.groupby(block_data.columns[breakdown]).agg(aggregate)  
    # remove other columns except the aggregate column
    scope_data = scope_data.iloc[:, -1].apply(lambda x: round(x, 2))  
    if scope_data.index.__contains__('MAR'):    #trick to sort months
        # record the origin order
        scope_data.index = scope_data.index.to_series().replace(month2letter, regex=True)
        # sort the data by origin order
        scope_data = scope_data.sort_index()
        # change back to the origin name
        scope_data.index = scope_data.index.to_series().replace(letter2month, regex=True)
    calc_insight(scope_data, breakdown, aggregate)

def get_scope_rearrange_old(header, block_data, header_split):
    scope_data = copy.deepcopy(block_data)
    # concat row and column headers to one level if needed
    if block_data.shape[1]-1 - header_split > 1: 
        scope_data = merge_columns(scope_data, header_split, block_data.shape[1]-1,'Merged_col')
    if header_split > 1:
        scope_data = merge_columns(scope_data, 0, header_split, 'Merged_idx')
    
    # group by columns 
    scope_data.set_index(scope_data.columns[0], inplace=True)
    scope_data = scope_data.pivot(columns=scope_data.columns[0], values=scope_data.columns[-1])
    get_scope_rearrange_more(scope_data)
    
    # group by rows
    scope_data = scope_data.T
    if check_is_temporal(scope_data):
        # for temporal data, record the origin order
        scope_data.index = scope_data.index.to_series().replace(month2letter, regex=True)
        # sort the data by origin order
        scope_data = scope_data.sort_index()
        # change back to the origin name
        scope_data.index = scope_data.index.to_series().replace(letter2month, regex=True)
    get_scope_rearrange_more(scope_data)

def get_scope_rearrange(header, block_data, header_split):
    origin_data = copy.deepcopy(block_data)
    # in order to avoid repated calculation inside groups
    # group by columns
    header_col_name = origin_data.columns[header_split]
    get_scope_rearrange_advanced(origin_data, header_col_name, header_split, 0, 1)
    # group by rows
    header_row_name = origin_data.columns[0]
    get_scope_rearrange_advanced(origin_data, header_row_name, header_split, 1, 0)

def get_scope_rearrange_advanced(origin_data, header_name, header_split, idx_num, col_num):
    grouped_data = dict(list(origin_data.groupby(header_name))).values()
    grouped_data_processed = []
    for g_data in grouped_data:
        if g_data.shape[1]-1 - header_split > 1:    # many col headers, concat them
            g_data = merge_columns(g_data, header_split, origin_data.shape[1]-1, 'Merged_col')
        if header_split > 1:    # many row headers, concat them
            g_data = merge_columns(g_data, 0, header_split, 'Merged_idx')
        g_data = g_data.pivot(
            index=g_data.columns[idx_num], 
            columns=g_data.columns[col_num], 
            values=g_data.columns[-1]
        )
        if check_is_temporal(g_data):
            # for temporal data, record the origin order
            g_data.index = g_data.index.to_series().replace(month2letter, regex=True)
            # sort the data by origin order
            g_data = g_data.sort_index()
            # change back to the origin name
            g_data.index = g_data.index.to_series().replace(letter2month, regex=True)
        grouped_data_processed.append(g_data)
    tmp_corr_list = []
    tmp_scope_list = []
    tmp_score = float('inf')
    for i in range(len(grouped_data_processed)-1):
        for k in range(len(grouped_data_processed[i].columns)):
            tmp_corr_vars = [(i, k)]
            scope_data = grouped_data_processed[i].iloc[:,k]
            for j in range(i+1, len(grouped_data_processed)):
                for l in range(len(grouped_data_processed[j].columns)):
                    scope_data_subset = pd.concat([grouped_data_processed[i].iloc[:,k], grouped_data_processed[j].iloc[:,l]], axis=1)
                    ins_type, ins_score = calc_compound_insight(scope_data_subset)
        
                    if ins_type=='correlation-temporal':  # only merge when temporal data
                        tmp_corr_vars.append((j, l))
                        tmp_score = min(tmp_score, ins_score)
                        scope_data = pd.concat([scope_data, grouped_data_processed[j].iloc[:,l]], axis=1)
                    elif ins_type=='correlation':    # no merge, directly save the insight
                        save_insight(scope_data_subset, 'compound', ins_type, ins_score)
            if len(tmp_corr_vars) > 1:
                tmp_corr_list.append(tmp_corr_vars)
                tmp_scope_list.append(scope_data)
    if len(tmp_corr_list) > 0:
        # tmp_list = merge_lists_with_common_element(tmp_list)
        # TODO simply pick the longest list, may cause problems
        scope_data = max(tmp_scope_list, key=len)
        save_insight(scope_data, 'compound', 'correlation-temporal', tmp_score)
            
def save_insight(scope_data, ins_category, ins_type, ins_score, breakdown=None, aggregate=None):
    insight = Insight(scope_data, breakdown, aggregate)
    insight.type = ins_type
    insight.score = ins_score
    insight.category = ins_category

    # # keep the top1 insight for each category
    # if block_insight[ins_category] is None:
    #     block_insight[ins_category] = insight
    # elif block_insight[ins_category].score < insight.score:
    #     block_insight[ins_category] = insight

    # keep_top_k(ins_category, insight, 3)
    block_insight[ins_category].append(insight)
    # sort the insight list
    # if len(block_insight[ins_category]) > 1:
    #     block_insight[ins_category].sort(key=lambda x: x.score, reverse=True)

def get_scope_rearrange_more(d):
    for i in range(len(d.columns)):
        for j in range(i+1, len(d.columns)):
            scope_data = pd.concat([d.iloc[:,i], d.iloc[:,j]], axis=1)
            calc_insight(scope_data, None, 'compound')

def calc_insight(scope_data, breakdown, aggregate, no_aggreate=False):
    ins_type = ''
    ins_score = 0
    if check_is_temporal(scope_data):
        ins_type, ins_score = calc_shape_insight(scope_data)
        if ins_score>0:
            save_insight(scope_data, 'shape', ins_type, ins_score, breakdown, aggregate)
        ins_type, ins_score = calc_outlier_temporal(scope_data)
        if ins_score>0:
            save_insight(scope_data, 'point', ins_type, ins_score, breakdown, aggregate)
    else:
        ins_type, ins_score = calc_point_insight(scope_data, no_aggreate)
        if ins_score>0:
            save_insight(scope_data, 'point', ins_type, ins_score, breakdown, aggregate)
        ins_type, ins_score = calc_outlier(scope_data)
        if ins_score>0:
            save_insight(scope_data, 'point', ins_type, ins_score, breakdown, aggregate)
        
        scope_data = scope_data[scope_data != 0] # remove all zeros when calculating distribution insight
        ins_type, ins_score = calc_distribution_insight(scope_data)
        if ins_score>0: 
            save_insight(scope_data, 'shape', ins_type, ins_score, breakdown, aggregate)
        

def keep_top_k(category, insight, k=3):
    heapq.heappush(block_insight[category], insight)  # add the new insight element
    if len(block_insight[category]) > k:
        heapq.heappop(block_insight[category])  # pop the smallest element
    
def merge_lists_with_common_element(lists):
    merged_lists = []
    for new_list in lists:
        merged = False
        for old_list in merged_lists:
            if set(new_list).intersection(set(old_list)):
                old_list.extend(new_list)
                merged = True
                break
        if not merged:
            merged_lists.append(new_list)
    return merged_lists
