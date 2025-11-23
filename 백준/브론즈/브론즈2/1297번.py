import sys
import math
d, h, w = map(int, sys.stdin.readline().split())
x = math.sqrt((d*d) / (h*h + w*w))
print(math.floor(h*x), math.floor(w*x))
'''
h2x2 + w2x2 = d2
(h2 + w2)x2 = d2
x2 = d2 / (h2 + w2)

'''