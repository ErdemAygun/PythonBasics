""""
first_number = int(input('enter the first number:'))
second_number = int(input('enter the second number:'))
operation = input('select one of the opertaion (+,-,*,/):')

if operation == '+':
    print(f'Result: {first_number + second_number}')
elif operation == '-':
    print(f'Result: {first_number - second_number}')
elif operation == '*':
    print(f'Result: {first_number * second_number}')
elif operation == '/':
    print(f'Result: {first_number / second_number}')
else:
    print('unreadable operation')

"""
while True:
    user_input = input('enter the first number: or end to stop')
    if user_input == 'end':
        break

    first_number = int(user_input)
    second_number = int(input('enter the second number:'))
    operation = input('select one of the opertaion (+,-,*,/):')

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        result = first_number / second_number
    else:
        result = None

    if result is None:
        print('unreadable operation')
    else:
        print(f'{first_number} {operation} {second_number} = {result}')
