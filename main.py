# import time
#
# for i in range(10):
#     print(f"Прогресс: {i}/10", end="\r")
#     time.sleep(1)


# a = "hello"
# b = a[3]
# c = a[len(a) - 1]
# print(b)
# print(c)

# str1 = "Hello my friend!"
# str2 = str1[0:6]
# str3 = str1[:6]
# str4 = str1[6:]
# str6 = str1[::2]
# str7 = str1[::-1]
# str8 = str1[4::-1]
# print(str2)
# print(str3)
# print(str4)
# print(str6)
# print(str7)
# print(str8)
#
# str1 = "Hello World!"
# str1 = "K" + str1[1:]

# main_str = input()
# first_char = main_str[0]
# last_char = main_str[-1]
# print(first_char, last_char)

# main_str = "Hello"
# print(id(main_str))
# print(id(main_str[0]))

# main_string = "Привет, мир!"
# reversed_string = main_string[::-1]  # Получаем строку в обратном порядке "!рим ,тевирП"
# substring1 = main_string[4:1:-1]  # Получаем подстроку "евир"
# substring2 = main_string[::-2] # Получаем каждый второй символ в обратном порядке
# substring3 = main_string[1:4:-1] # Получаем пустую строку
# print("reversed_string: ", reversed_string)
# print("substring1: ", substring1)
# print("substring2: ", substring2)
# print("substring3: ", substring3)

# main_str = "Hello World!"
# number_str = "+123456"
# sub_str = "a"
# result_str = main_str.upper()
# result_str = main_str.lower()
# result_str = main_str.count(sub_str)
# result_str = main_str.find(sub_str)
# # result_str = main_str.index(sub_str)
# result_str = main_str.replace(" ", "/")
# result_str = main_str.isalpha()
# result_str = main_str.ljust(16, ",")
# print(result_str)

# cities = "Питер,Моска,Ростов,Ставрополь,Нальчик"
# cities_lst = cities.split(",")
# print(cities_lst)

# cities_lst = ["Питер", "Москва", "Нальчик"]
# cities_str = ",     ".join(cities_lst)
# print(cities_str)

# main_str = "    h e l l o    "
# result_str = main_str.replace(" ", "")
# print(result_str)

# main_str = "hesdvsd world"
# index_space = main_str.find(" ")
# print(index_space)
# sub_str1 = main_str[:index_space]
# print(sub_str1)

# import math
# print(round(math.pi))
# print(round(math.pi, 2))
# print(math.pi)
#
# main_str = "hello world"
# sub_str = main_str[:5]
# char = main_str[0]
# index_char = main_str.index("h")

# path = r"C:\Users\whymk\Desktop\Python\PythonStartCourse\pythonProject\main.py"
# print(path)

# name = "Vasya"
# second_name = "Oblomov"
# age = 33
# main_str = "My name is {width}, old {height}".format(width=a, deep=b, height=c)
# print(main_str)
# # f_str = f"My name is {name + ' ' + second_name}, old {age + 10}"
# # print(f_str)
#
# a, b, c = "10 11 12".split()










# my_lst = [1, 2, 3, 4, 5]
# my_lst = []
# my_lst = list( (1, 2, 3, 4, 5) )



# my_list = list('hello')
# print(my_list)
#
# my_list[10]
# print(my_list)



# my_list = [1, 2, 3, 4, 5]
# lenght_list = len(my_list)
# sorted_list = sorted(my_list, reverse=True)
# flag = 6 in my_list
# print(flag)


# count = 2
# str = "hello"
#
# print(len(str))

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Пример среза с двумя аргументами
# sublist1 = numbers[2:5]
# print(sublist1)  # [2, 3, 4]
#
# # Пример среза с тремя аргументами
# sublist2 = numbers[1:8:2]
# print(sublist2)  # [1, 3, 5, 7]

# numbers = [1, 2, 3, 4, 5]
# numbers[1:4] = [10, 20, 30, 40]
# print(numbers)

# a = 12
# a = "12"
# a = input()
# print(a)

# str = input() #получаем строку
# print(type(str), str)
# lst = str.split() #превращаем ее в список
# print(type(lst), lst)
# lst[0] = int(lst[0])
# lst[1] = int(lst[1])
# print(type(lst), lst)

# lst = [1, 2, 3, 2, 6, 1, 10, 5]
# lst_str = ["1", "2", "3"]
# lst.append(5)
# lst.insert(2, 5)
# lst.remove(3)
# lst_str.remove("1")
# lst.pop()
# number = lst.pop(0)
# sorted(lst)
# print(lst)
# print(lst2)
#
# cities = ["Москва", "Казань", "Ярославль"]
# city = "Ульяновск"
#
# print(cities)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix[0][-1] = matrix[0][-1] + 10
# print(matrix)

