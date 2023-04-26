# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"
#
# some_list = [1, 2, 4, 3, 9, 8, 11, 0, 13]
# some_list.sort()
# result_list = []
# temp_list = []
# print(some_list)
# for i in range(0, len(some_list) - 1):
#     if some_list[i + 1] - some_list[i] == 1:
#         temp_list.append(some_list[i])
#     else:
#         temp_list.append(some_list[i])
#         result_list.append(temp_list)
#         temp_list = []
# if temp_list:
#     result_list.append(temp_list)
#
# if some_list[-1] - some_list[-2] == 1:
#     result_list[-1].append(some_list[-1])
# else:
#     result_list.append([some_list[-1]])
#
# print_list = []
# for i in result_list:
#     if len(i) > 1:
#         print_list.append(f'{i[0]}-{i[-1]}')
#     else:
#         print_list.append(i[0])
#         print(*print_list, sep=',')

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
#
# def get_result (a,b):
#     if (b == 1):
#         return a
#     return a * get_result(a, b - 1)
#
# print(get_result(a,b))

# Дана строка(возможно,пустая),состоящая из букв A-Z
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида :
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения:Если символ встречается 1 раз , он остается без изменений;
# Если символ повторяется более 1 раза , к нему добавляется количество повторений
import re
pattern = re.compile("[A-Z]+")
txt = str(input("Введите строку вида ""AAAABBBCCXYZD"": "))

def RLE(text):
    if not pattern.fullmatch(text):
        return "Error"
    count_dict = {}
    for i in range(0, len(text)):
        count=0
        key=text[i]
        if key in count_dict:
            count = count_dict.get(key)
        count= count+1
        count_dict[key]= count
    result_txt = ""
    for key, value in count_dict.items():
        result_txt = result_txt + key + str(value)
    return result_txt

print(RLE(txt))