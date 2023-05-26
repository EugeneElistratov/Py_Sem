# Пришлось делать на версии Python 3.8.8. 
# Поэтому вместо match использовал if/else
# Задача 38: Дополнить телефонный справочник возможностью изменения 
# и удаления данных. Пользователь также может ввести имя 
# или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

from os import path
except_message = 'Ой! Что-то пошло не так... Попробуйте снова'
file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_file():
    try:
        with open(file_base,'r',encoding='UTF-8') as f:
            for line in f:
                print(line.strip())
    except:
        print(except_message)
    print()
def add_to_file():
    print()
    try:
        new_info = []
        directives = ['Введите фамилию: ', 'Введите имя: ', 'Введите отчество: ', 'Введите номер телефона: ']

        for i in directives:
            data = input(i)
            if data == '#': return
            new_info.append(data)

        new_info = (' ').join(new_info).strip()

        with open(file_base,'a',encoding='UTF-8') as f:
            f.writelines('\n' + new_info)

        print(f'Данные "{new_info}" сохранены успешно')
    except:
        print(except_message)

def find_line():
  print()
  try:
    find_info = input('Введите данные для поиска: ')
    with open(file_base,'r',encoding='UTF-8') as f:
      for line in f:
        if find_info.casefold() in line.casefold():
          print(line)
  except:
    print(except_message)

def find_line_for_modify():
  print()
  try:
    res = []
    find_info = input('Введите данные для поиска: ')

    if find_info == '#': return '#'

    with open(file_base,'r',encoding='UTF-8') as f:
      for line in f:
        if find_info.casefold() in line.casefold():
          res.append(line)

    if len(res) == 1:
      print(res[0])
      return res[0]
    elif len(res) > 1:
      for i in range(len(res)):
          print(f'{i + 1} - {res[i]}')
      num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
      print(res[num_count - 1])
      return res[num_count - 1]
    else:
      print('По введённым данным ничего не найдено')
      return '#'

  except:
    print(except_message)

def change_file():
  try:
    phonebook = ''
    changing_line = find_line_for_modify()
    if changing_line == '#': return

    changing_line_list = changing_line.split()
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Номер телефона\n')
    if field == '#': return
    text = ''
    if field == '1': text = 'Фамилию'
    elif operation == '2': text = 'Имя'
    elif operation == '3': text = 'Отчество'
    elif operation == '4': text = 'номер телефона'
    else: return

    new_field = input(f'Введите {text}: ')
    if new_field == '#': return
    changing_line_list[int(field) - 1] = new_field

    with open(file_base,'r',encoding='UTF-8') as f:
      phonebook = f.read()

    phonebook = phonebook.replace(changing_line, ' '.join(changing_line_list) + '\n')

    with open(file_base,'w',encoding='UTF-8') as f:
      f.write(phonebook)

    print('Данные успешно изменены')

  except:
    print(except_message)

def delete_line():
  try:
    phonebook = ''
    changing_line = find_line_for_modify()
    if changing_line == '#': return

    confirm = input(f'Для подтверждения удаления данных нажмите 1, для отмены #: ')

    if confirm != '1': return

    with open(file_base,'r',encoding='UTF-8') as f:
      phonebook = f.read()
    phonebook = phonebook.replace(changing_line, '')
    with open(file_base,'w',encoding='UTF-8') as f:
      f.write(phonebook)

    print('Данные успешно удалены')

  except:
    print(except_message)

def main_menu():
    play = True
    while play:
        answer = input("Phone book:\n"
                       "1. Посмотреть весь справочник.\n"
                       "2. Добавить запись.\n"
                       "3. Найти запись.\n"
                       "4. Изменить запись\n"
                       "5. Удалить запись\n"
                       "6. Выход\n")
        if answer == "1":
            read_file()
        elif answer == "2":
            add_to_file()
        elif answer == "3":
            find_line()
        elif answer == "4":
            change_file()
        elif answer == "5":
            delete_line()
        elif answer == "6":
            play = False
        else:
            print("Try again!\n")
    
main_menu()

# Phone book:
# 1. Посмотреть весь справочник.
# 2. Добавить запись.
# 3. Найти запись.
# 4. Изменить запись
# 5. Удалить запись
# 6. Выход
# 1
# Иванов Иван Кириллович 8451235678
# Васечкин Иван Васильевич 84951234567
# Сидоров Сидор Сидорович 84952345678
# Кошкин Петр Сергеевич 84953451256
# Никифоров Иван Ильичев 84954561223
# Корягин Никодим Иванович 84957812389
# Фамусевич Василий Петрович 84952584585
# Панин Петр Иванович 84955465431
# Сидоров Сидор Сидорович 849554652165