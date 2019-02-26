#s = ['code', 'doce', 'frame', 'framer', 'odec']
#s = []
#s = ['aaaa','aaaa','cccc','dddd','eeee','bbbb']
#s = ['a', 'b', 'ca', 'ac', 'teste', 'stete', 'aaaa']
#s = ['poke', 'pkoe','okpe','ekop']
s = ['code', 'aaagmnrs', 'anagrams', 'doce']

def anagrams(s):
    a = []


    s.sort(key = lambda x: len(x))


    if len(s) > 1:
        for j in range(len(s)):
            if s[j] != '':
                for i in range(j + 1, len(s)):
                    if len(s[j]) == len(s[i]):
                        if s[j] not in a:
                            a.append(s[j])
                        if sorted(s[j]) == sorted(s[i]):
                            s[i] = ''
                    else:
                        if s[j] not in a:
                            a.append(s[j])
                if j == len(s) - 1:
                    if s[j] not in a:
                        a.append(s[j])

    return sorted(a)


print(anagrams(s))