# перед нотами до и фа поставить символ диеза '#'. Если число равно 1 или 4
# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# a, b, c = map(int, ["1", "6", "7"])
# note_a = f"{'#' + m[a-1] if a == 1 else '#' + m[a-1] if a == 4 else m[a-1]}"
# note_b = f"{'#' + m[b-1] if b == 1 else '#' + m[b-1] if b == 4 else m[b-1]}"
# note_c = f"{'#' + m[c-1] if c == 1 else '#' + m[c-1] if c == 4 else m[c-1]}"
# print(note_a, note_b, note_c)

# lst = [1, 3, 2]
# print(lst)
# str = f"{lst[0]} {lst[1]} {lst[2]}"
# print(str)

# lst = [ [ 1, [5, 6, 7], False ],  [2, 3, 4],  [3, 4, 5] ]
# print(lst[0])
# print(lst[0][1][1])
#
# num = "Сок"
#
# if num == "Чай":
#     print("Это чай")
# elif num == "Сок":
#     print("Это сок")
# elif num == "Кофе":
#     print("Это кофе")
# elif num == "Газировка":
#     print("Это Газировка")
# else:
#     print("Это не напиток")

# a = 12
# b = 3
# c = 14
#
# if a < b:
#     if a < c:
#         print(a)
#     else:
#         print(c)
# elif a < c:
#     if a < b:
#         print(a)
#     else:
#         print(b)
# elif b < c:
#     if b < a:
#         print(b)
#     else:
#         print(a)
#
# a = 3
# str = f"a {'четное' if a % 2 == 0 else 'нечетное'} число"
# print(str)
#
# a = 10
# b = 7
# if a < 10:
#     if b > 15:
#         print(a, b)
#
# if a > 10:
#     print(b)
# elif b > 15:
#     print(b)
# else:
#     print("ascwea")

# numbers = [1, 2, 3, 4, 5]
#
# for num in numbers:
#     print(num)

# good_password = input("Создайте пароль: ")
# password = input("Введите пароль: ")
#
# while password != good_password:
#     print("Неверный пароль. Попробуйте еще раз.")
#     password = input("Введите пароль: ")
#
# print("Доступ разрешен. Добро пожаловать!")

# numbers = [10, 40, 20, 30]
#
# for item in numbers:
#     print(item)
#     item += 10
#     print(item)

# for i in range(1, 6):
#     print(i)

# word = "Hello"
# for char in word:
#     print(char)

# fruits = ["apple", "banana", "cherry"]
# str = "Hello"
#
# for index, fruit in enumerate(str):
#     print("Index:", index, "Fruit:", fruit)
#
# original_list = ["Hello", "World", "Python"]
# new_list = []
#
# for string in original_list:
#     first_letter = string[0]
#     new_list.append(first_letter)
#
# print(new_list)

# r = range(9)
# lst = list(r)
# print(lst)
# lst = ["Hello", "Python", "Phone", "Pc", "numbers", "digits", "fruits", "honor"]
# for i in range(2, 8):
#     print(lst[i])
#
# for i in range(1, 10, 2):
#     print(i)

# lst = [1, 2, 3, 4, 5]
#
#
# lst = list(map(int, input().split()))
#
# for i in range(len(lst)):
#     element = lst[i]
#     print(element)

# список замен для соответствующих русских букв

# str = "osnovnye---metody-----------spiska----------------hjgcvfgcgfccfg"
# str_2 = str.replace("-", " ")
# lst = str_2.split()
# str_3 = ""
# while len(lst) > 0:
#     str_3 += lst.pop(0) + "-"
#
# str_3 = str_3[:-1]
# print(str)

# numbers = "Hello World"
# lst = numbers.split()
# for item in lst:
#     print(item)

# original_list = ["Hello", "World", "Python"]
# new_list = []
#
# for string in original_list:
#     first_letter = string[0]
#     new_list.append(first_letter)
#
# print(new_list)

# lst1 = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# lst2 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
#
# r_lst = []
# for i in range(len(lst1)):
#     sublist = []
#     for j in range(len(lst2[i])):
#         sublist.append(lst1[i][j] + lst2[i][j])
#     r_lst.append(sublist)
# print(r_lst)
#
# lst = [ "Я   помню  чудное    мгновенье",
# "Передо  мной    явилась   ты",
# "Как    мимолетное   виденье",
# "Как     гений   чистой  красоты"]
#
# for index, line in enumerate(lst):
#     while lst[index].count("  "):
#         lst[index] = lst[index].replace("  ", " ")
#
# print(lst)

# lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
#
# for row in lst:
#     for number in row:
#         print(number, end='\t')
#     print()

# str = "Москва Уфа Караганда Тверь Минск Казань"
# lst = str.split() # ['Москва', 'Уфа', 'Караганда', 'Тверь', 'Минск', 'Казань']
# for index in range(len(lst)):
#     print(index)
# print(lst)


# lst = [1, 2, 3, 4, 5]
# number_zero = 0
# lst[0] = number_zero
# print(lst)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# number = 5
# factorial = 1
#
# for i in range(1, number + 1):
#     factorial = factorial * i
#     print(factorial)


# words = ["Python", "JavaScript", "C++", "Java", "TypeScript", "PHP", "Rust", "Go"]
# str = ''
# for word in words:
#     str += ' ' + word
#
# print(str.strip())

# digs = [4, 3, 100, -53, -30, 1, 34, -8]
# for index in range(len(digs)):
#     if 10 <= abs(digs[index]) <= 99:
#         digs[index] = 0
# print(digs)

# digs = [4, 3, 100, -53, -30, 1, 34, -8]
#
# for i, d in enumerate(digs):
#     if 10 <= abs(d) <= 99:
#         digs[i] = 0
#
# print(digs)

# список замен для соответствующих русских букв
# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
#      'shch', '', 'y', '', 'e', 'yu', 'ya']
# # кодовое значение для первой буквы этого списка
# start_index = ord('а')
# print(start_index)
# # зададим строку и переменную slug, где будем формировать строку на латинице
# title = "Программирование------на Python - лучшее занятие"
# slug = ''
# #  преобразование в цикле, перебирая каждый символ исходной строки
# for s in title.lower():
#     if 'а' <= s <= 'я':
#         slug += t[ord(s) - start_index]
#     elif s == 'ё':
#         slug += 'yo'
#     elif s in ' !?:,.':
#         slug += '-'
#     else:
#         slug += s
# # удалим все подряд идущие символы дефиса
# while slug.count('--'):
#     slug = slug.replace('--', '-')
# # выводим результат
# print(slug)
#
# count = 0
# while True:
#     if count == 5:
#         break
#     count += 1

# Создание списка с парами чисел от 1 до 3
# pairs = [(x, y, z) for x in range(1, 4) for y in range(1, 4) for z in range(1,4)]
# Результат: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# print(pairs)
#
# lst_m_31 = [1, 3, 5, 7, 8, 10, 12]
# lst_m_30 = [4, 6, 9, 11]
# lst_m_28 = [2]
# m = 3
# n = 30
# if m in lst_m_31:
#     if n == 31:
#         print(m, n - 1)
#         print(m+1, end=" ")
#         print(1)
#     else:
#         print(m, n - 1)
#         print(m, n + 1)
# elif m in lst_m_30:
#     print()
# else:
#     print()

# str_in = "dfраdedрафысфсцусцура"
# sub_str = "ра"
# for index in range(len(str_in)):
#     if sub_str in str_in[index:index+len(sub_str)]:
#         print(index)

# lst = [1, 2, 3, 4, 5, 6]
# str = "ejhcvjsevhc"
#
# g_phone_number = "+7(928)714-49-14"
# sub_str = "5"
# flag = False
# for index, char in enumerate(g_phone_number):
#     print(index)
#     print(char)
#
# for char in g_phone_number:
#     print(char)
#
# for index in range(len(g_phone_number)):
#     print(index)
#     print(g_phone_number[index])
#
#
# numbers = [1, 2, 3, 4, 5, 6]
# iterator = iter(numbers)
#
# print(next(iterator))  # Выводит 1
# print(next(iterator))  # Выводит 2
# print(next(iterator))  # Выводит 3


#
# r = range(5)
# iterator = iter(r)
#
# for _ in range(3):
#     print(next(iterator))
#
# print()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# lst = ['one', 'two', 'three', 'four', 'five']
# r_lst = []
# for index in range(len(lst)):
#     r_lst.append(lst[index])
#     r_lst.append(lst[index])
#
# print(r_lst)

