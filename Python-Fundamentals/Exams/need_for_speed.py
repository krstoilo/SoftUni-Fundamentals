cars_count = int(input())
cars = {}
for i in range(cars_count):
    car = input().split("|")
    cars[car[0]] = []
    cars[car[0]].append(int(car[1]))
    cars[car[0]].append(int(car[2]))

command = input()
while command != 'Stop':
    token = command.split(" : ")
    if "Drive" in command:
        car = token[1]
        distance = int(token[2])
        fuel = int(token[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif "Refuel" in command:
        car = token[1]
        fuel = int(token[2])
        if cars[car][1] + fuel >= 75:
            current_fuel = cars[car][1]
            cars[car][1] = 75
            print(f"{car} refueled with {75 - current_fuel} liters")
        else:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif "Revert" in command:
        car = token[1]
        km = int(token[2])
        if cars[car][0] - km <= 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] -= km
            print(f"{car} mileage decreased by {km} kilometers")
    command = input()

for car, stats in sorted(cars.items(), key=lambda x: ((-x[1][0]), x[0])):
    print(f"{car} -> Mileage: {stats[0]} kms, Fuel in the tank: {stats[1]} lt.")
