def print_formatted(number):
    # your code goes here
    a = []
    for i in range(number):
        b = []
        b.append('{}{}'.format(' '*((len(str(bin(number)))-2)-len(str(i+1))),i+1))
        b.append('{}{}'.format(' '*((len(str(bin(number)))-2)- len(oct(i+1)[2:])), oct(i+1)[2:]))
        b.append('{}{}'.format(' '*((len(str(bin(number)))-2) - len(hex(i+1)[2:])), hex(i+1)[2:]).upper())
        b.append('{}{}'.format(' '*((len(str(bin(number)))-2)-len(bin(i+1)[2:])), bin(i+1)[2:]))
        a.append(b)
    for c in range(len(a)):
        for d in range(len(a[c])):
            print(a[c][d],end = ' ')
        print('')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
