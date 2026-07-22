def num():
    x=int(input("Enter a number x:"))
    y=int(input("enter a number y:"))

    c=x+y
    return (c)
result=num()
print(result)



def name():
    x=str(input("Enter the first name:"))
    y=str(input("Enter the last name:"))

    x=x.capitalize()
    y=y.capitalize()
    print(f"{x}  {y}")
    
name()