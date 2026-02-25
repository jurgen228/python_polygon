# numbers list
# user enters number x
# find two numbers in list in sum x
# all range parameters studieren
numbers = [5, 7, 1, -3]


x_number = int(input("Enter number: "))


print(f"number of elements: {len(numbers) - 1}")


for i in range(len(numbers) - 1):
    break_condition = False
    # if x_number == numbers[0] + numbers[1]:
    #     print("Gefinden.")
    # if x_number == numbers[0] + numbers[2]:
    #     print("Gefinden.")
    for j in range(i + 1, len(numbers)):
        if x_number == numbers[i] + numbers[j]:
            print(f"Gefinden: {numbers[i]} and {numbers[j]}")
            break_condition = True
            break
    if break_condition:
        break