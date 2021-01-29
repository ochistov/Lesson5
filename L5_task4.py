'''
Creating a dictionary for translating English numbers into Russian 
-----------------------------------------------------------------------------
Создание словаря для перевода английских числительных на русский язык
'''
translate = {"one" : "один", 
             "two" : "два",
             "three" : "три",
             "four" : "четыре"}

'''
Simultaneous opening of original and final test files, line by line
reading the original, replacing English numerals with Russian using
the previously created dictionary, line by line output of the result to the 
final text file 
-----------------------------------------------------------------------------
Одновременное открытие исходного и конечного тестовых файлов, построчное 
чтение исходного, замена английских числительных на русские с использованием
созданного ранее словаря, построчный вывод результата в конечный текстовый файл
'''

with open("L5_task4_part1.txt", "r", encoding = "utf-8") as file_input:
    with open("L5_task4_part2.txt", "w", encoding = "utf-8") as file_output:
        for line in file_input:
            for word in line.split():
                if word.lower() in translate.keys():
                    print(*[elem.replace(word, translate[word.lower()].title()) for elem in line.split()], 
                          file = file_output)
