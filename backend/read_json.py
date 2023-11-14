import json

def generate_txt(path):
    txt_path = path.replace('.json', '.txt')
    with open(txt_path, 'w'):
        pass
    with open(path, 'r') as file:
        data = json.load(file)
        graph = data['graph']
        table = data['table']
        state_links = data['state_links']
        nodes = graph['nodes']
        links = graph['links']
        with open(txt_path, 'a') as f:
            for node in nodes:
                id = node['id']
                f.write('==================== [node] ' + id + ' ====================\n')
                f.write('state: ' + node['state'] + '   row: ' + node['row'] + '   col: ' + node['col'] + '\n')
                f.write('---------- insight-list ----------\n')
                insight_list = node['insight-list']
                for insight in insight_list:
                    f.write('insight-type: ' + insight['insight-type'] + '\n')
                    f.write('insight-category: ' + insight['insight-category'] + '\n')
                    vega = insight['vega-lite']
                    vega_obj = json.loads(vega)
                    vega_obj['width'] = 200
                    vega_obj['height'] = 200
                    vega = json.dumps(vega_obj)
                    f.write(vega)
                    f.write("\n---------------\n")
                    
            
            f.write('==================== links ====================\n')
            for link in links:
                f.write(str(link))
                f.write("\n")
            
            f.write('==================== table ====================\n')
            f.write(str(table))

            f.write('==================== state_links ====================\n')
            f.write(str(state_links))
            