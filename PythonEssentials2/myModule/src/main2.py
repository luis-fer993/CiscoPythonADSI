from sys import path
path.append('C:\\Users\\Aprendiz\\Documents\\CiscoPythonADSI\\PythonEssentials2\\myModule\\packages')
path.append('C:\\Users\\Aprendiz\\Documents\\CiscoPythonADSI\\PythonEssentials2\\myModule\\packages\\extraZIP.zip')
#agregamos modulo en zip

import extra.iota #todo el modulo
from extra.iota import FunI #funcion en especifico

import extra.good.best.sigma as sig #alias
from extra.good.best.tau import FunT

from extraZIP.iota import FunI as FunIZip  #modulos desde archivos zip


if __name__ == '__main__':
    print(extra.iota.FunI())
    print(FunI())
    
    print(sig.FunS())
    print(FunT())
    
    print(FunIZip()) #llamada funcion del modulo en archivo zip
