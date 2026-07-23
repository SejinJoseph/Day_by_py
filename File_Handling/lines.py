f=open("test_para.txt","r")
para=f.read()
print(para)
f.close()


f=open("test_para.txt","r")
para=f.readline()
print( para)
f.close()

f=open("test_para.txt","r")
para=f.readlines(1)
print( para)
f.close()
