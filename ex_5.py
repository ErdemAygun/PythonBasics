"""
number = int(input("Please write a number:"))

result = (number % 2) != 0, (number % 3) == True, number > 10 or number == 7

print(f'Result: {result}')

"""

number = int(input("Please write a number:"))

result = (number % 2 != 0 and number % 3 == 0 and number > 10) or number == 7

print(f'Result: {result}')
