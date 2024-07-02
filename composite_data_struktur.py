# Python List

karyawan = ['Joko', 'Alex', 'Chandra', 'Hartono', 'Samsul']
print(karyawan)
# Alex and Joko Resign
karyawan.remove('Alex')
karyawan.remove('Joko')
print(karyawan)
# Agus and Toni join the company A
karyawan.append('Agus')
karyawan.append('Toni')
print(karyawan)

# Python Dictionary
model = { 
    "LinearRegression" : 85,
    "SVM" : 88,
    "DecisionTree" : 90,
    "RandomForest" : 95    
}

print(model.values())

print(f'Nilai model ML metode Linear Regression {model.get("LinearRegression")}')
print(f'Nilai model ML metode SVM {model.get("SVM")}')
print(f'Nilai model ML metode Decision Tree {model.get("DecisionTree")}')
print(f'Nilai model ML metode Random Forest {model.get("RandomForest")}')


# buatlah sebuah empty list untuk menyimpan seluruh penonton yang terpilih
selected_viewers = []

# buatlah variabel konstant untuk menyimpan jumlah penonton
N_VIEWERS = 200

# buatlah variabel yang digunakan untuk menghentikan kondisi while
counter = 1

# buatlah empty list untuk menyimpan penonton terpilih pada persyaratan pertama
selected_viewers_first = []

# cari penonton dengan perulangan while sesuai kondisi
while counter <= N_VIEWERS:
    
    if (counter < 50) and (counter % 11 == 0):
        selected_viewers_first.append(counter)
        
    counter += 1

# print penonton yang memenuhi persyaratan
print(selected_viewers_first)

# karena ada lebih dari satu angka maka ambil sesuai kondisi
# masukkan penonton terpilih ke variabel untuk menyimpan penonton yang terpilih
# hint (gunakan method append)
get_first_viewers = selected_viewers_first[-2]

# print penonton terpilih
selected_viewers.append(get_first_viewers)

print(selected_viewers)
