import uuid
from datetime import datetime

from model import read_notes, Note, write_notes
from view import get_note_data, display_notes, get_filter_date, display_filtered_notes, get_note_id, \
    get_note_update_data


class NoteController:
    def __init__(self):
        self.notes = read_notes()

    def add_note_command(self):
        title, content = get_note_data()
        note_id = uuid.uuid4()
        time_stamp = datetime.now()
        note = Note(note_id, title, content, time_stamp)
        self.notes.append(note)
        print("Заметка добавлена.")

    def display_notes_command(self):
        display_notes(self.notes)

    def filter_notes_by_date_command(self):
        filter_date = get_filter_date()
        display_filtered_notes(self.notes, filter_date)

    def update_note_command(self):
        note_id = get_note_id()
        note_index = self.find_note_index_by_id(note_id)
        if note_index is None:
            print("Заметка не найдена.")
            return
        title, content = get_note_update_data()
        if title:
            self.notes[note_index].title = title
        if content:
            self.notes[note_index].content = content
        print("Заметка обновлена.")

    def delete_note_command(self):
        note_id = get_note_id()
        note_index = self.find_note_index_by_id(note_id)
        if note_index is None:
            print("Заметка не найдена.")
            return
        del self.notes[note_index]
        print("Заметка удалена.")

    def save_notes_command(self):
        write_notes(self.notes)
        print("Заметки сохранены в файл.")

    def find_note_index_by_id(self, note_id):
        for i, note in enumerate(self.notes):
            if note.note_id == note_id:
                return i
            return None




