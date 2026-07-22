lst=[10.0,20.0,30.0,40.0,50.0]

result= map(lambda x:x*9/5 ,lst) 

for resultss in result:
        print(resultss)


print("\nnext section\n")

lst=[10.0,20.0,30.0,40.0,50.0]

result= lambda x:x*9/5 

for x in lst:
        print(result(x))