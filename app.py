from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

notes_put_args = reqparse.RequestParser()
notes_put_args.add_argument("title", type=str, help="title of note")
notes_put_args.add_argument("body", type=str, help="body of note")

notes = [
    {
        "id": 0,
        "title": "todo",
        "body": "fill up gas"
    },
    {
        "id": 1,
        "title": "grocery",
        "body": "milk, eggs"
    }
]


class Note(Resource):
    def get(self, note_id):
        return notes[note_id]

    def put(self, note_id):
        args = notes_put_args.parse_args()
        return {note_id: args}

    def delete(self, note_id):
        pass


class NoteByTitle(Resource):
    def get(self, title):
        for note in notes:
            if note['title'] == title:
                return note
        return {}

    def put(self, title):
        pass

    def post(self, title):
        pass


class AllNotes(Resource):
    def get(self):
        return notes


api.add_resource(Note, '/notes/<int:note_id>')
api.add_resource(NoteByTitle, '/notes/<string:title>')
api.add_resource(AllNotes, '/notes/')

if __name__ == '__main__':
    app.run(debug=True)
