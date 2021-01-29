'''
Opening a text file, writing its contents to a variable
--------------------------------------------------------------
Открытие текстового файла, запись его содержимого в переменную
'''

with open("L5_task3.txt", "r", encoding = "utf-8") as input_file:
    content = input_file.readlines()

'''
Creation of a list from which further output will occur
Create a variable that will contain the amount of salaries required
to calculate the average income of employees 
--------------------------------------------------------------------------
Создание списка, из которого в дальнейшем будет происходить вывод
Создание переменной, которая будет содержать сумму зарплат, необходимую 
для расчёта средней величины дохода сотрудников
'''
fin_list = []
sum = 0
'''
Line-by-line check of the content of the content variable, if the conditions 
are met adding the last name of the employee to the final list. 
Calculation of the amount of salaries, displaying on the screen final list 
and average income 
--------------------------------------------------------------------------
Построчная проверка содержимого переменной content, в случае соблюдения условий
добавление фамилии сотрудника к итоговому списку. Подсчёт суммы зарплат, вывод
на экран итогового списка и средней величины дохода
'''
for string in content:
    a = string.split()
    if int(a[1]) < 20000:
        fin_list.append(a[0])
    sum += int(a[1])
print(f"There are empoyees with salary lower then 20 000 rub: {', '.join(x for x in fin_list)}\nEverage income of employees is {sum/(len(content))} rub")