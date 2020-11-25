def persistance(number):
    x = list(str(number))
    y = list(map(int, x))
    hasil = 1
    list1 = []
    # list2 = []
    if len(y) > 1:
        for i in y:
           hasil = hasil * i
        print(hasil)
    else:
        print(0)
persistance(0)
persistance(39)
persistance(999)