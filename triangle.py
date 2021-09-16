from array import array
import random
import math

max = 0
q = random.sample(range(100), 10)
print(q)
for i in range(len(q)):
    for j in range(i+1, len(q)):
        for k in range (j+1, len(q)):
            a = q[i]
            b = q[j]
            c = q[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = math.sqrt(p*(p - a)*(p - b)*(p - c))
                if s > max:
                    max = s
print(max)

