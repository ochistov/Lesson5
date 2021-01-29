'''
Opening and reading a text file line by line, displaying the number of lines
and the number of words in each line 
----------------------------------------------------------------------------
Открытие и чтение построчно текстового файла, вывод количества строк
и количества слов в каждой строке
'''

with open("L5_task2.txt", "r", encoding = "utf-8") as input_file:
    content = input_file.readlines()
    print(f"There are {len(content)} strings in the file")
    i = 1 #счётчик для нумерации строк
    for string in content:
        print(f"There are {len(string.split())} words in {i} string")
        i += 1