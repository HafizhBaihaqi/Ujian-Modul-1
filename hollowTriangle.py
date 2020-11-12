def hollowTriangle(t):
    for i in range(t):
        if i < 1: # baris pertama
            print(('__' * (t-1))+'#', end='_') # print untuk output ____#_
            print('_____') # print _ untuk menambah underscore dibagian akhir baris pertama
        elif i < (t-1): # baris diantara pertama dan terakhir
            for j in range(t-(i+1)):
                print('_', end='_') # print _ untuk menambah underscore di bagian awal baris tengah (baris antara baris pertama dan terakhir)
            print('#', end='_')
            for j in range((i*2)-1):
                print('_', end='_')
            print('#__', end='_') # tambahan _ untuk mengadjust underscore di bagian akhir baris
            print('_') # print _ untuk menambah underscore di bagian akhir baris tengah (baris antara baris pertama dan terakhir)
        else: # baris terakhir
            print('# ' * ((t*2)-1)) # ditambahkan spasi agar baris akhir seimbang/setara dengan baris atasnya
hollowTriangle(1)
hollowTriangle(2)
hollowTriangle(3)
hollowTriangle(4)
hollowTriangle(5)
hollowTriangle(6)
