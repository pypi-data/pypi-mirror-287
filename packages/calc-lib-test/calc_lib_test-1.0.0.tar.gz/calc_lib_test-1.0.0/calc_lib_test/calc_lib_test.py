class __calc_test__:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    # Запрос ввода у пользователя
    a = float(input("Введите 1 число: "))
    b = float(input("Введите 2 число: "))

    # Использование методов класса для выполнения операций
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    try:
        print(f"{a} / {b} = {divide(a, b)}")
    except ValueError as e:
        print(e)

    input("Нажмите Enter, чтобы закрыть программу...")
