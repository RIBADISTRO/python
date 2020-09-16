'''
RECARGA DE MODULOS

Un  modulos puede ser  recargado. Sin embargo
todos los  valores definidos  en sus miembros
seran  perdidos

'''

import  importlib

import  modulo

del(modulo.b)
modulo.a = 0


importlib.reload(modulo)
from pprint import pprint

pprint(modulo.__dict__)

