
try:
    # this will call finally method immediately
    with open("app.py") as file:
        print("The file has opened")
    age = int(input("Enter age: "))
    xfactor = 10/age
    # file.close()Non
except (ValueError, ZeroDivisionError) :
    print("You entered the wrong value")
    # file.close()Non
else:
    print("No exception thrown")
# finally:
#     file.close()

