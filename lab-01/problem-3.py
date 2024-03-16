numbers = []

for i in range(10):
    numbers.append(int(input(f"[{i + 1}/10] Enter an integer.\n> ")))

largest_num = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > largest_num:
        largest_num = numbers[i]

print(f"The largest number is {largest_num}.")
