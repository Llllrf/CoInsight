import json
import pandas as pd

class VisualForm:
    def __init__(self, data, insight_type, insight_category, insight_score):
        self.data = data
        self.insight_type = insight_type
        self.insight_category = insight_category
        self.insight_score = insight_score
        self.description = str(insight_type)
        self.vega_json = None
        self.create_vegalite()
    
    def create_vegalite(self):
        func_list= {'outlier': create_box_plot, 
                    'outlier-temporal': create_trail_plot,
                    'dominance':create_pie_chart, 
                    'top2':create_pie_chart, 
                    'trend':create_area_chart, 
                    'correlation': create_scatter_plot, 
                    'correlation-temporal': create_multi_line_chart,
                    'kurtosis': create_density_plot_color,
                    'skewness': create_density_plot,
                    'evenness': create_bar_chart
                    }
        vega_obj = func_list[self.insight_type](self.data)                     
        # vega_obj['description'] =  self.description
        self.vega_json = json.dumps(vega_obj)

# class VegaLiteObject:
#     def __init__(self, description, data, mark, encoding):
#         self.description = description
#         self.data = data
#         self.mark = mark
#         self.encoding = encoding

def create_bar_chart(d):
    values = []
    d = d.reset_index()
    if d[d.columns[0]].str.contains('-').any(): # include multiple columns, break it          
        d_tmp = d[d.columns[0]].str.split('-', n=1, expand=True)
        d_tmp.columns = ['var1', 'var2']
        d.drop(columns=d.columns[0], inplace=True)
        d = pd.concat([d_tmp, d], axis=1)
    else:
        d.columns = ['variable', 'value']
    for row in d.itertuples(index=False):
        v = {}
        for i in range(len(d.columns)):
            v[d.columns[i]] = row[i]
        values.append(v)
    mark = 'bar'
    encoding = {
        'x': {'field': d.columns[-2], 'type': 'nominal', "title": None},
        'y': {'field': d.columns[-1], 'type': 'quantitative', "title": None},
        'tooltip': [
            {'field': d.columns[-2], 'type': 'nominal'},
            {'field': d.columns[-1], 'type': 'quantitative'}
        ]
    }
    if len(d.columns)==3:   # breaked columns
        encoding["xOffset"] = {"field": d.columns[0]}
        encoding['color'] = {'field': d.columns[0], 
                             'type': 'nominal', 
                             "legend": {"orient": "bottom"},
                             "title": None}
    data = {'values': values}
    return {'data': data, 'mark': mark, 'encoding': encoding}

def create_pie_chart(d):
    values = []
    d = d.reset_index()
    d.columns = ['category', 'value']
    for row in d.itertuples(index=False):
        # if row[1] == 0:
        #     continue    # ignore zeros
        v = {d.columns[0]: row[0], d.columns[1]: row[1]}
        values.append(v)
    mark = {'type': 'arc', 'innerRadius': 5, 'stroke': '#fff'}
    encoding = {
        'theta': {'field': 'value', 'type': 'quantitative', "stack": True},
        'color': {'field': 'category', 'type': 'nominal', 'legend': None},
        'order': {
            'field': 'value',
            'type': 'quantitative',
            'sort': 'descending'
        },
        "radius": {"field": "value", "scale": {"type": "linear", "zero": True, "rangeMin": 20}},
        'tooltip': [
            {'field': 'category', 'type': 'nominal'},
            {'field': 'value', 'type': 'quantitative'}
        ]
    }
    data = {'values': values}
    return {'data': data, 'mark': mark, 'encoding': encoding}

def create_area_chart(d, color='#4682b4'):
    values = []
    d = d.reset_index()
    d.columns = ['variable', 'value']
    sort = []
    for row in d.itertuples(index=False):
        v = {d.columns[0]: row[0], d.columns[1]: row[1]}
        values.append(v)
        sort.append(row[0])
    mark = {
        'type': 'area', 
        'interpolate':'monotone',
        "line": {"color": color},
        "color": {
            "x1": 1,
            "y1": 1,
            "x2": 1,
            "y2": 0,
            "gradient": "linear",
            "stops": [
                {
                    "offset": 0,
                    "color": "white"
                },
                {
                    "offset": 1,
                    "color": color
                }
            ]
        }
    }
    encoding = {
        'x': {'field': d.columns[0], 'type': 'nominal', 'sort': sort, 'axis': {'labelOverlap': True, 'title': None}},
        'y': {'field': d.columns[1], 'type': 'quantitative', "title": None},
        'tooltip': [
            {'field': d.columns[0], 'type': 'nominal'},
            {'field': d.columns[1], 'type': 'quantitative'}
        ]
    }
    data = {'values': values}
    return {'data': data, 'mark': mark, 'encoding': encoding}

