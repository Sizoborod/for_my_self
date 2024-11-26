def zadacha1():
    def oper1():
        '''Открыть CSV с помощью списка
        ВТимур'''
        pass

    def oper2():
        '''Открыть CSV с помощью словаря
        МНикита'''
        pass

    def oper3():
        '''Сохранить CSV с помощью списка
        АЮра'''
        pass

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


def zadacha2():
    def oper1():
        '''Как делать простой запрос на SQL
        ГДима'''
        pass


def zadacha3():
    def oper1():
        '''Как делать сложный запрос по нескольким таблицам запрос на SQL
        МАня'''
        request_tables = "SELECT album.Title, artist.Name " \
                         "FROM album INNER JOIN artist ON artist.ArtistId = album.ArtistId;"
