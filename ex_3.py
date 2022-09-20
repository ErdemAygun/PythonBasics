city_a = input("please write the first city:")
city_b = input("please write the second city:")

fuel_price = float(input("please write the fuel price:"))

fuel_consumption = float(input("please write the fuel consumption price:"))

distance = 420

cost = distance * fuel_consumption / 100.0 * fuel_price

print(f"The cost of from {city_a} to {city_b} is {cost} PLN")