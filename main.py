import csv


def zadacha1():
    def oper1():
        '''Открыть CSV с помощью списка
        ВТимур'''
        with open('files/ikea.csv', encoding="utf8") as csvfile:
            read_file = csv.ListReader(csvfile, delimiter=';', quotechar='"')  # again_1

    def oper2():
        '''Открыть CSV с помощью словаря
        МНикита'''
        pass

    def oper3():
        '''Сохранить CSV с помощью списка
        АЮра'''

        # Набор данных
        data = [('Name', 'Age'), ('Alice', 25), ('Bob', 22)]

        # Непосредственная запись в CSV-файл
        with open('my.csv', 'w', newline='') as f:
            csv.writer(f, delimiter=';').writerows(data)

    def oper4():
        '''Сохранить CSV с помощью словаря
        МАня что-то да делает'''
        import csv

        data = [{
            'lastname': 'Иванов',
            'firstname': 'Пётр',
            'class_number': 9,
            'class_letter': 'А'
        }, {
            'lastname': 'Кузнецов',
            'firstname': 'Алексей',
            'class_number': 9,
            'class_letter': 'В'
        }, {
            'lastname': 'Меньшова',
            'firstname': 'Алиса',
            'class_number': 9,
            'class_letter': 'А'
        }, {
            'lastname': 'Иванова',
            'firstname': 'Татьяна',
            'class_number': 9,
            'class_letter': 'Б'
        }]

        with open('dictwriter.csv', 'w', newline='', encoding="utf8") as f:
            writer = csv.DictWriter(
                f, fieldnames=list(data[0].keys()),
                delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            for d in data:
                writer.writerow(d)

    oper3()


def zadacha2():
    def oper1():
        '''Как делать простой запрос на SQL
        ГДима'''
        pass


def zadacha3():
    pass


zadacha1()
