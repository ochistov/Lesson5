'''
Creating of a text file, writing user-defined numbers, splitted by space to it.
Checking for the non-digit symbols in the list
---------------------------------------------------------------------------
Создание текстового файла, запись в него заданных пользователем чисел, 
разделённых пробелом. Проверка на наличие в строке символов, не являющихся
цифрами
'''
while True:
    try:
        numbers = input("Insert numbers, splitted by space: ").split()
        for number in numbers:
            number = float(number)
        with open("L5_task5.txt", "w", encoding = "utf-8") as file_output:
            print(*numbers, file=file_output)
    except:
        print("Your string consists a non-digit symbol!\nTry again")
        continue
    break

'''
Opening a previously created file, reading a numeric string from it, 
calculating the sum of numbers, displaying the result on the screen 
----------------------------------------------------------------------------
Открытие созданного ранее файла, чтение числовой строки из него, подсчёт 
суммы чисел, вывод результата на экран
'''
sum_of_numbers = 0
with open("L5_task5.txt", "r", encoding = "utf-8") as file_input:
    for string in file_input.readlines():
        for number in string.split():
            sum_of_numbers += float(number)
print(f"Here is a sum of numbers you entered: {sum_of_numbers}")