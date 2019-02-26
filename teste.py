string = 'AABACAADA'

k = 3

for i in range(0,len(string), int((len(string)/k))):
    a = string[i:i+k]
    fim = a[1:]
    print(fim)
