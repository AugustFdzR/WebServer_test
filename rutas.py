from flask import Flask
from flask import request

#http://localhost:8000/params?params1=Cesar_Fdz
#http://localhost:8000/params?params1=Cesar_Fdz&params2=Ingeniero
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola mundo'
		
@app.route('/params')
def params():
	param = request.args.get('params1', 'no contiene este parametro')
	param_dos = request.args.get('params2', 'no contiene este parametro')
	return 'El parametro es : {} , {}'.format(param, param_dos)
if __name__ == '__main__':
	app.run(debug = True, port=8000)
