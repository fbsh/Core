import math
import cmath

def fft(p):
    n = len(p)
    if n == 1:
        return p
    w = cmath.exp(2 * math.pi*1j / n)
    y_e = fft(p[0::2])
    y_o = fft(p[1::2])
    y = [None] * n
    for i in range(n//2):
        y[i] = y_e[i] + y_o[i] * w**i
        y[i+n//2] = y_e[i] - y_o[i] * w**i
    return y

def p(x):
    return 1 + 2*x + 3*x**2 + 4*x**3

print(fft([1, 2, 3, 4]))
print([p(1), p(1j), p(-1), p(-1j)])
