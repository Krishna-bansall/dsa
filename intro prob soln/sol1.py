# weird algorithm
n = int(input())
stri = '' + str(n)

while (n != 1):
    if n%2==0:
        n /= 2
    else:
        n = (n*3) + 1
        
    stri = stri + " " + str(int(n))
    
print(stri)