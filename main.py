import csv

def zadacha1():
    def oper1():
        '''Открыть CSV с помощью списка
        ВТимур'''
        pass

    def oper2():
        '''Открыть CSV с помощью словаря
        МНикита
        начинаю'''
        with open('files/ikea.csv', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            expensive = sorted(reader, key=lambda x: int(x['price']), reverse=True)

        pass

    def oper3():
        '''Сохранить CSV с помощью списка
        АЮра'''
        pass

    def oper4():
        '''Сохранить CSV с помощью словаря
        МАня'''
        pass


def zadacha2():
    def oper1():
        '''Как делать простой запрос на SQL
        ГДима'''
        pass


def zadacha3():
    pass
