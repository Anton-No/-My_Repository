#2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.



with open('/Users/an/Documents/My_Repository/for GeekBrains/lesson_5/text_2.txt', 'r', encoding='utf-8') as f:
      my_line = f.readlines()
      for index, value in enumerate(my_line, 1):
            number_of_words = len(value.split())
            print(f'Строка {index} содержит {number_of_words} слов')