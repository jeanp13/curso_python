import datetime


nome = "John"
sobrenome = "Doe"
ano_nascimento = 1990
idade = datetime.date.today().year - 1990
maior_de_idade = idade >= 18
altura_metros = 1.78

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de Nascimento:", ano_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura em metros:", altura_metros)
