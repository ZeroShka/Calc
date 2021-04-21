input_number = float(input('Введите число:'))
Calculate = True
while(Calculate):
    operation = input(f'{input_number} ')
    operation = operation.split()
    try:
        if (operation[0] == '+'):
            input_number = input_number + float(operation[1])
        elif (operation[0] == '-'):
            input_number = input_number - float(operation[1])
        elif (operation[0] == '*'):
            input_number = input_number * float(operation[1])
        elif (operation[0] == '/'):
            if (operation[1] != '0'):
                input_number = input_number / float(operation[1])
            else:
                print('Делить на ноль нельзя XD')
        elif (operation[0] == '**'):
            input_number = input_number ** float(operation[1])
        elif (operation[0] in 'cC'):
            input_number = 0
        elif (operation[0] == '='):
            Calculate = False
        else:
            print('Не верная операция')
    except:
        print('Что-то пошло не так...')
print(f'Ответ {input_number}')
