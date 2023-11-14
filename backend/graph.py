def get_node(idx, col, vis_list, state):
    id = get_id(idx, col, state)
    idx2str = "_".join(str(item) for item in idx) if len(idx)!=0 else '_'
    col2str = "_".join(str(item) for item in col) if len(col)!=0 else '_'
    ins_list = []
    for vis in vis_list:
        ins_list.append({
            'insight-type': vis.insight_type,
            'insight-category':vis.insight_category,
            'insight-score': vis.insight_score,
            'vega-lite': vis.vega_json})
    
    node = {'id': id, 
            'row': idx2str,
            'col': col2str,
            'insight-list': ins_list,
            'state': 'S'+str(state)}
    return node

def get_links(block_list):
    links = []
    for state in range(len(block_list)):
        s_num, blocks = block_list[state]
        for i in range(len(blocks)-1):
            for j in range(i+1, len(blocks)):
                block1 = blocks[i]
                block2 = blocks[j]
                link = get_link_between_blocks(block1, block2, s_num)
                if link != None:
                    links.append(link)
    return links

def get_link_between_blocks(block1, block2, state):
    link = None
    row1 = block1[0]
    row2 = block2[0]
    col1 = block1[1]
    col2 = block2[1]
    id1 = get_id(row1, col1, state)
    id2 = get_id(row2, col2, state)

    if row1!=row2 and col1!=col2:
        return None
    if row1==row2:
        link_type, reverse = get_relation(col1, col2)
    elif col1==col2:
        link_type, reverse = get_relation(row1, row2)
    
    if link_type == 'parent':
        if reverse:
            link = {'source': id2, 'target': id1, 'type': link_type}
        else:
            link = {'source': id1, 'target': id2, 'type': link_type}
    elif link_type != None:
        link = {'source': id1, 'target': id2, 'type': link_type}

    return link

def get_relation(header1, header2):
    link_type = None
    reverse = False

    # same layer
    if len(header1) == len(header2):
        link_type = check_siblings(header1, header2)

    # parent-child relation
    elif len(header2) - len(header1) == 1:
        # header1 is the parent
        link_type = 'parent-child' if check_if_parent(header1, header2) else None
        reverse = False
    elif len(header1) - len(header2) == 1:
        # header2 is the parent
        link_type = 'parent-child' if check_if_parent(header2, header1) else None
        reverse = True
    return link_type, reverse

def get_state_links(block_list):
    links = {}
    curr_s, curr_list = block_list[0]   # first is the current state
    for i in range(len(curr_list)):
        block1 = curr_list[i]
        row1 = block1[0]
        col1 = block1[1]
        id1 = get_id(row1, col1, curr_s)
        curr_block_link = {}
        for s in range(1, len(block_list)): # iterate all other states
            state, other_list = block_list[s]
            state_label = "S"+str(state)
            state_block_link = []
            for j in range(len(other_list)):
                block2 = other_list[j]
                row2 = block2[0]
                col2 = block2[1]
                if check_state_link(row1, row2, col1, col2):
                    id2 = get_id(row2, col2, state)
                    state_block_link.append(id2)
                
            if len(state_block_link)!=0:
                curr_block_link[state_label] = state_block_link
        if len(curr_block_link)!=0:
            links[id1] = curr_block_link
    return links

def check_state_link(row1, row2, col1, col2):
    if row1==row2 or col1==col2:    # same row or same col
        if len(row1)==0 and len(row2)==0 and col1!=col2 \
            or len(col1)==0 and len(col2)==0 and row1!=row2:
            return False
        else:
            return True
    elif check_common_prefix(row1, row2) or check_common_prefix(col1, col2):
         # part same row or part same col
        return True
    else:
        return False

def check_common_prefix(h1, h2):
    if len(h1) == 0:
        return False
    elif len(h1) > len(h2):
        return False
    for i in range(len(h1)):
        if h1[i] != h2[i]:
            return False
    return True     
    
def check_siblings(h1, h2):
    if h1[-1] == h2[-1]:
        return 'same-name'
    elif h1[:-1] == h2[:-1]:
        return 'siblings'
    else:
        return None
    
def check_if_parent(parent, child):
    child_slice = child[:len(parent)]
    if parent == child_slice:
        return True
    else:
        return False

def get_id(idx, col, state):
    idx_str = "_".join(str(item) for item in idx)
    col_str = "_".join(str(item) for item in col)
    id = str(state) + '_' + idx_str + '-' + col_str + '_'
    return id