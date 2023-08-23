num = int(input())
def factorial(n):
    arr = [n]
    while n != 1:
        n -= 1
        arr.append(n)
    return arr
    
arr_real = factorial(num)
current_num_real = arr_real[0]
permutation_real  = []

# while len(permutation) < num:
def match_founder(current_num, arr, permutation):
    for i in range(len(arr) - 1):
        if (current_num - arr[i]) == 1:
            pass
        elif  current_num != arr[i]:
            current_num = arr[i]
            i = 0
            permutation.append(current_num)
            arr.remove(current_num)
        # print(arr, permutation, current_num)
        return current_num, permutation, arr
        
print(match_founder(current_num_real, arr_real, permutation_real))


# while not len(arr) == 0:
#     for i in range(num):
#         try:
#             arr.remove(current_num)
#         except ValueError:
#             pass  
#         if arr[i] - current_num == 1:
#             permutation.append(arr[i])
#         else:
#             pass
        
    
# print(permutation)