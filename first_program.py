def is_even(x):
     return x % 2 == 0
number = [1, 2, 3, 4, 5, 6 , 7, 8, 9 , 10,12]
res = list(filter(is_even,number))
print(res)
