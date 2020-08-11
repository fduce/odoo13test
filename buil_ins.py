#Sort
paises = [
     "España",
     "Ecuador",
     "Uruguay",
     "Estados Unidos",
     "Argentina",
     "Perú"
 ]
ordenado = sorted(paises, reverse=True)
print(ordenado)

#Filter

def filtro(elemento):
    return elemento >= 10

numeros = [1, 10, 15, 25, 3]
print("filter")
for item in filter(filtro, numeros):
    print(item)

print("filter_2")
filtro_2 = lambda arg: arg>=10 #formato= lambda parametros: return
for item in filter(filtro_2, numeros):
    print(item)