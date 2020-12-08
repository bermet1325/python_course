def calculate():
    while True:
       operation = input('''
Пожалуйста введите математическую операцую,которую вы хотите:
    + для сложения
    - для вычитания
    * для умножения
    / для деления
''')

       a = int(input('Введите первое число: '))
       b = int(input('Введите второе число: '))

       if operation == '+':
           print('{} + {} = '.format(a, b))
           print(a + b)

       elif operation == '-':
           print('{} - {} = '.format(a, b))
           print(a - b)

       elif operation == '*':
           print('{} * {} = ' .format(a, b))
           print(a*b)

       elif operation == '/':
           print('{} / {} = '.format(a, b))
           print(a/ b)

       else:
           print('Ошибка.')

calculate()