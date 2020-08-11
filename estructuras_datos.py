#Listas
secuencia = [1,2,3,4,5,6]
print(secuencia)
print(secuencia[0])
secuencia[0] = 0
secuencia.append(7) #agrega
secuencia.pop(0) #elimina
print(secuencia)
paises = [
     "España",
     "Ecuador",
     "Uruguay",
     "Estados Unidos",
     "Argentina",
     "Perú"
 ]
print(paises)
print(type(paises))

for pais in paises:
    print(pais)

#Diccionarios

dict_country = {
     "es": "España",
     "ec": "Ecuador",
     "ur": "Uruguay",
     "us": "Estados Unidos",
     "ar": "Argentina",
     "pe": "Perú"
}
for key,value in dict_country.items():
    print(key, ": ", value)

print(dict_country.keys())
print(dict_country.values())

for key,value in dict_country.items():
    print(key, ": ", value)

print("values: ", sorted(dict_country.values()))
print("keys: ", sorted(dict_country.keys()))
print("dictionary: ", sorted(dict_country))
print("items: ", sorted(dict_country.items()))

#Sets
paises_set = ({
    "España",
    "Ecuador",
    "Uruguay",
    "Estados Unidos",
    "Argentina",
    "Perú",
    "Perú"
})
print(paises_set)
print(type(paises_set))