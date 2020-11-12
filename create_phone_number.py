def create_phone_numbers(number):
    return f'({number[0]}{number[1]}{number[2]}) {number[3]}{number[4]}{number[5]}-{number[6]}{number[7]}{number[8]}{number[9]}'
# menggunakan indexing satu persatu, dan ditambahkan '()' kurung di antara index 0 sampai 2, spasi sebelum index 3, dan '-' strip setelah index 5 
print(create_phone_numbers([1,2,3,4,5,6,7,8,9,0]))