#2
import logging
def write_file(fill_pass,data):
    try:
        with open(fill_path, 'w') as file:
            file.write(data)
    except Exception as e:
        logging.error(f'сталася помилка під час зачитування з файлу {fill-path}: {str(e)}
logging.basicConfig(level=logging.INFO)
write_file('output.txt', input('dвведіть що треба ввести в файл:'))