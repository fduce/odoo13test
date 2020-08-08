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
    print("key {} - value {}",format(key.get("es"),value.get())
