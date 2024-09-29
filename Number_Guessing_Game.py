mal_qiymeti=input("Malin qiymeti:")

if mal_qiymeti == range(50,100):
    print("Malin qiymeti endirimle",mal_qiymeti-(mal_qiymeti*20)/100,"azn oldu.")
elif mal_qiymeti == range(100,150):
    print("Malin qiymeti",mal_qiymeti-(mal_qiymeti*30)/100,"azn oldu.")
else:
    print("Endirim movcud deyil.")    