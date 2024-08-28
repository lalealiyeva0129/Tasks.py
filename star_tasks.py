#task1
# * * * *

# * * * *

# * * * *

# * * * *
n=4
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print("\n")
    
#Yeni bir setre kecmek ucun \n istifade edilir.

#task2
# *
# **
# ***
# ****
# *****
n=6
for i in range(n):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print(" ")
    
print("\n")

#task3
# *****
# ****
# ***
# **
# *

n=5
for i in range(n+1,1,-1):
    for j in range(0,i-1):
        print("*", end=" ")
    print("\t")


#task4
#1
#22
#333
#4444
#55555
x=6
for i in range(x):
    for j in range(i):
        print(i,end=" ")
    print("\t")
    
#task5
#1
#12
#123
#1234
#12345

n=7
for i in range(1,n):
    for j in range(1,i):
        print(j,end="")
    print("")
    
print("\n")  
 
 #task6
n="Python"
x=0
for i in n:
    x+=1
    print(n[0:x])
    
for i in n:
    x-=1
    print(n[0:x])
    
#task7
#11111
#2222
#333
#44
#5

n=5
x=0
for i in range(n,0,-1):
    x+=1
    for j in range(1,i+1):
        print(x,end=" ")
    print("\t")