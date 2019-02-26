import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A', 'b', 'c', 'd', 'e'], ['w', 'x', 'y', 'z'])
print(df['w'])
#df['W']
