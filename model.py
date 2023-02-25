import json
import uuid
from datetime import datetime


class Note:

    def __init__(self, title: str, content: str):
        self._id = str(uuid.uuid4())
        self._title = title
        self._content = content
        self._time_stamp = datetime.now()

    def to_dict(self):
        return {
            'id': self._id,
            'title': self._title,
            'content': self._content,
            'time_stamp': self._time_stamp.strftime('%Y-%m-%d %H:%M:%S')
        }

    def update(self, title=None, content=None):
        self._title = title if title is not None else self._title
        self._content = content if content is not None else self._content
        self._time_stamp = datetime.now()


def save_note(note):
    with open('note_pad.json', 'r') as f:
        data = json.load(f)

    data['notes'].append(note.to_dict())

    with open('note_pad.json', 'w') as f:
        json.dump(data, f, indent=4)


def load_note():
    with open('note_pad.json', 'r') as f:
        data = json.load(f)

    notes = []
    for note_data in data['notes']:
        time_stamp = datetime.strftime(note_data['time_stamp'], '%Y-%m-%d %H:%M:%S')
        notes.append(Note(note_data['id']))