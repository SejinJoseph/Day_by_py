try:
    num=int(input("Enter a Number:"))
    div=100/num

except TypeError:
    print("you Enter a Wrong Data_Type ")
    
except ZeroDivisionError:
    print("it is not divisible by 0 ")
except Exception:
    print("some thing went wrong")

finally:
    print("You Are A Good Programmer")
