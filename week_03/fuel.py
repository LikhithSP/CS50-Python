while True:
    try:
        x, y = input("Fraction: ").split("/")
        if int(x) <= int(y):
            int(x)/int(y)
            break
    except (ValueError, ZeroDivisionError):
        pass


# Outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank
if int(x)/int(y) >= 0.99:
    print("F")
elif int(x)/int(y) >= 0.75:
    print("75%")
elif int(x)/int(y) >= 0.60:
    print("67%")
elif int(x)/int(y) >= 0.50:
    print("50%")
elif int(x)/int(y) >= 0.30:
    print("33%")
elif int(x)/int(y) >= 0.25:
    print("25%")
else:
    print("E")
