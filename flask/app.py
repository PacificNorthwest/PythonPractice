from flask import Flask, Response, render_template,  request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

records = [
    'record 1',
    'record 2',
    'record 3',
    'record 4'
]

class RecordsController(Resource):
    def get(self, id=None):
        if id:
            return records[id], 200
        return records, 200
    
    def post(self):
        records.append(request.form['record'])
        return Response(status=200)

    def put(self, id):
        records[id] = request.form['record']
        return Response(status=200)

    def delete(self, id):
        records.pop(id)
        return Response(status=200)

api.add_resource(RecordsController, '/records/<int:id>', '/records')

@app.route('/')
def index():
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run()