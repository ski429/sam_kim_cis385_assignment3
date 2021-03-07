from flask import Flask, make_response
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
        "id": 2,
        "title": "grocery",
        "body": "milk, eggs"
    }
]


def get_note(param, key):
    for note in notes:
        if note[param] == key:
            return note
    response = make_response("Note not found.", 404)
    return response


class Note(Resource):
    def get(self, note_id):
        return get_note("id", note_id)

    def put(self, note_id):
        temp = get_note("id", note_id)
        if temp is None:
            return None
        args = notes_put_args.parse_args()
        for k, v in args.items():
            temp[k] = v
        return temp

    def delete(self, note_id):
        notes.remove(get_note("id", note_id))
        return notes


class NoteByTitle(Resource):
    def get(self, title):
        return get_note("title", title)

    def put(self, title):
        temp = get_note("title", title)
        if temp is None:
            return None
        args = notes_put_args.parse_args()
        temp["body"] = args["body"]
        return temp

    def post(self, title):
        if get_note("title", title) is not None:
            return "Note already exists"
        args = notes_put_args.parse_args()
        next_id = notes[-1]["id"] + 1
        args["id"] = next_id
        args["title"] = title
        notes.append(args)
        return next_id


class AllNotes(Resource):
    def get(self):
        return notes


api.add_resource(Note, '/notes/<int:note_id>')
api.add_resource(NoteByTitle, '/notes/<string:title>')
api.add_resource(AllNotes, '/notes/')

if __name__ == '__main__':
    app.run(debug=True)
