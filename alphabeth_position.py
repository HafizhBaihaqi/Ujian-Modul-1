def alphabet_position(text):
    dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    # membuat dictionary untuk setiap alphabet dan posisinya (key = alphabet, value = posisinya)
    new_text = text.lower() # mengubah parameter menjadi lowercase dan menyimpan di variabel baru bernama new_text
    for i in new_text: # looping untuk new_text
        if i in dict: # jika i ada di dalam dictionary, maka perintah selanjutnya dieksekusi
            new_text = new_text.replace(i, dict[i]) # jika condition terpenuhi, maka alphabet di dalam new_text akan diganti dengan posisi(valuenya)
    print(new_text) # untuk print new_text yang sudah terlooping dengan conditional
alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position("it’s never too late to try")
alphabet_position("Have you done your homework?")