def create_scatter_plot(d):
    values = []
    d = d.reset_index()
    for row in d.itertuples(index=False):
        v = {d.columns[0]: row[0], d.columns[1]: row[1], d.columns[2]: row[2]}
        values.append(v)
    mark = 'point'
    encoding = {
        'x': {'field': d.columns[1], 'type': 'quantitative'},
        'y': {'field': d.columns[2], 'type': 'quantitative'},
        'tooltip': [
            {'field': d.columns[1], 'type': 'quantitative'},
            {'field': d.columns[2], 'type': 'quantitative'}
        ]
    }
    data = {'values': values}
    return {'data': data, 'mark': mark, 'encoding': encoding}

def create_multi_line_chart(d):
    values = []
    d = d.reset_index()
    d = d.melt(id_vars=[d.columns[0]])
    
    sort = []
    for row in d.itertuples(index=False):
        v = {d.columns[0]: row[0], d.columns[1]: row[1], d.columns[2]: row[2]}
        values.append(v)
        sort.append(row[0])
    mark = {'type': 'line', 'interpolate':'monotone'}
    encoding = {
        'x': {'field': d.columns[0], 
              'type': 'nominal',
              'axis': {'labelOverlap': True, 'title': None}, 
              'sort':sort
            },
        'y': {'field': d.columns[2], 'type': 'quantitative', 'title': None},
        'color': {'field': d.columns[1], 'type': 'nominal', 'legend': {'orient':'bottom'}, 'title': None},
        'tooltip': [
            {'field': d.columns[0], 'type': 'nominal'},
            {'field': d.columns[2], 'type': 'quantitative'}
        ]
    }
    data = {'values': values}
    return {'data': data, 'mark': mark, 'encoding': encoding}

def create_box_plot(d):
    values = []
    d = d.reset_index()
    d.columns = ['category', 'value']
    for row in d.itertuples(index=False):
        v = {d.columns[0]: row[0], d.columns[1]: row[1]}
        values.append(v)
    mark = {
        "type": "boxplot",
        "extent": 1.5,
        "size": 20,
        "median": {"color": "white"},
        "ticks": True
    }
    encoding = {
        'x': {'field': d.columns[1], 'type': 'quantitative', 'title': None},
        'tooltip': [
            {'field': d.columns[0], 'type': 'nominal'},
            {'field': d.columns[1], 'type': 'quantitative'}
        ]
    }
    data = {'values': values}
    return {'data': data, 'mark': mark, 'encoding': encoding}

def create_box_and_bar_plot(d):
    values = []
    d = d.reset_index()
    if d[d.columns[0]].str.contains('-').any(): # include multiple columns, break it          
        d_tmp = d[d.columns[0]].str.split('-', n=1, expand=True)
        d_tmp.columns = ['var1', 'var2']
        d.drop(columns=d.columns[0], inplace=True)
        d = pd.concat([d_tmp, d], axis=1)
    else:
        d.columns = ['variable', 'value']
    for row in d.itertuples(index=False):
        v = {}
        for i in range(len(d.columns)):
            v[d.columns[i]] = row[i]
        values.append(v)
    bar_mark = 'bar'
    bar_encoding = {
        'x': {'field': d.columns[-2], 'type': 'nominal', "title": None},
        'y': {'field': d.columns[-1], 'type': 'quantitative', "title": None},
        'tooltip': [
            {'field': d.columns[-2], 'type': 'nominal'},
            {'field': d.columns[-1], 'type': 'quantitative'}
        ]
    }
    if len(d.columns)==3:   # breaked columns
        bar_encoding["xOffset"] = {"field": d.columns[0]}
        bar_encoding['color'] = {'field': d.columns[0], 
                             'type': 'nominal', 
                             "legend": {"orient": "bottom"},
                             "title": None}
    box_mark = {
        "type": "boxplot",
        "extent": 4,
        "size": 20,
        "median": {"color": "white"},
        "ticks": True
    }
    box_encoding = {
        'x': {'field': d.columns[-1], 'type': 'quantitative', 'title': None},
        'tooltip': [
            {'field': d.columns[0], 'type': 'nominal'},
            {'field': d.columns[-1], 'type': 'quantitative'}
        ]
    }
    vconcat = [
        {"mark": box_mark, "encoding": box_encoding}, 
        {"mark": bar_mark, "encoding": bar_encoding}
    ]
    data = {'values': values}
    return {'data': data, "spacing": 15, "bounds": "flush", 'vconcat': vconcat}

