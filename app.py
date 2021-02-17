from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

notes = {}


class Note(Resource):
    def get(self, note_id):
        return {note_id: notes[note_id]}

    def put(self, note_id):
        notes[note_id] = request.form['data']
        return {note_id: notes[note_id]}


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
