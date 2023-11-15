import os
import uuid
import PoolGenerator
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from table import HierarchicalTable
from dataSource import DataSource


global data_table
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_table():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(folder):
            os.makedirs(folder)
        filepath = os.path.join(folder, filename)
        file.save(filepath)

        # process the uploading table
        requ_id = str(uuid.uuid4())
        result = create_table(filename, filepath, requ_id)

        # return the result to frontend
        return jsonify(result)


@app.route('/state/<s>', methods=['GET'])
@cross_origin()
def change_state(s):
    s_num = int(s[1:])
    global data_table
    result = data_table.change_current_state(s_num)
    return jsonify(result)

@app.route('/back/<s>', methods=['GET'])
@cross_origin()
def state_back(s):
    s_num = int(s[1:])
    global data_table
    result = data_table.change_state_back(s_num)
    return jsonify(result)


@app.route('/photo', methods=['POST'])
@cross_origin()
def get_state_table():
    states = request.json['stateList']
    global data_table
    result = {}
    for i in range(len(states)):
        s_name = states[i]
        s_num = int(s_name[1:])
        state_data = data_table.get_state_data(s_num)
        result[s_name] = state_data['table']
    return jsonify(result)


def create_table(name, path, requ_id):
    name = name.split('.')[0] # remove the postfix(.xlsx) of a file name
    
    # if there is func_dependency, add it here
    func_dependency = [(1, 0, 'row')]
    
    data_source = DataSource(name, path, requ_id, func_dependency)
    global data_table
    data_table = HierarchicalTable(data_source)
    result = data_table.generate_all_results()

    return result
    

if __name__ == '__main__':
    # PoolGenerator.init_pool()
    app.run(debug=True)
    # PoolGenerator.pool.close()
    # PoolGenerator.pool.join()
