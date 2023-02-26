from controller import NoteController


def main():
    controller = NoteController()
    while True:
        print("Меню: ")
        print("1. Добавить заметку")
        print("2. Вывести список заметок")
        print("3. Фильтровать заметки по дате")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Сохранить заметки в файл")
        print("7. Выход")
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            controller.add_note_command()
        elif choice == "2":
            controller.display_notes_command()
        elif choice == "3":
            controller.filter_notes_by_date_command()
        elif choice == "4":
            controller.update_note_command()
        elif choice == "5":
            controller.delete_note_command()
        elif choice == "6":
            controller.save_notes_command()
        elif choice == "7":
            break
        else:
            print("Неверный выбор.")


if __name__ == '__main__':
    main()
