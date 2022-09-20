day_number = 1
temperature_sum = 0

while day_number <= 7:
    temperature_sum += int(input(f'Provide the temperature for the day {day_number}:'))
    day_number += 1
average_temperature = temperature_sum / 7

print(f'average temperature for the week: {average_temperature}')
