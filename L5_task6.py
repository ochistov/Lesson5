######Вариант решения с использованием регулярных выражений######
'''
Creation of an empty dictionary, opening a file with data, line-by-line 
writing from the file to the "all_file" variable. Looping through a list 
of strings obtained earlier, searching for numbers in the list, forming 
a list of them. Summing up list items. Adding the name of the disciplines 
and the received sums of hours to an empty dictionary. 
Displaying the result on the screen 
-----------------------------------------------------------------------------
Создание пустого словаря, открытие файла с данными, построчная запись из файла 
в переменную "all_file". Перебор списка из строк, полученного ранее, поиск в 
списке чисел, формирование списка из них. Суммирование элементов списка. 
Добавление названия предметов и полученных сумм часов к пустому словарю. 
Вывод результата на экран
'''
import re
final_dict = {}
with open("L5_task6.txt", "r", encoding = "utf-8") as input_file:
    all_file = input_file.readlines()
    for discipline in all_file:
        sum_hours = 0
        hours = re.findall(r'\d+', discipline)
        for hour in hours:
            sum_hours += float(hour)
        final_dict[(discipline.split()[0]).replace(":","")] = sum_hours #replace - костыль для отсечения двоеточия от названия :D
    print(final_dict)


######Вариант решения без использования регулярных выражений######
'''
Creation of an empty dictionary, opening a file with data, line-by-line 
writing from the file to the "all_file" variable. Creation of an empty string. 
Loop over each line in a list of strings character by character. If the next 
character is a digit, append it to an empty string, check the next character, 
and if it is a digit too, add it to the previous one. If the next character is not 
a digit or the string has ended, applying float() to the new string and 
adding the resulting number to the list.
------------------------------------------------------------------------------
Создание пустого словаря, открытие файла с данными, построчная запись из файла 
в переменную "all_file". Создание пустой строки. Посимвольный перебор каждой 
строки в списке из строк. Если очередной символ - цифра, добавление его к 
пустой строке, проверка следующего символа и если он - цифра, добавление его 
к предыдущему. Если очередной символ - не цифра или строка закончилась, 
применение к новой строке float() и добавление полученного числа к списку.
'''
final_dict = {}
with open("L5_task6.txt", "r", encoding = "utf-8") as input_file:
    all_file = input_file.readlines()
    for discipline in all_file: 
        sum_hours = 0
        hours = [] 
        i = 0
        while i < len(discipline):
            numb = ''
            a = discipline[i]
            while '0' <= a <= '9':
                numb += a
                i += 1
                if i < len(discipline):
                    a = discipline[i]
                else:
                    break
            i += 1
            if numb != '':
                hours.append(float(numb))
                '''
                Эта часть кода полностью совпадает с заполнением и выводом словаря
                в варианте решения с использованием регулярных выражений
                '''
        for hour in hours:
            sum_hours += float(hour)
        final_dict[(discipline.split()[0]).replace(":","")] = sum_hours
    print(final_dict)  