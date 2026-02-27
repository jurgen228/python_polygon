try:
    first = int(input("Enter number:"))
    second = int(input("Enter number:"))
    print(first*second)
except ValueError:
    print("ERROR: only integer input is allowed")
