entrada = ""

while entrada != "entrar" and entrada != "sair":
    entrada = input('Você quer "entrar" ou "sair"? ')
    if entrada == "entrar":
        print("Você digitou entrar!")
    elif entrada == "sair":
        print("Você digitou sair!")
    else:
        print("Você não digitou nem entrar nem sair!")
