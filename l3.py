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

def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Извлечение квадратного корня")
        print("6. Выйти")

        choice = input("Введите номер операции: ")

        if choice == '6':
            print("Выход из калькулятора.")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Введите первое число: "))
                if choice != '5':
                    num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: Вы ввели строку, введите число чтобы продолжить пользоваться калькулятором.")
                continue

            if choice == '1':
                print("Результат:", add(num1, num2))
            elif choice == '2':
                print("Результат:", subtract(num1, num2))
            elif choice == '3':
                print("Результат:", multiply(num1, num2))
            elif choice == '4':
                print("Результат:", divide(num1, num2))
            elif choice == '5':
                print("Результат:", square_root(num1))
        else:
            print("Ошибка: Неверный выбор операции. Пожалуйста, введите число от 1 до 6.")

if __name__ == "__main__":
    main()
