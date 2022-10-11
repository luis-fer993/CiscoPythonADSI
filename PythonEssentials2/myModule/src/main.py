from sys import path

#path.append('..\\modules')
path.append('C:\\Users\\Aprendiz\\Documents\\CiscoPythonADSI\\PythonEssentials2\\myModule\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

print('variable importada',module.var)

