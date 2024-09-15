#PALINDROM
#Vəzifə: Bir sözün palindrom olub-olmadığını yoxlayan bir proqram yaradın.
#Palindrom nədir? Palindrom, tərsinə oxunduqda da eyni olan sözlərdir. Məsələn, "radar"

#Istifadeciden sozu alaq
Soz=input('Soz:')
#palindrom olub-olmamasini yoxlayaq
ters_soz=str(Soz[::-1])
if ters_soz==Soz:
    print(Soz,"sozu palindromdur.")
else:
    print(Soz, 'palindrom deyil.')
