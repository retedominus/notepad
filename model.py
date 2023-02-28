import json
import os.path
from datetime import datetime


class Note:

    def __init__(self, note_id, title, content, time_stamp):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.time_stamp = time_stamp

    def to_dict(self):
        return {
            'id': self.note_id,
            'title': self.title,
            'content': self.content,
            'time_stamp': str(self.time_stamp)
        }


def get_next_id():
    if not os.path.exists('notes.json'):
        return 0
    with open('notes.json', 'r') as f:
        data = f.read().strip()
        if not data:
            return 0
        data = json.loads(data)
        notes = data.get('notes', [])
        if notes:
            note_ids = set()
            for note in notes:
                note_ids.add(note['id'])
            next_id = max(note_ids) + 1
            return next_id
            # last_note_id = notes[-1]['id']
            # return int(last_note_id) + 1
        else:
            return 0


def write_notes(notes):
    data = {'notes': [note.to_dict() for note in notes]}
    with open('notes.json', 'w') as f:
        json.dump(data, f, indent=4)


def read_notes():
    if not os.path.exists('notes.json'):
        return []
    with open('notes.json', 'r') as f:
        data = f.read().strip()
        if not data:
            return []
        data = json.loads(data)

    notes = []
    for note_data in data['notes']:
        time_stamp = datetime.strptime(note_data['time_stamp'], '%Y-%m-%d %H:%M:%S.%f')
        notes.append(Note(int(note_data['id']), note_data['title'], note_data['content'], time_stamp))

    return notes
