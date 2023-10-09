a = float(input('Enter first num: '))
b = float(input('Enter second num: '))
operator = input('Enter operator: ')

if operator == '+':
    result = a + b
    print(f'resul {a} + {b} = {result}')
elif operator == '-':
    result = a - b
    print(f'resul {a} - {b} = {result}')
elif operator == '*':
    result = a * b
    print(f'resul {a} * {b} = {result}')
elif operator == '/':
    try:
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль недопустимо")
        result = a / b
        print(f'Результат {a} / {b} = {result}')
    except ZeroDivisionError as e:
        print(e)
else:
    print('wrong operator')