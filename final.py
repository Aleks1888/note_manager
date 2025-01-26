
username = input("Введите имя пользователя: ")
title = input("Заголовок заметки: ")
titles = input("Заголовок 1: "), input("Заголовок 2: "),input("Заголовок 3: ")
content = input("Описание заметки: ")
status = input("Статус заметки: ")
created_data = input('Введите дату начяла, д-м-г: ')
issue_data = input('Ввкдите дату окончяние, д-м-г: ')

note = {
    "Имя пользователя" : username,
    "Заголовок заметки" : title,
    "Под заголовк" : titles,
    "Описание заметки" : content,
    "Статус заметки" : status,
    "Начяла" : created_data,
    "Окончание" : issue_data,
    ("Заголовок 1: ","Заголовок 2: ","Заголовок 3: ") : titles
}

print (f"Имя пользователя: {username}")
print (f"Заголовок заметки: {title}")
print (f"Под заголовки. {titles}")
print (f"Описание заметки: {content}")
print (f"Статус заметки: {status}")
print (f"Начяло:{created_data}"[:-5])
print (f"Окончание:{issue_data}"[:-5])
