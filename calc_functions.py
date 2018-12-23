import math


# def check_num():
#     num = entry.get()
#     if num.isdigit() == False:
#         mb.showerror("Error", "Должно быть введено число")
#     else:
#         entry.delete(0, END)
#         label['text'] = num


def addition(a, b):
    """Сложение"""
    return a + b


def subtraction(a, b):
    """Вычитание"""
    return a - b


def multiply(a, b):
    """Умножение"""
    return a * b


def division(a, b):
    """Деление"""
    try:
        return a / b
    except ZeroDivisionError:
        return 'Error: Division by zero'


def sq_root(a):
    """Извлечение квадратного корня"""
    return math.sqrt(a)


if __name__ == '__main__':
    test_add = addition(34, 56)
    if test_add == 90:
        print('Addition test OK!')
    else:
        print('Addition test Failed!')

    test_sub = subtraction(23, 45)
    if test_sub == -22:
        print('Sub test OK!')
    else:
        print('Sub test Failed!')

    test_mult = multiply(6, 66)
    if test_mult == 396:
        print('Multiply test OK!')
    else:
        print('Multiply test Failed!')

    test_div = division(35, 5)
    if test_div == 7:
        print('Division test OK!')
    else:
        print('Division test Failed!')

    test_div_0 = division(35, 0)
    if test_div_0 == 'Error: Division by zero':
        print('Zero division test OK!')
    else:
        print('Zero division test Failed!')

    test_sqrt = sq_root(4)
    if test_sqrt == 2:
        print('Square root test OK!')
    else:
        print('Square root test Failed!')

