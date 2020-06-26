'''
Programa pergunta a idade, o peso e a altura e
decide se ela está apta a ser do exercito.
Para entrar no exercito é preciso ter mais de 18
anos, passar de 60kg e medir mais de 1.70 metros.
'''

nome = input('Qual o seu nome?:')
idade = int(input('Qual sua idade?:'))
peso = float(input('Qual o seu peso?:'))
altura = float(input('Qual sua altura?:'))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print(nome,'Está apto ao Exercito')
else:
    print(nome,'Não está apto ao Exercito')