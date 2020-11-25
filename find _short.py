def find_short(string):
    x = string.split() # memisahkan string menjadi beberapa index ke dalam list dan menamakannya dengan variabel x
    y = min(len(word) for word in x) # mencari string yang mempunyai panjang menggunakan 'len', yang paling kecil menggunakan 'min' dengan melooping setiap word di variabel x
    print(y) # print hasil looping
    return
find_short('Many people get up early in the morning')
find_short('Every office would getting newest monitor')
find_short('Create new file after this morning')