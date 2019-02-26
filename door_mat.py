
n, m = [int(i) for i in input().split()]
'''
for a in range(n):
    for b in range(m):
        if b == ((m//2)-(a*3)):
            print('.|.'* (a+1), end = '')
        else:
            print('-', end = '')
    print('')
'''
p = [('.|.' * (2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(p + ['WELCOME'.center(m, '-')]+p[::-1]))
