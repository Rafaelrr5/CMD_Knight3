import time
import random
import datetime
import pygame
import pyautogui
import keyboard
import os
import User, Classes, Armas, Menus

def tempo():
    time.sleep(0.2)
    
def opcoesmenu(escolha, opcao):
    a = keyboard.read_key()
    if a == 'down':
        opcao+=1
        time.sleep(0.1)
        
    elif a == 'up':
        opcao-=1
        time.sleep(0.1)    
        
    elif a == "enter":
        escolha = opcao
        
    return opcao, escolha
    
# pygame.mixer.music.stop pygame.mixer.music.pause pygame.mixer.music.unpause

pygame.init()
pygame.mixer.music.load('musica.wav')
pygame.event.wait()
volume = 0.8
pygame.mixer.music.set_volume(volume)
escolha = 0
opcao = 1
menuInicial = Menus.MenusIni

loadbarwidth =  23#23

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
    time.sleep(1)
    print("")
    tempo()
    print("     ___         ___                     ___   ___         ___         ___  ")
    tempo()
    print("    |     |\ /|   | |       |  /  |\  |   |   |     |   |   |             | ")
    tempo()
    print("    |     | + |   + |       |-+   | + |   +   | +-  |-+-|   +          -+-  ")
    tempo()
    print("    |     |   |   | |       |  \  |  \|   |   |   | |   |   |             | ")
    tempo()
    print("     ---         ---                     ---   ---                     ---  ")
    tempo()
    print("             ")
    tempo()
    print("                     _    .  ,   .           .")
    tempo()
    print("        *  / \_ *  / \_      _  *        *   /\\'__        *")
    tempo()
    print("          /    \  /    \,   ((        .    _/  /  \  *'.")
    tempo()
    print("     .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.")
    tempo()
    print("        /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *")
    tempo()
    print("      /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \\")
    tempo()
    print("     /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-")
    tempo()
    print("    /        `.  / /       `.~-^=-=~=^=.-'      '-._ `._""")
    tempo()
    

while(escolha != 1) or (escolha != 4):
    if inicio != 0:
        print("""
         ___         ___                     ___   ___         ___         ___  
        |     |\ /|   | |       |  /  |\  |   |   |     |   |   |             | 
        |     | + |   + |       |-+   | + |   +   | +-  |-+-|   +          -+-  
        |     |   |   | |       |  \  |  \|   |   |   | |   |   |             | 
         ---         ---                     ---   ---                     ---  
                 
                         _    .  ,   .           .
            *  / \_ *  / \_      _  *        *   /\\'__        *
              /    \  /    \,   ((        .    _/  /  \  *'.
         .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
            /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
          /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \\
         /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
        /        `.  / /       `.~-^=-=~=^=.-'      '-._ `._""")
    
    if opcao == 1:
        menuInicial.menu1()
    elif opcao == 2:
        menuInicial.menu2()
    elif opcao == 3:
        menuInicial.menu3()
    elif opcao == 4:
        menuInicial.menu4()
    
    if opcao == 0:
        opcao = 1
        menuInicial.menu1()
        
    if opcao == 5:
        opcao = 4
        menuInicial.menu4()

    opcao, escolha = opcoesmenu(escolha, opcao)
    
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
    
os.system("cls")

print("A história começa...")
print("""                           (   ))
                          (    ))
                           (    ))
                          (    ))
                            )  )
                           (  (                  /\\
                            (_)                 /  \  /\\
                    ________[_]________      /\/    \/  \\
           /\      /\        ______    \    /   /\/\  /\/\\
          /  \    //_\       \    /\    \  /\/\/    \/    \\
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \\
 /\/\/\/       //_______\       \|__|      \\
/      \      /XXXXXXXXXX\    Taverna dos   \\
        \    /_I_II  I__I_\_______C̲r̲i̲a̲_______\\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~""")
time.sleep(1)

#https://pt.piliapp.com/cool-text/small-caps/
print("Clóvis: ᴍᴇᴜ ᴅᴇᴜs ᴄʀɪᴀ ᴇᴜ ʙᴇʙɪ ᴛᴀɴᴛᴏ ǫᴜᴇ ᴇᴜ ɴᴇᴍ ʟᴇᴍʙʀᴏ ᴏ sᴇᴜ ɴᴏᴍᴇ, ᴀᴊᴜᴅᴀ ᴀɪ́...")
User.nome = input("Digite seu nome: ") 
User.nome = input()
while((escolha != 1) or (escolha!=2)):
    
    print(f"Clóvis: Isso aí memo, {User.nome} ᴇ ᴠᴏᴄᴇ̂ ᴇ́...?")
    if opcao == 1:
        menuInicial.menuclas1()
        
    elif opcao == 2:
        menuInicial.menuclas2()
    
    if opcao < 1:
        opcao = 1
        menuInicial.menuclas1()
        
    if opcao > 2:
        opcao = 2
        menuInicial.menuclas2()
    
    opcao, escolha = opcoesmenu(escolha, opcao)
    
    os.system("cls")

print("ᴘᴏᴅᴇ ᴄʀᴇʀ, ᴛᴏ ᴍᴇ ʟᴇᴍʙʀᴀɴᴅᴏ... ᴠᴀᴍᴏ ɴᴇssᴀ, ᴊᴀ́ ᴛᴏ ʀᴜɪᴍ ᴊᴀ́")