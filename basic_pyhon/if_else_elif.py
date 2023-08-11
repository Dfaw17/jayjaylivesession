# operator kondisi

print("Silahkan masukan angka")
angka = int(input())

if angka > 0 and angka < 5:
    print("nilai yangk amu masukan termasuk nilai kecil")
elif angka > 5 and angka < 9:
    print("nilai yang kamu masukan termasuk nilai besar")
elif angka > 9 and angka < 20:
    print("nilai yang kamu masukan termasuk nilai sangat besar")
else:
    print("nilai yang kamu masukan termasuk nilai tak terhingga")
