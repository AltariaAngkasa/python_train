print("KONVERSI SUHU")
print("================================")
print("1. Celcius")
print("2. Reamur")
print("3. Fahrenheit")
print("4. Kelvin")
pilih = int(input("Pilih suhu: "))

if(pilih == 1):
    celc = int(input("Masukkan Suhu: "))
    ream = celc * (4/5)
    kelv = celc + 273
    fahr = (9/5) * celc + 32
    print(f"{celc} Celcius sama dengan {ream} Reamur")
    print(f"{celc} Celcius sama dengan {kelv} Kelvin")
    print(f"{celc} Celcius sama dengan {fahr} Fahrenheit")
elif(pilih == 2):
    ream = int(input("Masukkan Suhu: "))
    celc = (5/4) * ream
    kelv = (5/4) * ream + 273
    fahr = (9/4) * ream + 32
    print(f"{ream} Reamur sama dengan {celc} Celcius")
    print(f"{ream} Reamur sama dengan {kelv} Kelvin")
    print(f"{ream} Reamur sama dengan {fahr} Fahrenheit")
elif(pilih == 3):
    kelv = int(input("Masukkan suhu: "))
    celc = kelv - 273
    ream = 4/5 * (kelv - 273)
    fahr = 9/5 * (kelv - 273) + 32
    print(f"{kelv} Kelvin sama dengan {celc} Celcius")
    print(f"{kelv} Kelvin sama dengan {ream} Reamur")
    print(f"{kelv} Kelvin sama dengan {fahr} Fahrenheit")
elif(pilih == 4):
    fahr = int(input("Masukkan suhu: "))
    celc = 5/9 * (fahr - 32)
    ream = 4/9 * (fahr - 32)
    kelv = 5/9 * (fahr - 32) + 273
    print(f"{fahr} Fahrenheit sama dengan {celc} Celcius")
    print(f"{fahr} Fahrenheit sama dengan {ream} Reamur")
    print(f"{fahr} Fahrenheit sama dengan {kelv} Kelvin")
else:
    print("INVALID INPUT")
