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
    if b == 0:
        print('ZeroDivisionError')
    else:
        result = a / b
        print(f'resul {a} / {b} = {result}')
elif operator != '+' or operator != '-' or operator != '*' or operator != '/':
    print('Vrong operator')
    operator = input('try agan: ')
    exit(1)