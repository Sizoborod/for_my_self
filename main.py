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
        #Основной командой для получения какой-либо информации из БД является команда SELECT
        """SELECT перечень_полей FROM имя_таблицы
        WHERE условие"""
        # Пример запроса
        """SELECT * FROM Films
    WHERE year = 2010"""
        # Запрос для двух БД
        """SELECT title FROM Films 
                WHERE genre=(
                        SELECT id FROM genres 
                            WHERE title = 'фантастика')"""
        # Использование IN
        """SELECT title, duration FROM Films 
                WHERE duration IN (45, 90)""" # IN строго 45 или 90 минут
        # BETWEEN диапазон(включая границы)
        """SELECT * FROM Films
    WHERE (year > 2005) AND duration BETWEEN 45 AND 60 """
        # Оператор LIKE
        """SELECT * FROM Films
    WHERE title like 'А_к%'"""
        # % — обозначает любое количество, в том числе нулевое, любых символов
        # _  обозначает один любой символ
def zadacha3():
    def oper1():
        '''Как делать сложный запрос по нескольким таблицам запрос на SQL
        МАня'''
        pass
    pass
