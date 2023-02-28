import uuid
from datetime import datetime


def get_note_data():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    return title, content


def display_notes(notes):
    if not notes:
        print("\nСписок заметок пуст.\n")
        return
    print("\nСписок заметок: ")
    for note in notes:
        print(f"ID заметки: {note.note_id}\n{note.title} (Создана (изменена): "
              f"{note.time_stamp.strftime('%d-%m-%Y %H:%M:%S')})\n{note.content}")
    print()


def get_filter_date():
    filter_date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    try:
        filter_date = datetime.strptime(filter_date_str, "%d.%m.%Y")
    except ValueError:
        print("Некорректный формат даты. Попробуйте снова.")
        return get_filter_date()
    else:
        return filter_date


def display_filtered_notes(notes, filter_date):
    filtered_notes = [note for note in notes if note.time_stamp.date() == filter_date.date()]
    if not filtered_notes:
        print(f"Заметок за {filter_date.strftime('%d.%m.%Y')} не найдено.")
    else:
        print(f"Список заметок за {filter_date.strftime('%d.%m.%Y')}:")
        for note in filtered_notes:
            print(f"{note.title} ({note.time_stamp.strftime('%d-%m-%Y %H:%M:%S')})")
    print()


def get_note_id():
    note_id_str = input("Введите ID заметки: ")
    try:
        note_id = int(note_id_str)
    except ValueError:
        print("Некорректный формат ID. Попробуйте снова.")
        return get_note_id()
    else:
        return note_id


def get_note_update_data():
    title = input("Введите новый заголовок (оставьте пустым, чтобы не изменять): ")
    content = input("Введите новое содержание заметки (оставьте пустым, чтобы не изменять): ")
    return title, content

