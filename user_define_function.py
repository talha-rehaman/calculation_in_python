# def analyze_list(number):
#     return{
#         "length" : len(number),
#         "max":max(number),
#         "min": min(number),
#         "sum":sum(number)
#     }

# res = analyze_list([10,20,30,40])
# print(res)

# def count_even_odd(numbers):
#     even = 0
#     odd = 0

#     for num in numbers:
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     return even, odd

# print(count_even_odd([1, 2, 3, 4, 5, 6]))
# def separate_numbers(numbers):
#     even_list = []
#     odd_list = []

#     for num in numbers:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:
#             odd_list.append(num)

#     return even_list, odd_list

# print(separate_numbers([1, 2, 3, 4, 5]))
def check_numbers(numbers):
    result = []

    for num in numbers:
        if num > 50:
            result.append(f"{num} is large")
        elif num > 20:
            result.append(f"{num} is medium")
        else:
            result.append(f"{num} is small") 

    return result

print(check_numbers([10, 25, 60]))
