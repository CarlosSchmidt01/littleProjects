s = 'abaabaabaabaae'

import re

l = [a for a in re.findall('[aAeEiIoOuU]+', s)]

print(l)
