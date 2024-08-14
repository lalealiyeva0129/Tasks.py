#list_task
#1 giris[1,2,3] cixis[3,2,1]
giris=[1,2,3]
cixis=giris[::-1]
print(cixis)
#2 bir list duzeldin onun uzunlugun da gosterin
a=[True,67," "]
print("Listin uzunlugu:",(len(a)))
#3 iki ededin max tap, hemcinin de min ucun yaza bilerik
a=4
b=7
if a>b:
    print("iki ededden a boyukdu:",a)
else:
    print("iki ededden b boyukdur:",b)
    
a=[2,5,66]
print(max(a))
#4 list hazirla ve onun butun elementlerin sil
task=[False,47,90]
task.clear()
print(task)
task=[False,47,90]
del task[:]
print(task)
#5 kistin tersine cevrilmesi
task1=[4,5,3,8,77]
task2=task1[::-1]
print(task2)