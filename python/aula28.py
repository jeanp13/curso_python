nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    contemEspacos = " não"
    if " " in nome:
        contemEspacos = ""
    print(f"Seu nome{contemEspacos} contem espaços")
    print(f"Seu nome contem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0:1]}")
    print(f"A última letra do seu nome é {nome[-1:]}")
else:
    print("Desculpe, você deixou campos vazios.")
