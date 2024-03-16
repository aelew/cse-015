numbers = []

for i in range(10):
    numbers.append(int(input(f"[{i + 1}/10] Enter an integer.\n> ")))

largest_odd_num = numbers[0]
for i in range(1, len(numbers)):
    num = numbers[i]
    if num % 2 != 0 and (numbers[i] > largest_odd_num or largest_odd_num % 2 == 0):
        largest_odd_num = numbers[i]

if largest_odd_num % 2 == 0:
    print("No odd numbers were entered")
else:
    print(f"The largest odd number is {largest_odd_num}.")