# Самостоятельная
# users = [
#     ["Александр", "2aB3c", "user"],
#     ["Михаил", "5Xy1Z", "user"],
#     ["Иван", "9mN7p", "admin"],
#     ["Дмитрий", "4Qw6R", "user"],
#     ["Андрей", "3sT9u", "admin"]
# ]
#
# questions = ["Сколько вам лет? ", "Чем любите заниматься? ", "Ваш любимый фильм? "]
# # дополнительные списки
# lst_man = []
# user_lst = []
#
# # использование цикла while
# while True:
#     print("\nВы входите в программу заного!\n")
#     login = input("Введите логин: ")
#     # использование условного оператора
#     if login.lower() == "выход":
#         print("Досвидания!")
#         break
#     password = input("Введите пароль: ")
#     # использование булевого флага
#     flag = False
#     # использование цикла for
#     for user in users:
#         if login == user[0] and password == user[1]:
#             if user[2] == "admin":
#                 flag = True
#                 print("Вы вошли как админ!")
#                 user_lst.append(input("Придумайте логин для нового пользователя: "))
#                 user_lst.append(input("Придумайте парольдля нового пользователя: "))
#                 user_lst.append(input("Укажите его роль для нового пользователя: "))
#                 print(f"Вы создали пользователя {user_lst}")
#             else:
#                 flag = True
#                 lst_man.append(login)
#                 for index in range(len(questions)):
#                     lst_man.append(input(questions[index]))
#     if not flag:
#         print("Неверный логин или пароль, попробуйте заного")
#         continue
#     if len(lst_man):
#         print(f"\nПривет, меня зовут {lst_man[0]}.")
#         print(f"Мне {lst_man[1]} лет, я люблю {lst_man[2]}.")
#         print(f"Мой любимый фильм - {lst_man[3]}.\n")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Напишите программу, которая будет запрашивать у пользователя количество студентов, их имена, фамилии и оценки по трем предметам.
# Программа должна вычислять среднюю оценку.
# Программа должна добавлять строку "низкая"/"средняя"/"высокая" в результирующий список с информацией студента исходя из средней оценки.
# Если меньше 8 - "низкая", от 8 до 10 - "средняя", от 10 и выше - "высокая".
# Для каждого студента должен формироваться список типа: [Имя студента, первая оценка, вторая оценка, третья оценка, средняя оценка, низкая/средняя/высокая]
# Программа должна выводить список всех студентов с их информацией.
# Пример вывода:
# Информация о студентах:
# 1. Ivan Petrov: Оценки: [8, 7, 9], Средняя оценка: 8.00 (средняя)
# 2. Sergey Ivanov: Оценки: [6, 5, 8], Средняя оценка: 6.33 (низкая)
# Так же программа должна вывести всех студентов с низкой оценкой.
# Пример вывода:
# Информация о студентах с низкой оценкой:
# 1. Sergey Ivanov - 6.33

# # Запрашиваем количество студентов
# students_count = int(input())
# # Результирующий список
# students = []
# # Счетчик для выхода из цикла
# count = 0
# # Цикл, который будет работать пока не введем всех студентов
# while count < students_count:
#     # Запрашиваем имя
#     name_student = input("name: ")
#
#     # Запрашиваем оценки по трем предметам
#     scores = [int(input(f"{i+1} score: ")) for i in range(3)]
#
#     # Средняя оценка студента
#     avg_score = sum(scores)/len(scores)
#
#     # Строка "низкая"/"средняя"/"высокая"
#     str_score = "низкая" if avg_score < 8 else "средняя" if avg_score < 11 else "высокая"
#
#     # Нужно помнить, что списки мы можем складывать только со списками
#     students.append([name_student] + scores + [avg_score] + [str_score])
#
#     count += 1
#
# print(students)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# n = 14
# for number in range(2, n):
#     if n % number == 0:
#         print("Число не простое")
#         break
#     else:
#         continue
# else:
#     print("Число простое")

# str = input()
# iterator = iter(str)
# temp = None
# while temp != " ":
#     temp = next(iterator)
#     print(temp)

# count = 1
# while count <= 3:
#     for i in range(1, 4):
#         print(i, end=' ')
#     count += 1

# for i in range(1, 4):
#     count = 1
#     while count <= 3:
#         print(i, end=' ')
#         count += 1

# for i in range(1, 4):
#     for j in range(0, 3):
#         print(i, end=" ")
#         print(j)
#     print()

# lst = [
#     [1, 2, 3, 4],
#     [2, 3, 4, 5],
#     [3, 4, 5, 6]
# ]
#
# for row in lst:
#     for number in row:
#         print(number, end=" ")
#
# lst1 = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# lst2 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
#
# r_lst = []
# for i in range(len(lst1)):
#     sublist = []
#     for j in range(len(lst2[i])):
#         print(f"{lst1[i][j]} + {lst2[i][j]}")
#         sublist.append(lst1[i][j] + lst2[i][j])
#     r_lst.append(sublist)
# print(r_lst)

