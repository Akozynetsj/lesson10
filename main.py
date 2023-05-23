import  logging

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add(self, a, b):
        result = a + b
        self.logger.info(f" {a} + {b} = {result}")
        return result
        def sub(a, b):
            result = a - b
        self.logger.info(f" {a} - {b} = {result}")
        return result

        def mult(a, b):
            self.logger.info(f" {a} * {b} = {result}")
        return result
        def div(self , b):
            result = a/b
            if b == 0:
                try:
                    a / b
                except ValueError:
            else:
                raise ValueError('POMULKAAA')
                return add, sub, mult, div
                add, sub, mult, div = calc()
calc1 = Calculator()
calc1.add(6,7)
calc1.div(3, 1)
calc1.mult(4,6)
calc1.sub(14,4)