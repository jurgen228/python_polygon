#   c approach to error handling


def validate_age(age):
    if age < 0 or age > 110:
        return False
    else:
        return True
    
child_age = int(input("Enter age:"))
bodybag_age = int(input("Enter age:"))
unboarn_age = int(input("Enter age:"))
maximus_age = int(input("Enter age:"))

if (validate_age(child_age)
    and validate_age(bodybag_age) 
    and validate_age(unboarn_age) 
    and validate_age(maximus_age)):
    print("Good boy.")
else:
    print("Zhalko maluka")

#   python approach to error handling

def validate_age(age):
    if age < 0 or age > 110:
        raise RuntimeError("I can't take it anymore.")

child_age = int(input("Enter age:"))
bodybag_age = int(input("Enter age:"))
unboarn_age = int(input("Enter age:"))
maximus_age = int(input("Enter age:"))

try:
    validate_age(child_age)
    validate_age(bodybag_age)
    validate_age(unboarn_age)
    validate_age(maximus_age)
    print("Good boy")
except RuntimeError as exception: 
    print("Zhalko maluka:", exception)


    
