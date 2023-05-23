import logging #стандартна бібліотека для логування перебігу програми
logging.basicConfig(level=logging.DEBUG,
                    filename= "logs.log",
                    filemode= 'w',
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug")
logging.info("info")
logging.error("погано написав програму error")
logging.warning("warning")
logging.critical("critical")
try:
    print(10/0)
except Exception:
    logging.exception('помилоочкаааааааа')
#факторіал числа

def factorial(n):
    logging.info(f'розпочато обчислення факторіалу числа {n}')
    result = 1
    for i in range(1, n + 1):
        result *= i
    logging.info(f'закінчено обчислення факторіалу числа {n} Результат виконання {result}')
    return result
logging.basicConfig(level= logging.INFO)
factorial(5)