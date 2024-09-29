import random
a=random.randrange(1,10)
b=int(input("eded daxil et:"))
while a!=b:
 if a>b:
        print("Texmininiz cox boyukdu.")  
        b=int(input("eded daxil et:"))
 elif a<b:
      print("texmin cox kicikdi")
      b=int(input("eded daxil et:"))
print(a)