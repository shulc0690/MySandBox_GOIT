from decimal import Decimal as d, getcontext

getcontext().prec = 4

f = 0.2 + 0.1 + 0.3 - 0.5
print(f)

f2 = d("0.2") + d("0.1") + d("0.3") - d("0.5112")

print(f2)