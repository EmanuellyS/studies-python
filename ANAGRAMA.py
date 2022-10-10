# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 08:12:22 2022

@author: DISRCT
"""

import random

dic = {}

facil = []
medio = []
dificil = []

pont = 100


def org_palavras():
    arquivo = open('wordlist.txt', 'r', encoding='utf-8')
    for line in arquivo:
        line = list(line.strip())
        original = (''.join(line).lower())
        random.shuffle(line)
        result = ''.join(line).lower()
        dic[original]=result
        if len(result) <= 4:
            facil.append(result)
        elif len(result) > 4 and len(result) <= 7:
            medio.append(result)
        else: 
            dificil.append(result)
 

print("""
          --------------------BEM VINDO AO ANAGRAMA GAME----------------
          
          Instruções: 
              1 - Você ira escolher o nível que deseja jogar.
              2 - Você irá receber uma palavra embaralhada e deverá adivinha-la.
              3 - O jogo inicia com 100 pts. A cada tentativa errada você perderá 20 pts.
              4 - Ao zerar os pontos você perderá a partida.""")
org_palavras()
while True:
    try:
        nivel = int(input("""
                          Nível 1 - Nível 2 - Nível 3
                          Digite o nível que deseja jogar: """))               
        if nivel == 1:
            palavra = random.choice(facil)
            print(palavra)
            
        elif nivel == 2:
            palavra = random.choice(medio)
            print(palavra)
        
        elif nivel == 3:        
            palavra = random.choice(dificil)
            print(palavra)
            
        else: 
            print('Tente novamente.')
    except:
        print("""Opção inválida.""")
        continue
    while True:
        tentativa = input('Digite sua tentativa: ')
        if tentativa.lower() in dic.keys():
            print(f"""
                  PALAVRA: {tentativa} """)
            print(f"""
                  PARAÉNSSSS!!!!!!!
                  
                  SUA PONTUAÇÃO FINAL: {pont}""")
            break
        else:
          print('Não foi dessa vez, tente novamente!!')
          pont -= 20
          continue
          if pont == 0:
              print("""VOCÊ PERDEU!!!! MAIS SORTE NA PROXIMA!!!!""")
              break
