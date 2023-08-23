input_dna = list(str(input()))
dna_set = ['A', 'C', 'G', 'T']
maxi = []

for char in dna_set:
    meter = 0
    for i in input_dna:
        if i==char:
            meter += 1
        else:
            meter = 0
        maxi.append(meter)
    

print(int(max(maxi)))
    
