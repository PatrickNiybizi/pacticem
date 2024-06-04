try:
    age = int(input("Enter age: "))
except ValueError:
    print("You entered the wrong value")
else:
    print("No exception thrown")
print("Execution continue")

