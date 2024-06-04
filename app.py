def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("The age can not be zero or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
