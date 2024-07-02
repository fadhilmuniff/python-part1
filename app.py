# printing and variabel
print("hello world")
myName = "Fadhil"
# print(myName)

# # more printing
umur = 12
# Versi lama
print("Halo, saya %s. Saya berumur %s tahun." % (myName, umur))
# Versi baru
print(f"Halo, saya {myName}. Saya berumur {umur} tahun.")

# data struktur
num_1 = 1
num_2 = 1.3
print(type(num_1))
print(type(num_2))

angka_1 = 20
angka_2 = 30
total_angka = angka_1+angka_2
print(f"total penjumlahan {angka_1} + {angka_2} adalah {total_angka}")


#string
# concenate
nama_depan = "fadhil"
nama_belakang = "munif"
print(f"nama lengkap saya adalah {nama_depan+nama_belakang}")

# repetition 
print(nama_belakang*3)

# slicing
print(nama_belakang[0:4]) # output : muni

# branching
lembab = 1
if lembab < 3 :
    print("perlu disiram")
else:
    pass

# Buatlah nested branch kondisi untuk Normal - Dry dan Normal - Moist dengan aturan penyiraman yg telah ditentukan dengan input Normal dan Moist
temp = "Normal"
moist = "Moist"
if temp == "Normal" :
    if moist == "Dry" :
        print("Penyiraman 15 menit")
    else :
        print ("Penyiraman 10 menit")



 


