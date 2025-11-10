meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "Abreviação de verdade",
            "TLGD": "Abreviação para To ligado",
            "PAIA": "Algo sem graça, ruim ou chato"
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Ainda não temos essa palavra... Mas estamos trabalhando nela!")