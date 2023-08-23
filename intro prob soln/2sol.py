inp1 = int(input())
inp2 = str(input())

def sum_ap(n):
    sum = (n/2)*(1 + n)
    return sum

def sum_str(inp):
    temp = inp.split(' ')
    finSum = sum(list(map(int, temp)))
    return finSum

missing_number = sum_ap(inp1) - sum_str(inp2)

print(int(missing_number))
