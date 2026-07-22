lst=[10,20,30,40,50,60,70,80,90]

print("The list value:",lst)

#result=filter(lambda x:x>=40,lst)
#for results in result:
 #   print(results)



def check(x):
    return(x>=40)


def filt(y):
   return(filter(check,y))
    

for fi in filt(lst): 
    print(fi)

