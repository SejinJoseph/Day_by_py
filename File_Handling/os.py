import os 
#os.chdir("D:/Python/Basic_py")
#print(os.getcwd())

#print(os.listdir())

#os.mkdir("stuff.txt")

#print(os.listdir())
file="test-para.txt"

if (os.path.exists(file)):
    print(f"the file {file} is exist")

else:
     print(f"the file {file} is not exist")

print(os.path.isfile(file))
print(os.path.isdir(file))