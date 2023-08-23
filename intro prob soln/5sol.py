num = int(input())
def factorial(n):
    arr = [n]
    while n != 1:
        n -= 1
        arr.append(n)
    return arr
    
array = factorial(num)
permutations = []

current = array[0]
i = 0
error = False

while num > 0:
    try:
        if abs(array[i] - current) == 1:
            i += 1
        else:
            if array[i] not in permutations:
                current = array[i]
                permutations.append(current)
                array.remove(current)
                num -= 1
                i = 0
            else:
                i += 1
    except IndexError:
        error = True
        break

if error:
    print("NO SOLUTION") 
else:
    permutations = map(str, permutations)
    print(" ".join(permutations))
