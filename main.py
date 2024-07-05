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

numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [10, 20, 30, 40]
print(numbers)