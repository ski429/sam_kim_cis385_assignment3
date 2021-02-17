from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

notes = [
    {
        'id': 0,
        'title': 'hello',
        'body': 'world'
    },
    {
        'id': 1,
        'title': 'hello',
        'body': 'everybody'
    }
]


@api.route('/notes/')
def get(self):
    return notes


@api.route('/notes/<int:note_id>')
def get(self, note_id):
    return [note for note in notes if note[note_id] == note_id]


if __name__ == '__main__':
    app.run()
