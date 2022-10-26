import random

import numpy as np
rng = np.random.RandomState(1)
a = rng.randint(1,100,10)
b = rng.randint(1,100,10)
c = a + b  #矩陣內的"數值"相加
print(a);print(b);print(c)
###############################
random.seed(1)
d = [random.randint(1,100) for i in range(10)]
e = [random.randint(1,100) for i in range(10)]
f = d + e #矩陣內的"個數"相加 : 10個+10個 =20個
print(d);print(e);print(f)