people_count = int(input())
lift =[int(i) for i in input().split()]

for n in range(len(lift)):
    while lift[n] < 4:
        if people_count <= 0:
            break
        lift[n] += 1
        people_count -= 1

empty_slots_left = False
for wagon in lift:
    if wagon < 4:
        empty_slots_left = True
        break

if people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")
else:
    if empty_slots_left:
        print("The lift has empty spots!")

lift = [str(i) for i in lift]
print(" ".join(lift))
