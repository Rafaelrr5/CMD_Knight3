import time
import random
import datetime
import pygame
import pyautogui
import keyboard
import menus
import os

# pygame.mixer.music.stop pygame.mixer.music.pause pygame.mixer.music.unpause

pygame.init()
pygame.mixer.music.load('musica.wav')
pygame.event.wait()
volume = 0.8
pygame.mixer.music.set_volume(volume)
escolha = 0
opcao = 1
menuInicial = menus.MenusIni

loadbarwidth =  10#23

for i in range(1, loadbarwidth + 1):
    time.sleep(0.1) 

    strbarwidth = '[{}{}] - {}\r'.format(
        (i * '#'),
        ((loadbarwidth - i) * '-'),
        (('{:0.2f}'.format(((i) * (100/loadbarwidth))) + '%'))
    )

    print(strbarwidth ,end = '')
pygame.mixer.music.play()

print()
inicio = 0
if inicio == 0:
    print("Bem vindo, jovem cavaleiro, ao...")
    print(""" 
     ___         ___                     ___   ___         ___         ___  
    |     |\ /|   | |       |  /  |\  |   |   |     |   |   |             | 
    |     | + |   + |       |-+   | + |   +   | +-  |-+-|   +          -+-  
    |     |   |   | |       |  \  |  \|   |   |   | |   |   |             | 
     ---         ---                     ---   ---                     ---  """)
    

while(escolha != 1) or (escolha != 4):
    if inicio != 0:
        print("""
         ___         ___                     ___   ___         ___         ___  
        |     |\ /|   | |       |  /  |\  |   |   |     |   |   |             | 
        |     | + |   + |       |-+   | + |   +   | +-  |-+-|   +          -+-  
        |     |   |   | |       |  \  |  \|   |   |   | |   |   |             | 
         ---         ---                     ---   ---                     ---  """)
    
    if opcao == 1:
        menuInicial.menu1()
    elif opcao == 2:
        menuInicial.menu2()
    elif opcao == 3:
        menuInicial.menu3()
    elif opcao == 4:
        menuInicial.menu4()

    a = keyboard.read_key()
    if a == 'down':
        opcao+=1
        time.sleep(0.1)
        
    elif a == 'up':
        opcao-=1
        time.sleep(0.1)    
        
    elif a == "enter":
        escolha = opcao
        
        if escolha == 1:
            break
        
        elif escolha == 2:
            pygame.mixer.music.set_volume(int(input(f"Digite o valor do volume que você deseja || Atual: {volume}")))
            escolha = 0
        
        elif escolha == 3:
            print("""_________         _________ 
                  /         \\       /         \\                       ___                                             ___   ___   ___                         
                 /  /~~~~~\\  \\     /  /~~~~~\\  \\                     |   |              |  /        |                 | |   | |   | |                         
                 |  |     |  |     |  |     |  |                     |   |    --        |-+    -    |-    |-     -     -+-   -+-   -+-                        
                 |  |     |  |     |  |     |  |                     |   |     \\        |  \\  | |   | |   |     | |     | |   | |   | |                       
                 |  |     |  |     |  |     |  |         /            ---     --               -     -           --    ---   ---   ---                        
                 |  |     |  |     |  |     |  |       //                                 
                (o  o)    \\  \\_____/  /     \\  \\_____/ /                              
                 \\__/      \\         /       \\        /                                 
                  |         ~~~~~~~~~         ~~~~~~~~                                     
                  ^""")
            input("Pressione enter para volar ao menu")
            escolha = 0
        
        if escolha == 4:
            exit()
    
    inicio=1
    os.system("cls")
    
