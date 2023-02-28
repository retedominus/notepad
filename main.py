from controller import NoteController


def main():
    controller = NoteController()
    while True:
        print("Меню:\n"
              "1. Добавить заметку\n"
              "2. Вывести список заметок\n"
              "3. Фильтровать заметки по дате\n"
              "4. Редактировать заметку\n"
              "5. Удалить заметку\n"
              "6. Выход")
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
            break
        else:
            print("Неверный выбор.")


if __name__ == '__main__':
    main()
