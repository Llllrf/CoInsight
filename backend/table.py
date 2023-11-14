import pandas as pd
import json
import time, os
import multiprocessing as mp
from itertools import groupby
from insight import get_insight
from visualization import get_visualization
from graph import get_node, get_links, get_state_links, get_id
from read_json import generate_txt
from transformation import swap, transpose
from tableJsonGenerator import get_table_json

class HierarchicalTable:
    def __init__(self, data_source):
        self.data_source = data_source  
        self.origin_data = pd.read_excel(data_source.source_path, header=data_source.header_row, index_col=data_source.index_col).fillna(0)
        self.process_origin_data()
        self.all_nodes = None
        self.all_links = None
        self.block_with_insight = None
        self.curr_focus = 0
        self.curr_key = self.get_state_key(self.origin_data)
        self.curr_focus_all_state = None
        self.all_state = [self.origin_data]
        self.all_state_keys = [self.curr_key]
        self.func_depends = self.get_func_dependency(data_source.func_depends)
    
    def process_origin_data(self):
        # warning!!!! only when columns having MAR JUN SEP DEC
        # keep the order of indexes and columns (only columns having MAR JUN SEP DEC)
        df = self.origin_data
        if df.columns[0][1] != 'MAR':
            return
        order = pd.Categorical(df.columns.get_level_values(1).unique(), categories=df.columns.get_level_values(1).unique(), ordered=True)
        df.columns= pd.MultiIndex.from_product([df.columns.get_level_values(0).unique(), order])

    def generate_all_results(self):
        s_time = time.time()

        curr_data = self.all_state[self.curr_focus]
        curr_key = self.all_state_keys[self.curr_focus]
        self.curr_focus_all_state = [curr_data]
        
        # get transformations
        transform_func_list = [swap,transpose]
        for func in transform_func_list:
            # res, res_keys = func(self.origin_data, curr_key, self.data_source.func_depends)
            res, res_keys = func(curr_data, curr_key, self.data_source.func_depends)

            # remove common dataframes if they are already in all_state
            res, res_keys = remove_common_elements(res_keys, self.all_state_keys, res) 
            self.curr_focus_all_state.extend(res)
            self.all_state_keys.extend(res_keys)
            
        self.generate_blocks()
        self.generate_links()
        
        graph = self.generate_graph()
        table = self.generate_table_json(curr_data, graph)
        state_links = self.state_links

        result = {}
        result['table'] = table
        result['graph'] = graph
        result['state_links'] = state_links
        
        filepath = self.data_source.get_result_path(self.curr_focus)
        with open(filepath, mode='w') as f:
            json.dump(result, f)  
        
        print('done!')
        e_time = time.time()
        print('time cost: ', e_time - s_time)

        # just for test
        # generate_txt(filepath)
        return result
    
    def generate_blocks(self):
        self.all_nodes = []
        self.block_with_insight = []
        args_list = []
        curr_focus_headers = []
        for i in range(len(self.curr_focus_all_state)):
            src_data = self.curr_focus_all_state[i]
            transformed_state = i
            columns = src_data.columns.tolist()
            index = src_data.index.tolist()
            all_columns = self.generate_all_headers(columns)
            all_index = self.generate_all_headers(index)
            
            for idx in all_index:
                for col in all_columns:
                    idx_cond = len(idx)==len(src_data.index[0]) or \
                        (len(idx)==1 and type(src_data.index[0])!=tuple)
                    col_cond = len(col)==len(src_data.columns[0]) or \
                        (len(col)==1 and type(src_data.columns[0])!=tuple)
                    if idx_cond and col_cond:                    
                        continue    # skip the singel cell
                    if len(idx) == 0 and len(col) == 0:
                        continue    # skip the whole table
                    
                    
                    # record the scope in curr focus state
                    if i==0:
                        header = set(idx+col)   # generate a set using idx and col
                        curr_focus_headers.append(header)  
                        args = (idx, col, src_data, transformed_state, None)            
                    else:
                        args = (idx, col, src_data, transformed_state, curr_focus_headers)
                    # record the arguments of the block_processing function                     
                    args_list.append(args)
                    
        print('processing blocks...')
        pool = mp.Pool(mp.cpu_count())
        # multi-processing
        res_list = pool.map(self.process_block, args_list)
        for node, args in zip(res_list, args_list):
            if node != None:
                idx, col, _, state, _ = args
                # if set(idx+col) in curr_focus_headers:
                #     continue
                self.all_nodes.append(node)
                global_state = self.get_global_state_num(state)
                # save the block with insight, used for link generation
                self.block_with_insight.append((idx, col, global_state))   
        pool.close()
        pool.join()

        # save the state-data and state-keys
        self.all_state.extend(self.curr_focus_all_state[1:])  # the first state must have been recorded
        # self.all_state_keys.extend(self.)
        
        # Normalization of the insight score 
        
    def process_block(self, args):
        s_time = time.time()
        idx, col, src_data, transformed_state, curr_focus_headers = args
        if transformed_state!=0:    # not curr_state, do not re-calculate same scope insight
            header_set = set(idx+col)
            if header_set in curr_focus_headers:
                return None
            elif self.func_depends is not None:   # extend header_set when having func_depends
                extended_header = extend_header(header_set, self.func_depends)
                if extended_header in curr_focus_headers:
                    return None
    
        header = (idx, col)
        block_data = self.get_block_data(src_data, idx, col)
        # calculate the split of column and row headers in a block data
        header_split = len(src_data.index[0]) - len(idx)    
        insight_list = get_insight(header, block_data, header_split, transformed_state)
        # self.block_insight[header] = insight_list   # save the insight of the block
        vis_list = get_visualization(insight_list)
        # self.block_vis[header] = vis_list   # save the visulization of the block  
        node = None
        if vis_list != []:
            global_state = self.get_global_state_num(transformed_state)
            node = get_node(idx, col, vis_list, global_state)
        # print('node complete!')
        e_time = time.time()
        # print('state:', transformed_state, '    block:', idx, col, '    shape:', block_data.shape,'    time:', e_time - s_time)
        return node
    
    def generate_links(self):
        print('processing links...')
        blocks = self.block_with_insight
        grouped_blocks = groupby(blocks, key=lambda x: x[-1])
        # all_blocks = [list(group) for key, group in grouped_blocks]
        all_blocks = []
        for key, group in grouped_blocks:
            grp_list = list(group)
            all_blocks.append((key, grp_list))
        self.all_links = get_links(all_blocks)
        self.state_links = get_state_links(all_blocks)

    def generate_graph(self):
        # generate result json
        graph = {}
        graph['nodes'] = self.all_nodes
        graph['links'] = self.all_links
        return graph

    def generate_table_json(self, df, graph):
        filepath = self.data_source.get_state_data_path(self.curr_focus) 
        df.to_excel(filepath)   # to help get table json
        del_row = len(df.columns[0])+1
        table = get_table_json(filepath, del_row, graph, 'S'+str(self.curr_focus))
        if os.path.exists(filepath):    # remove the generated xlsx file
            os.remove(filepath)
        return table

    def get_block_data(self, src_data, idx, col):
        '''
        get the data of a block from origin data and convert it to flat table
        idx is the index of the block, e.g. ('Nintendo', '3DS')
        col is the column of the block, e.g. ('2011', 'JUN')
        '''
        # get block data from origin data
        block = None
        if len(idx)==0:
            block = src_data.sort_index().loc[:, col] 
        elif len(col)==0:
            block = src_data.sort_index().loc[idx, :] 
        else:
            block = src_data.sort_index().loc[idx, col] 
        res = None
        if isinstance(block, pd.Series):
            res = block.to_frame()   # convert to dataframe
            res.columns = ['value']   # set column name
            res = res.reset_index() # convert to flat table
        elif block.shape[1]==1:
            res = block.reset_index()
        else:
            res = block.melt(ignore_index=False).reset_index() # convert to flat table

        # # get the length of the original header
        # origin_col_len = len(self.origin_data.columns[0]) 
        # origin_idx_len = len(self.origin_data.index[0])
        # # if the header is from a higher level, add the higher level header to the flat table
        # if len(idx) < origin_idx_len:
        #     for i in range(len(idx)):
        #         res.insert(i, 'idx'+str(i), idx[i])
        # if len(col) < origin_col_len:
        #     for i in range(len(col)):
        #         res.insert(origin_idx_len+i, 'col'+str(i), col[i])

        # with open('data/all_block.csv', mode='a') as f:
        #     f.write(''+str(idx)+str(col)+'\n')
        #     res.to_csv(f, index=False)
        return res
    
    def generate_all_headers(self, header_list):
        res = [()] 
        for i in range(len(header_list)):
            header = header_list[i]
            if type(header) == tuple:
                for j in range(1, len(header)):
                    new_header = header[:j]
                    if new_header not in res:   # avoid duplicate
                        res.append(new_header)
            else:   # header is a list
                header_list[i] = (header,)
        res.extend(header_list)
        return list(res)

    def change_current_state(self, new_state):
        self.curr_focus = new_state
        
        # if the state has already been calculated, return the result directly
        # if self.get_state_data(new_state):
        #     return self.get_state_data(new_state)
        # else:

        result = self.generate_all_results()    
        return result

    def get_global_state_num(self, transformed_state):
        if transformed_state == 0:  # current focus state
            state = self.curr_focus
        else:
            state = transformed_state + len(self.all_state) - 1
        return state

    def get_state_key(self, df):
        # get the key of a dataframe, using the node_id of the first item
        idx = [i for i in range(len(df.index[0]))]
        col = [i for i in range(len(df.index[0]),len(df.index[0])+len(df.columns[0]))]
        id = [idx, col]
        return id
    
    def get_func_dependency(self, fd_list): # get each domain and range pair for function dependencies
        if fd_list is None:
            return None
        res = {}
        for x, y, label in fd_list:
            if label=='row':
                headers = self.origin_data.index
            else:
                headers = self.origin_data.columns
            for header in headers:
                h_domain = header[x]
                h_range = header[y]
                res[h_domain] = h_range
        return res
    
    def get_state_data(self, num):
        tablename = self.data_source.source_name
        filepath = os.path.join('results', tablename+'_S'+str(num)+'.json')
        if os.path.isfile(filepath):
            with open(filepath, mode='r') as f:
                result = json.load(f)
            return result
        else:
            return None
            

def remove_common_elements(curr_keys, all_keys, curr_data):
    res = []
    res_keys = []
    for key, df in zip(curr_keys, curr_data):
        if key in all_keys:
            continue
        res.append(df)
        res_keys.append(key)
    return res, res_keys

def extend_header(key, func_depends):
    res = []
    for k in key:
        res.append(k)
        if k in func_depends:
            res.append(func_depends[k])
            
    return set(res)
        
            