## thisset = {1, "salam" , 52 , True, "0"} setinin uzunluqunu teyin etmek 
## thisset = {1, "salam" , 52 , True, "0"} setine 0 ve false deyerleri daxil edib uzunlugunu cap etmek 
## her-hansi iki seti birlesdirmek 
## iki oxsar elementli setlerden ferqli elementleri cap etmek 
## setden element silmek 
## setin daxilindeki butun elementleri silmek 
## setdeki butun elementleri cap etmek 

#1
thisset = {1, "salam" , 52 , True, "0"}
print(len(thisset))
thisset.update(("false",0))
print(thisset)
#union() ve 
#different() ve - operatoru
#remove(), discard()
#clear()
#for i in thisset
for i in thisset:
    print(i)