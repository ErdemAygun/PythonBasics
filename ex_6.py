"""
age = int(input('please provide your year of birth:'))

if age <= 2004:
    print('you are of legal age!')

else:
    print('you are under legal age')

"""

year_of_birth = int(input('please provide your year of birth:'))

age = 2022 - year_of_birth

if age >= 18:
    print('you are of legal age!')

else:
    print('you are under legal age')