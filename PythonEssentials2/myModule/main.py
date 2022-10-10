import module 
from module import suml, prodl

print('variable importada',module.var)

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))