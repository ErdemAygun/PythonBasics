# f(x) = x + 1
# f(1) = 2

# str - string data type

# literal - whatever value you putting into the code

print('Hello World!')
print("Hello World!")

print("Book 'Moby dick' is great")
print("Book \"Moby dick\" is great")

# int - integer data type, unlimited precision
print(100)
print(-23)

# float
print(2.5)
print(-4.3)
print(2.0)

# 2 different type than 2.0

print(3E5) # 3*10^5 - scientific notation

#bool - boolean type
print(True)
print(False)

# None - in python we have None, not NULL
print(None)

print(type(10))
print(type(10.0))
print(type("10"))

# OPERATORS
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 ** 3)
print(10 % 3)

# the process of connecting strings together: concatenation
print("I see" + "the cat")

print("Tom" * 10)

# variables
number = 10  # create a variable named number and assign 10 to this variable
print(number)

number = 'john'
print(number)

first_name = 'john'
print(first_name)

# concatenating different types
print('My age is ' + str(10))

# f string - we have to put f before quotes
rate = 10.352
last_name = 'Doe'
print(f'My last name is {last_name} and my rate is {rate}')
print(f'My last name is {last_name} and my rate is {rate:.2f}')
print(f'My last name is {last_name} and my rate is {rate:.1f}')
print(f'My last name is {last_name} and my rate is {rate:10.1f}')
print(f'My last name is {last_name} and my rate is {rate:_>10.1f}')

# Comparison operators

print(1 == 1)
print(1 < 2)
print(32 != 23)
print(23 > 21)
print(32 <= 23)
print(23 >= 12)

# Logical operators

print(True and True)
print(False or True)
print(not False)

# Conditional statements

number = int(input('Provide a number:'))

if number > 0:
    print('Yey! We have a number greater than 0')
elif number == -10:
    print('Wow! My favourite negative number!')
elif number == -20:
    print('Nice, -20')
elif number == -30:
    print('Nice shoot')
else:
    print('Nay! The number is lower than 0!!!')
print("thank you for using my script!")

# Loops - while

i = 0

while i < 10:
    print(i)
    i += 1   #i = i + 1

