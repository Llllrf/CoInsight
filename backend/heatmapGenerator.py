import json


def findSpanInfo(name, dict, mode):
    paths = name.split('_')
    info = dict[paths[0]]
    for path in paths[1:]:
        info = info['children'][path]
    return info['rowSpan'] if mode == 'row' else info['colSpan']


def listToDict(lst):
    d = {}
    for item in lst:
        if "children" in item and item["children"]:
            child_dict = listToDict(item["children"])
            d[item["name"]] = {**item, "children": child_dict}
        else:
            d[item["name"]] = item
    return d


def get_heatmap(table, graph, focus):
# with open('result_0830_S7.json') as file:
#     data = json.load(file)
    colNum = table['colNum']
    rowNum = table['rowNum']
    rowDict = listToDict(table['rows'])
    colDict = listToDict(table['cols'])
    # 只对当前focus 的点做计算
    nodeData = list(
        filter(lambda x: x['state'] == focus, graph['nodes'])
    )
    # 创建空数组, 记录单个cell 在 insight 中的出现值
    heatData = []
    for rowNumber in range(rowNum):
        rowHeat = []
        for colNumber in range(colNum):
            rowHeat.append(0)
        heatData.append(rowHeat)

    for node in nodeData:
        rowName = node['row']
        colName = node['col']
        colSpan = []
        if (colName == '_'):
            colSpan = [0, colNum-1]
        else:
            colSpan = findSpanInfo(colName, colDict, 'col')
        rowSpan = []
        if (rowName == '_'):
            rowSpan = [0, rowNum-1]
        else:
            rowSpan = findSpanInfo(rowName, rowDict, 'row')
       # print(rowSpan, colSpan)
        for rowNumber in range(rowSpan[0], rowSpan[1]+1):
            rowHeat = heatData[rowNumber]
            for colNumber in range(colSpan[0], colSpan[1]+1):
                rowHeat[colNumber] += 1
    # print(heatData)
    return heatData
