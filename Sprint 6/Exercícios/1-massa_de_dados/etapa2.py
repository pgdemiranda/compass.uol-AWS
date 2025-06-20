lista_animais = [
    "Marreco",
    "Formiga",
    "Rato",
    "Javali",
    "Girafa",
    "Arara",
    "Pato",
    "Elefante",
    "Sapo",
    "Hipopótamo",
    "Quati",
    "Dromedário",
    "Leão",
    "Narval",
    "Baleia",
    "Tamanduá",
    "Iguana",
    "Ovelha",
    "Cachorro",
    "Zebra",
]

lista_animais = sorted(lista_animais)

[print(animal) for animal in lista_animais]

with open("lista_animais.txt", "w") as file:
    for animal in lista_animais:
        file.write(f"{animal}\n")
    
    print(f"lista organizada e arquivo 'lista_animais.txt' salvo com sucesso")
