from controller import NoteController


def main():
    controller = NoteController()
    while True:
        print("Меню:\n"
              "1. Добавить заметку\n"
              "2. Вывести список заметок\n"
              "3. Фильтровать заметки по дате\n"
              "4. Показать заметку\n"
              "5. Редактировать заметку\n"
              "6. Удалить заметку\n"
              "7. Выход\n")
        choice = input("Выберите пункт меню: ")
        if choice == "1":
            controller.add_note_command()
        elif choice == "2":
            controller.display_notes_command()
        elif choice == "3":
            controller.filter_notes_by_date_command()
        elif choice == "4":
            controller.show_specific_note_command()
        elif choice == "5":
            controller.update_note_command()
        elif choice == "6":
            controller.delete_note_command()
        elif choice == "7":
            break
        else:
            print("\nНеверный выбор.\n")


if __name__ == '__main__':
    main()
