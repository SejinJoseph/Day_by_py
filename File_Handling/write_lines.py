f=open("test-para.txt","w")

lines=[
   " Python is a powerful and easy-to-learn programming language.\n"
"It is widely used for web development, data science, and artificial intelligence.\n"
"Learning Python helps you build real-world applications.\n"
"Practice every day to improve your programming skills.\n"
]
    
f.writelines(lines)
f.close()
