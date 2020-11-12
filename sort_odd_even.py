def sort_odd_even(x):
    list2 = [] # membuat list kosong untuk angka genap
    list3 = [] # membuat list kosong untuk angka ganjil
    for i in range(len(x)): # memanggil seluruh isi list x
        if x[i] % 2 == 0: # jika angka di dalam x adalah genap, maka line selanjutnya akan dieksekusi
            list2.append(x[i]) # memasukan angka genap ke dalam list kosong/baru
            list2.sort(reverse=True) # untuk sorting reverse angka genap
        else: # jika angka di dalam x bukan angka genap, maka line selanjutnya akan dieksekusi
            list3.append(x[i]) # memasukan angka ganjil ke dalam list baru/kosong
            list3.sort() # untuk sorting angka ganjil
    joinedlist = list2 + list3 # menggabungkan list angka genap dan ganjil
    return f'[{joinedlist[3]},{joinedlist[4]},{joinedlist[0]},{joinedlist[1]},{joinedlist[5]},{joinedlist[2]}]'
    # return untuk mengatur posisi angka ganjil dan genap
print(sort_odd_even([5, 3, 2, 8, 1, 4]))

