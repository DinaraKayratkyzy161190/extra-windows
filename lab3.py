import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ошибка: деление на ноль"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Ошибка: невозможно извлечь корень из отрицательного числа"

def regression(x, y):
    # Ваш код для регрессии
    pass

def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Извлечение корня")
        print("6. Регрессия")
        print("7. Выйти из калькулятора")

        choice = input("Введите номер операции: ")

        if choice == '7':
            print("Выход из калькулятора.")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Введите первое число: "))
                if choice != '5':
                    num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: введите числовое значение.")
                continue

            if choice == '1':
                print(f"Результат: {add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Результат: {square_root(num1)}")
            elif choice == '6':
                print("Регрессия: Ваш код здесь")  # Добавьте свой код для регрессии

        else:
            print("Ошибка: выберите правильную операцию (от 1 до 7).")

if __name__ == "__main__":
    calculator()
