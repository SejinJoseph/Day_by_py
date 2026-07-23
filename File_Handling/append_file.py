f=open("laptop.txt","a")
f.write("\nApple\n")
f.write("Lenovo\n")
f.write("Dell\n")
f.close()

f=open("laptop.txt")
content=f.read()
print(content)