def create_density_plot(d):
    values = []
    d = d.reset_index()
    d.columns = ['category', 'value']
    for row in d.itertuples(index=False):
        v = {d.columns[0]: row[0], d.columns[1]: row[1]}
        values.append(v)
    transform = [{"density": d.columns[1]}]
    mark = {
        'type': "area",
        "color": {
            "x1": 1,
            "y1": 1,
            "x2": 1,
            "y2": 0,
            "gradient": "linear",
            "stops": [
                {
                    "offset": 0,
                    "color": "white"
                },
                {
                    "offset": 1,
                    "color": 'darkgreen'
                }
            ]
        }
    }
    encoding = {
        "x": {
            "field": d.columns[1],
            "title": None,
            "type": "quantitative"
        },
        "y": {
            "field": "density",
            "type": "quantitative",
        }
    }
    data = {'values': values}
    return {'data': data, 'transform':transform ,'mark': mark, 'encoding': encoding}

def create_density_plot_color(d):
    values = []
    d = d.reset_index()
    d.columns = ['category', 'value']
    for row in d.itertuples(index=False):
        v = {d.columns[0]: row[0], d.columns[1]: row[1]}
        values.append(v)
    transform = [{"density": d.columns[1]}]
    mark = {
        'type': "area",
        "color": {
            "x1": 1,
            "y1": 1,
            "x2": 1,
            "y2": 0,
            "gradient": "linear",
            "stops": [
                {
                    "offset": 0,
                    "color": "white"
                },
                {
                    "offset": 1,
                    "color": '#e6550d'
                }
            ]
        }
    }
    encoding = {
        "x": {
            "field": d.columns[1],
            "title": None,
            "type": "quantitative"
        },
        "y": {
            "field": "density",
            "type": "quantitative",
        }
    }
    data = {'values': values}
    return {'data': data, 'transform':transform ,'mark': mark, 'encoding': encoding}

def create_trail_plot(d):
    values = []
    d = d.reset_index()
    d.columns = ['category', 'value']
    sort = []
    for row in d.itertuples(index=False):
        v = {d.columns[0]: row[0], d.columns[1]: row[1]}
        values.append(v)
        sort.append(row[0])
    mark = {
        "type": "trail"
    }
    encoding = {
        'x': {'field': d.columns[0], 'type': 'nominal', 'sort':sort, 'axis': {'labelOverlap': True, 'title': None}},
        'y': {'field': d.columns[1], 'type': 'quantitative', 'title': None},
        'size': {'field': d.columns[1], 'type': 'quantitative', 'legend': None},
        'tooltip': [
            {'field': d.columns[0], 'type': 'nominal'},
            {'field': d.columns[1], 'type': 'quantitative'}
        ]
    }
    data = {'values': values}
    return {'data': data, 'mark': mark, 'encoding': encoding}

def get_visualization(insight_list):
    vis_list = []
    if insight_list['point'] != [] \
        or insight_list['shape'] != [] \
        or insight_list['compound'] != []:
        for category in insight_list:
            insights = insight_list[category]
            for insight in insights:  
                vis = VisualForm(insight.scope_data, insight.type, insight.category, insight.score)
                vis_list.append(vis)
    # sort the vis list
    if len(vis_list) > 1:
        vis_list.sort(key=lambda x: x.insight_score, reverse=True)
    return vis_list