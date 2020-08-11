dict_country = {
     "es": "España",
     "ec": "Ecuador",
     "ur": "Uruguay",
     "us": "Estados Unidos",
     "ar": "Argentina",
     "pe": "Perú"
}
valid_code = ['ec','ar']
paises = [val for key, val in dict_country.items() if key in valid_code]
print(paises)