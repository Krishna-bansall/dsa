size = input()
input_arr = list(str(input()).split(" "))
int_arr = list(map(int, input_arr))
step = 0

for i in range(int(size) - 1):
    if int_arr[i+1] < int_arr[i]:
        step += int_arr[i] - int_arr[i + 1] 
        int_arr[i + 1] = int_arr[i]
    
print(step)
        