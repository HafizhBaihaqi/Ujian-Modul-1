def multiplication_table(row,column):
    number = 0 # membuat nomor kosong untuk ditambahkan pada looping kolom
    for i in range(row): # looping untuk baris
        for j in range(column): # looping untuk kolom
            number = number + 1 # variable number pada setiap looping ditambahkan 1
            print(number, end=' ') # print looping number pada setiap kolom, diakhiri
        print() # untuk ganti baris setelah selesai looping kolom
    return
multiplication_table(3,3)
multiplication_table(5,3)
multiplication_table(3,5)