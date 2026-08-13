'''Re-aprendendo Arrays
import numpy as np

minha_lista = np.array([0,1,2,3,4,5])
print(minha_lista * 2)
'''

'''Lista

minha_lista = []
carro = ["celta", "palio", "corsa", "prisma"]
#carro.append("uno")#
#carro.insert(1,"mobi")#
#carro.pop(0)#
print (carro)
'''

'''Funções

def saudar():
    print("Olá! Seja Bem vindo"
saudar()

def testar():
    print("faça teste em tal maquina!")
testar()


def somar(a,b):
    return a + b
resultado= somar(250,250)
print(resultado)
'''

#EXEMPLO PRATICO#

'''
minhaLista = []

def adicionarItem(nomeItem):
    minhaLista.append(nomeItem)
    print(f"✅ '{nomeItem}' foi adicionado com sucesso!")

def exibirLista():
    print("\n -- SUA LISTA DE COMPRA --")
    if len(minhaLista) == 0:
        print("A lista está vazia.")
    else: 
        for item in minhaLista:
            print(f"{item}")

adicionarItem("Arroz")
adicionarItem("Café")
adicionarItem("Feijão")

exibirLista()
'''

# Criamos a lista para guardar as notas
notas_aluno = []

# 1. Adiciona a nota na lista
def adicionar_nota(nota):
    notas_aluno.append(nota)
    print(f"Nota {nota} adicionada!")

# 2. Calcula e retorna a média
def calcular_media():
    total_notas = sum(notas_aluno)
    quantidade = len(notas_aluno)
    return total_notas / quantidade

# 3. Analisa a média e exibe o resultado final
def verificar_situacao(media):
    if media >= 7.0:
        print("Situação: Aprovado! 🎉")
    else:
        print("Situação: Reprovado. 😢")

# --- EXECUTANDO O TESTE ---

# Adicionando 3 notas
adicionar_nota(8.5)
adicionar_nota(7.0)
adicionar_nota(9.0)

print("-" * 30)

# Calcula a média e guarda o valor retornado na variável 'media_final'
media_final = calcular_media()
print(f"Média do aluno: {media_final:.2f}") # o :.2f serve para mostrar só 2 casas decimais

# Passa a média calculada para a função decidir se aprovou ou reprovou
verificar_situacao(media_final)
