#SIMPLE CALCULATOR-->Basit Hesab Makinesi
#Vəzifə: İstifadəçidən iki ədəd daxil etməsini və toplama, çıxarma, vurma və ya bölmə əməliyyatlarını seçməsinə imkan verən sadə bir kalkulyator yaradın.

print('*****SIMPLE CALCULATOR*****')

num1=float(input("Birinci ededi daxil edin:"))
num2=float(input("Ikinci ededi daxil edin:"))
emeliyyat=input("Icra edilecek emeliyyati daxil edin(+,-,*,/):")

if emeliyyat=='+':
    print("Toplama emeliyyati:",num1+num2)
elif emeliyyat=='-':
    print('Cixma emeliyyati:',num1-num2)
elif emeliyyat=='*':
    print('Vurma emeliyyati:',num1*num2)
elif emeliyyat=='/':
    if num2 !=0: 
      print('Bolme emeliyyati:',num1/num2)
    else:
      print("Bolme emeliyyati icra edile bilmir. Cunki 0-a bolme yoxdur.")
else:
    print("simple_calculator islemir.") 

#Funksiyanin icinde de yazmaq olardi.