# lst = [ "Я   помню  чудное    мгновенье",
# "Передо  мной    явилась   ты",
# "Как    мимолетное   виденье",
# "Как     гений   чистой  красоты"]
#
# for index, line in enumerate(lst):
#     while lst[index].count("  "):
#         lst[index] = lst[index].replace("  ", " ")
#
# print(lst)

# M = int(input("Введите количество строк: "))
# N = int(input("Введите количество столбцов: "))
#
# nested_list = []
# for i in range(M):
#     sublist = []
#     for j in range(N):
#         sublist.append(0)
#     nested_list.append(sublist)
#     print(nested_list[i])


# for i in range(M):
#     for j in range(N):
#         print(nested_list[i][j], end=' ')
#     print()

# for i in range(M):
#     for j in range(N):
#         nested_list[i][j] = 1
#         print(nested_list[i][j], end=" ")
#     print()

# for i in range(M):
#     for j in range(N):
#         print(nested_list[i][j], end=' ')
#     print()

# lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j], end='\t')
#     print()
#
# print()
#
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
#
# for row in lst:
#     for number in row:
#         print(number, end='\t')
#     print()

# lst = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]


# task = "12-11+30"
# task = task.replace(" ", "")
# result = ""
# for index in range(len(task)):
#     if task[index] == "+":
#         result = task[:index] + " " + task[index] + " " + task[index + 1:]
#     if task[index] == "-":
#         result = task[:index] + " " + task[index] + " " + task[index + 1:]
#
# print(result)

# numbers = [0 for number in range(1, 11)]
# print(numbers)
#
# squares = [i**2 for i in range(1, 11)]
# print(squares)

# Ввод чисел с клавиатуры и создание списка
# numbers = [int(i) for i in input().split()]
# print(numbers)

# # Список городов
# cities = ['Москва', 'Санкт-Петербург', 'Нью-Йорк', 'Лондон', 'Париж', 'Мадрид']
# # Создание списка городов, начинающихся с буквы "М"
# filtered_cities = [city for city in cities if city.startswith('М')]
# print(filtered_cities)

# Список чисел
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Создание списка четных чисел
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# Создание списка с парами чисел от 1 до 3
# pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
# pairs = []
# for x in range(1, 4):
#     for y in range(1, 4):
#         pairs.append((x, y))
# # Результат: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# print(pairs)

# # Преобразование двумерного списка в одномерный
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = [num for row in matrix for num in row]
# # Результат: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(flat_list)
#

# # Получение двумерного списка с помощью вложенного генератора списков
# matrix = [[i+j for j in range(3)] for i in range(3)]
# # Результат: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
# print(matrix)

# Возвести все значения двумерного списка в квадрат с помощью вложенного генератора списков
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# squared_matrix = [ [num**2 for num in row] for row in matrix]
# # Результат: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
# print(squared_matrix)

# # Транспонирование матрицы с использованием вложенных генераторов
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# # Результат: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# print(transposed_matrix)

# # Пример: Создание списка кубов чисел от 1 до 5 с использованием вложенного генератора списков
# cubes = [num ** 2 for num in [value + 1 for value in range(5)]]
# # Результат: [1, 8, 27, 64, 125]
# print(cubes)

# task = "12 + 13-5"
# task = task.replace("-", " - ")
# task = task.replace("+", " + ")
# # while "  " in task:
# #     task = task.replace("  ", " ")
# task = task.replace("  ", " ")
# print(task)

# task = "12 + 13 -5"
# i = 0
# # task = task[:i] + task[i+1:]
# while " " in task:
#     if " " in task[i]:
#         task = task[:i] + task[i+1:]
#     i += 1
#
# print(task)

# # Входные данные:
# scores_students = [[10, 11, 11], [11, 9, 12], [8, 12, 12]]
# names_students = [["Александр","Александров"], ["Михаил","Иванов"], ["Дмитрий","Петров"]]
#
# # Объединение в один список
# # [['Александр', 'Александров', 10, 11, 11], ['Михаил', 'Иванов', 11, 9, 12], ['Дмитрий', 'Петров', 8, 12, 12]] с помощью генератора списков.
# students = [names_students[i] + scores_students[i] for i in range(len(names_students))]
# print(students)
#
# # Добавление к каждому списку средней оценки с помощью обычного цикла. Округлив до одного знака после запятой.
# for index in range(len(students)):
#     students[index].append(round(sum(students[index][2:]) / len(students[index][2:]), 1))
# print(students)


# str = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890"
# lst = str.split()
# d = dict()
# for number in lst:
#     d[number[:2]] = [lst_number for lst_number in lst if lst_number[:2] == number[:2]]
#
# print(d)


