import random
import logging
def rand_file(file_path,num ):
    try:
        with open(fill_path, 'w') as file:
            for i in range(num):
                data = random.randint(1, 100)
                 file.write(str(data)+ '\n')
                #далі допишіть логуваняя
    except:
logging.basicConfig(level= logging.INFO)
def rand_file('input_random.txt',int(input(('кількість згенерованих чисел: ')))
