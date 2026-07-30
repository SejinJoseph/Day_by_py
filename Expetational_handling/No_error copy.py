try:
    n = int(input("Enter a number: "))

    div=10/n
except ZeroDivisionError:
    print("0 can't divide idiot!!!")

finally:
    print("you are a good programmer")