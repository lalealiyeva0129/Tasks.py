#alizadelale
print("task2")
#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5   
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=(" "))
    print("")
    
print("task3")
# Istifadeciden eded qebul edib, 1 den bu edede qeder olan elementlerin cemini yazdirmaq.
x=int(input("Zehmet olmasa ededi daxil edin:"))    
print(x)
for i in range(1,x+1):
    if i>0:
       s=(((x+1)*x)/2)
print("Cem=",s)

print("task4")
#Verilmis ededin vurma cedvelin qurun.
n=7
for i in range(1,11,1):
    x=i*n
    print(x)

print("task5")
# Nömrə beşə bölünməlidir
 #Əgər rəqəm 150-dən çox olarsa, onu keçin və növbəti nömrəyə keçin
 #Əgər rəqəm 500-dən çox olarsa, döngəni dayandırın 
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5==0:
        if i>=150:
            continue
            if numbers<500:
                break
        print(i)
 
print("task6")
#Bir ədəddəki rəqəmlərin ümumi sayını hesablayın
y=input("Zehmet olmasa ededi daxil edin:")
for i in (y):
    print(int(i))
    
print("task7")
#Aşağıdakı nümunəni çap edin
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=(" "))
    print("")
    
print("task8")
#list1=[10,20,30,40,50] donguden istifade ederek  siyahini ters qaydada cap edin.
list1=[10,20,30,40,50]
list2=[]
for i in list1:
    list2.append(i)
    list2.sort(reverse=True)
    print(list2)
    for x in list2:
        print(x)

print("task9")
#for döngəsindən istifadə edərək -10-dan -1-ə qədər rəqəmləri göstərin   
for i in range(-10,0,1):
    print(i)
    
print("task10 ") 
# For döngəsinin uğurla icrasından sonra “Bitti” mesajını göstərmək üçün else blokundan istifadə edin.
for i in range(5):
    print(i)
else:
    print("Bitdi!")
    
print("task11") 
#Bir diapazonda bütün sadə ədədləri göstərmək üçün proqram yazın
print("25 ile 50 arasinda olan sade ededler:")   
for i in range(25,50):
    if i%2!=0 and i%3!=0 and i%7!=0 and i%5!=0:
        print(i)

    
print("task12")
#Fibonacci seriyasını 10 terminə qədər göstərin:0 1 1 2 3 5 8 13 21 34
num1, num2 = 0, 1
print("Fibonacci ardicilligi:")
for i in range(10):
    print(num1, end="  ")
    n = num1 + num2
    num1 = num2
    num2 = n
    
print("\n")
print("task13")
# Verilmiş ədədin faktorialını tapın
n=int(input("ededi daxil edin:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)

"""   
print("task14")
#Tam ədədi tərsinə çevirin. Verildi :76542 Gözlənilən nəticə:24567
n=int(input("ededi daxil edin:"))
for i in n:
    print(i)"""

    
print("task15")
#Tək indeks mövqelərində mövcud olan verilmiş siyahıdan elementləri çap edin
my_list=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
   print(i)   
    
print("\n") 
print("task16")
#1-dən verilmiş ədədə qədər bütün ədədlərin kubunu çap etmək üçün Python proqramı yazın.
n=int(input("Daxil edilen eded:"))
for i in range(1,n+1):
    x=i*i*i
    print("Yeni eded:",i,"Yeni ededin kubu ise:",x)
    
print("task17")
#N həddə qədər sıraların cəmini hesablamaq üçün proqram yazın. Məsələn n = 5 serial halına gələcək2 + 22 + 222 + 2222 + 22222 = 24690
s=0
for i  in range(1, 5):
    s+=int('2'*i)
print(s)

print("task18")
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*
for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print("")
    
for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print(" ")
 