######    Так как в прошлом задании уже делал    ######
###### вариант без re, в этом решил использовать ######
######            только вариант с re            ######
'''
Opening a file, reading data line by line. Searching a string for numbers 
using the "re" module, checking the firm's profitability, generating a list 
with the profits of all firms. Adding the name of the company and its 
profit / loss to the final dictionary. Calculating the average profit. 
Formation of the final list containing a dictionary with profits / losses 
of companies and a dictionary with an average profit. 
------------------------------------------------------------------------------
Открытие файла, построчное чтение данных. Поиск в строке чисел с 
использованием модуля "re", проверка прибыльности фирмы, формирование 
списка с прибылями всех фирм. Добавление названия фирмы и её прибыли/убытка 
в итоговый словарь. Подсчёт среднего значения прибыли. Формирование итогового 
списка, содержащего словарь с прибылями/убытками фирм и словарь 
со средней прибылью. 
'''
import re, json, numpy
with open("L5_task7.txt", "r", encoding = "utf-8") as input_file:
    all_profits = []
    firms_and_profits = {}
    average_profit = {}
    all_file = input_file.readlines()
    for firm in all_file:
        all_money = re.findall(r'\d+', firm)
        if (float(all_money[0]) - float(all_money[1])) > 0:
            profit = float(all_money[0]) - float(all_money[1])
            firms_and_profits[firm.split()[0]] = profit
            all_profits.append(profit)
        else:
            loss = float(all_money[0]) - float(all_money[1])
            firms_and_profits[firm.split()[0]] = loss
    average_profit['average_profit'] = numpy.mean(all_profits) #коварный подсчёт среднего арифметического с использованием модуля numpy :D
#    print(firms_and_profits)
#    print(average_profit)
final_list= [firms_and_profits, average_profit]

'''
Сохранение результата в json файл
--------------------------------------------------------------------------
Saving the result to a json file 
'''
with open("L5_task7.json", "w", encoding = "utf-8") as output_file:
    json.dump(final_list, output_file, ensure_ascii = False) #ensure_ascii = False для корректного отображения кириллицы