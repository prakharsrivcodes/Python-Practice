
try:
    number = int(input("enter a number"))
    print(1/number)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Please enter a number other than zero")
finally:
    print("do some cleanup here")