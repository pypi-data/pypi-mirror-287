def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Деление на ноль невозможно"
    return a / b

# class CalcTest:
#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def subtract(a, b):
#         return a - b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

#     @staticmethod
#     def divide(a, b):
#         if b == 0:
#             raise ValueError("Деление на ноль невозможно")
#         return a / b