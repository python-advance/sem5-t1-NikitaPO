'''

1.2. Создание пользовательского пакета для приложения «Гостевая книга» («Регистрация на конференцию») с прототипами методов,
позволяющих взаимодействовать с JSON-файлом(создание, удаление, переименование, чтение, запись). Формирование отчета по практическому заданию и публикация его в портфолио.
'''

import json


def showGuests():
    with open('guests.json', 'r') as f:
        guests = json.load(f)
        print(guests)


def createFile():
    try:
        open("guests.json", 'r+')
    except FileNotFoundError:
        with open('guests.json', 'w') as f:
            json.dump([], f)


def addGuest(name, age):
    guests = []
    with open('guests.json', 'r+') as f:
        guests = json.load(f)

    with open('guests.json', 'w') as f:
        guests.append({"name": name, "age": age})
        json.dump(guests, f)


createFile()
addGuest("Mark", "22")
showGuests()
