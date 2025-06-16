from flask import Flask
from flask import request

import anothermodule as am

# Best practice: use __name__ to help Flask find its own location.
app = Flask(__name__)

# The route is now '/ping', which is more descriptive.
@app.route('/ping', methods=['GET', 'POST'])
# @app.route('/ping', methods=['GET', 'POST'])
def ping():
    data = request.get_json()
    name = data['name']
    
    return am.sayhello() + ', ' + name 

@app.route('/pong', methods=['GET', 'POST'])
def pong():
    return 'pong'
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

# https://www.youtube.com/watch?v=D7wfMAdgdF8&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=18
# pipenv shell