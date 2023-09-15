# Singleton - significa que sópode existir uma instancia daquele objeto

# Importlib server para recarregar o modulo
import importlib

import aula156_m
# recarregar o modulo
print(aula156_m.varialvel)

for i in range(10):
    importlib.reload(aula156_m)
    print(i)

print('fim')
