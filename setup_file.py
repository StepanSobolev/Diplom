from class_file import People_base


def choice():
    main = People_base()
    while True:
        choice_user = input('Якшо хочете додати людину натисніть Д/A\n'
                            'Якщо хочете перевірити людину натисніть П/R\n'
                            'Якщо хочете видалити людину натисніть В/D\n'
                            'Щоб вийти натисніть Q:\n'
                            'Щоб загрузити документи з файлу натисніть Я/L:').strip().lower()

        if choice_user in ['д', 'a']:
            main.add_member()
        elif choice_user in ['п', 'r']:
            main.show_user()
        elif choice_user in ['в', 'd']:
            main.dell_user()
        elif choice_user in ['я', 'l']:
            main.export_to_db()
        elif choice_user == 'q':
            print('Бувайте здорові!!!')
            break
        else:
            print('-' * 30)
            print('Будь ласка слідкуйте привилам!!!')
            print('-' * 30)


choice()
