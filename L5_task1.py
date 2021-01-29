'''
Opening a test file for overwriting (if it is missing
file is created), recording line by line lines specified by the user through the function
input(), outputting the result line by line to the created text file. Stop typing
made by entering an empty line (by pressing the Enter key) 
-----------------------------------------------------------
Открытие тестового файла для перезаписи (в случае его отсутствия
файл создаётся), запись построчно строк, заданных пользователем через функцию 
input(), вывод результата построчно в созданный текстовый файл. Остановка ввода
производится вводом пустой строки (нажатием клавиши Enter)
'''
with open("L5_task1.txt", "w", encoding = "utf-8") as output_file:
    data_for_file = ' ' #изначальное значение переменной для срабатывания "стопера" ввода
    i = 1 #переменная для нумерации строк на вводе
    while data_for_file != '': #проверка условия прерывания (введена ли пустая строка)
        data_for_file = input(f"Please enter {i} string\nFor finish insert nothing (just press 'Enter'): ")
        output_file.writelines(data_for_file+"\n") #запись строки в файл, \n для построчной записи
        #print(data_for_file, file = output_file) #ещё один вариант построчной записи в файл
        i += 1