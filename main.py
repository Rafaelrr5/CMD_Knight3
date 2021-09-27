import time
import random
import datetime
import pygame
import pyautogui
import keyboard
import os
import User, Armas, Menus
from Armas import Arco,Espada
from User import user

def musiquinha(musica):
    if musica:
        musica = False
        pygame.mixer.music.pause()
        return musica
    
    if not musica:
        musica = True
        pygame.mixer.music.unpause()
        return musica

def tempo():
    time.sleep(0) #0.2
    
def opcoesmenu(escolha, opcao):
    a = keyboard.read_key()
    if a == 'down':
        opcao+=1
        time.sleep(0.1)
        
    elif a == 'up':
        opcao-=1
        time.sleep(0.1)    
        
    elif a == "space":
        escolha = opcao
        time.sleep(0.1)
        
    os.system("cls")
    return opcao, escolha

def voltarmenu(escolha, opcao):
    opcao, escolha = opcoesmenu(escolha, opcao)
    return opcao, escolha

# pygame.mixer.music.stop pygame.mixer.music.pause pygame.mixer.music.unpause

pygame.init()
path = os.path.join(os.path.dirname(__file__), 'musica.wav')
pygame.mixer.music.load(path)
pygame.event.wait()
volume = 0.8
pygame.mixer.music.set_volume(volume)
escolha = 0
opcao = 1
menuInicial = Menus.MenusIni
musica = True

carregamento =  10 #23

for i in range(1, carregamento + 1):
    time.sleep(0.1) 

    strbarwidth = '[{}{}] - {}\r'.format(
        (i * '#'),
        ((carregamento - i) * '-'),
        (('{:0.2f}'.format(((i) * (100/carregamento))) + '%'))
    )

    print(strbarwidth ,end = '')
pygame.mixer.music.play()

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
    
    print("Para manipular o menu, utilize as setinhas e a tecla espaço do seu teclado")
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
        opcao = 4
        menuInicial.menu4()
        
    if opcao == 5:
        opcao = 1
        menuInicial.menu1()

    opcao, escolha = opcoesmenu(escolha, opcao)
    
    if escolha == 1:
        break
        
    elif escolha == 2:
        input("Aperte enter")
        musica = musiquinha(musica)
        opcao, escolha = voltarmenu(0,2)
        
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
        input("Pressione enter para voltar ao menu")
        opcao, escolha = voltarmenu(0,3)
        
    if escolha == 4:
        exit()
    
    inicio=1
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
user.nome = input("Digite seu nome: ") 
escolha = 0
while((escolha == 0)): 
    
    print(f"Clóvis: Isso aí memo, {user.nome}, ᴇ ᴠᴏᴄᴇ̂ ᴇ́...?")
    if opcao == 1:
        menuInicial.menuclas1()
        
    elif opcao == 2:
        menuInicial.menuclas2()
    
    if opcao < 1:
        opcao = 2
        menuInicial.menuclas1()
        
    if opcao > 2:
        opcao = 1
        menuInicial.menuclas2()
    
    opcao, escolha = opcoesmenu(escolha, opcao)

if escolha == 1:
    user = user(user.nome,1,100,25,25,80,Espada(2,1))
        
elif escolha == 2:
    user = user(user.nome,2,80,40,10,100,Arco(2,1))

escolha = 0
while(escolha==0): 

    if user.classe == 1:
        print(f"Clóvis: ᴘᴏᴅᴇ ᴄʀᴇʀ, ᴛᴏ ᴍᴇ ʟᴇᴍʙʀᴀɴᴅᴏ... sᴇ ᴇᴜ ɴᴀ̃ᴏ ᴍᴇ ᴇɴɢᴀɴᴏ sᴜᴀ ᴇsᴘᴀᴅᴀ ᴇʀᴀ ᴀ ᴄᴏᴍ {user.danoArma} ᴅᴇ ᴅᴀɴᴏ ᴇ {user.speedArma} ᴅᴇ ᴠᴇʟᴏᴄɪᴅᴀᴅᴇ ᴅᴇ ᴀᴛᴀǫᴜᴇ ɴᴇ́?")
        
        if opcao == 1:
            menuInicial.menucvs1()
        
        elif opcao == 2:
            menuInicial.menucvs2()
        
        if opcao < 1:
            opcao = 2
            menuInicial.menucvs1()
        
        if opcao > 2:
            opcao = 1
            menuInicial.menucvs2()
        
        opcao, escolha = opcoesmenu(escolha, opcao)
        
    elif user.classe == 2:
        print(f"Clóvis: ᴘᴏᴅᴇ ᴄʀᴇʀ, ᴛᴏ ᴍᴇ ʟᴇᴍʙʀᴀɴᴅᴏ... sᴇ ᴇᴜ ɴᴀ̃ᴏ ᴍᴇ ᴇɴɢᴀɴᴏ sᴇᴜ ᴀʀᴄᴏ ᴇʀᴀ ᴏ ᴄᴏᴍ {user.danoArma} ᴅᴇ ᴅᴀɴᴏ ᴇ {user.speedArma} ᴅᴇ ᴠᴇʟᴏᴄɪᴅᴀᴅᴇ ᴅᴇ ᴀᴛᴀǫᴜᴇ ɴᴇ́?")

        if opcao == 1:
            menuInicial.menucvs1()
        
        elif opcao == 2:
            menuInicial.menucvs2()
        
        if opcao < 1:
            opcao = 2
            menuInicial.menucvs1()
        
        if opcao > 2:
            opcao = 1
            menuInicial.menucvs2()
        
        opcao, escolha = opcoesmenu(escolha, opcao)

if escolha == 1:
    print("ʙᴇʟᴇᴢᴀ ᴇɴᴛᴀ̃ᴏ")
    
if escolha == 2:
    print("ɴᴀ̃ᴏ ᴢᴏᴀ ɴᴀ̃ᴏ ᴄᴀʀᴀ")

print("...")
time.sleep(2)
print("Clóvis: ᴠᴀᴍᴏ ɴᴇssᴀ, ᴊᴀ́ ᴛᴏ ʀᴜɪᴍ ᴊᴀ́")
    