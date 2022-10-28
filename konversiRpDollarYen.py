# Konversi mata uang Rupiah, Yen, Dollar
print("================================================")
print("1. Koversi Rupiah ke Yen")
print("2. Konversi Yen ke Rupiah")
print("3. Konversi Yen ke Dollar")
print("4. Konversi Dollar ke Yen")
print("5. Konversi Rupiah ke Dollar")
print("6. Konversi Dollar ke Rupiah")
print("=================================================")
tanya = int(input("Pilih konversi: "))

if tanya == 1:
    rupiah = int(input("Masukkan nilai mata uang Rupiah:Rp. "))
    hasil = rupiah/105
    print(f"Rp.{rupiah} sama dengan {int(hasil)} yen")
elif tanya == 2:
    yen = int(input("Masukkan nilai mata uang Yen:Y. "))
    hasil = yen * 105
    print(f"Y.{yen} sama dengan {int(hasil)} rupiah")
elif tanya == 3:
    yen = int(input("Masukkan nilai mata uang yen:Y. "))
    hasil = yen/133
    print(f"Y.{yen} sama dengan {int(hasil)} dollar")
elif tanya == 4:
    dollar = int(input("Masukkan nilai mata uang dollar:$. "))
    hasil = dollar * 133
    print(f"${dollar} sama dengan {int(hasil)} yen")
elif tanya == 5:
    rupiah = int(input("Masukkan nilai mata uang rupiah:Rp. "))
    hasil = rupiah/15000
    print(f"Rp.{rupiah} sama dengan {int(hasil)} dollar")
elif tanya == 6:
    dollar = int(input("Masukkan nilai mata uang dollar:$. "))
    hasil = dollar * 15000
    print(f"$.{dollar} sama dengan {int(hasil)} rupiah")
else:
    print("Invalid Input")
