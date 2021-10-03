import random, datetime, time
import pygame, os, sys, keyboard, pyautogui
import User, Armas, Monstros
from MenusJogo import MenuIni, MenuGeral

escolha = 0
keyboard.on_press_key("esc", lambda _:pausemenu(escolha,opcao))
                               
def pausemenu(escolha,opcao):
    
    while(escolha == 0):
        
        if opcao == 1:
            MenuGeral.menuesc1()

        elif opcao == 2:
            MenuGeral.menuesc2()

        elif opcao == 3:
            MenuGeral.menuesc3()

        elif opcao == 4:
            MenuGeral.menuesc4()
            
        elif opcao == 0:
            opcao = 4
            MenuGeral.menuesc4()
        
        elif opcao == 5:
            opcao == 1
            MenuGeral.menuesc1()
        
        opcao, escolha = opcoesmenu(escolha,opcao)
        
        if escolha==1:
            break
            
        elif escolha==2:
            pass
            
        elif escolha==3:
            sys.stdout.flush()
            os.execv(sys.argv[0], sys.argv)
            
        elif escolha==4:    
            exit()

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
musica = True
user = User.user

carregamento =  0 #23

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
        print("Para manipular o menu, utilize as setinhas e a tecla espaço do seu teclado")
        print("A qualquer momento do jogo, aperte ESC para abrir o menu")
        
    if opcao == 1:
        MenuIni.menu1()
    elif opcao == 2:
        MenuIni.menu2()
    elif opcao == 3:
        MenuIni.menu3()
    elif opcao == 4:
        MenuIni.menu4()
    
    if opcao == 0:
        opcao = 4
        MenuIni.menu4()
        
    if opcao == 5:
        opcao = 1
        MenuIni.menu1()

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
        
    elif escolha == 4:
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
        MenuIni.menuclas1()
        
    elif opcao == 2:
        MenuIni.menuclas2()
    
    if opcao < 1:
        opcao = 2
        MenuIni.menuclas1()
        
    if opcao > 2:
        opcao = 1
        MenuIni.menuclas2()
        
    opcao, escolha = opcoesmenu(escolha, opcao)

if escolha == 1:
    user = user(user.nome,1,100,25,25,80,Armas.Espada(2,1))
        
elif escolha == 2:
    user = user(user.nome,2,80,40,10,100,Armas.Arco(2,1)) 

escolha = 0
time.sleep(1)
while(escolha==0): 

    if user.classe == 1:
        print(f"Clóvis: ᴘᴏᴅᴇ ᴄʀᴇʀ, ᴛᴏ ᴍᴇ ʟᴇᴍʙʀᴀɴᴅᴏ... sᴇ ᴇᴜ ɴᴀ̃ᴏ ᴍᴇ ᴇɴɢᴀɴᴏ sᴜᴀ ᴇsᴘᴀᴅᴀ ᴇʀᴀ ᴀ ᴄᴏᴍ {user.danoArma} ᴅᴇ ᴅᴀɴᴏ ᴇ {user.speedArma} ᴅᴇ ᴠᴇʟᴏᴄɪᴅᴀᴅᴇ ᴅᴇ ᴀᴛᴀǫᴜᴇ ɴᴇ́?")
        if opcao == 1:
            MenuIni.menucvs1()
        
        elif opcao == 2:
            MenuIni.menucvs2()
        
        if opcao < 1:
            opcao = 2
            MenuIni.menucvs1()
        
        if opcao > 2:
            opcao = 1
            MenuIni.menucvs2()
        
        opcao, escolha = opcoesmenu(escolha, opcao)
        
    elif user.classe == 2:

        print(f"Clóvis: ᴘᴏᴅᴇ ᴄʀᴇʀ, ᴛᴏ ᴍᴇ ʟᴇᴍʙʀᴀɴᴅᴏ... sᴇ ᴇᴜ ɴᴀ̃ᴏ ᴍᴇ ᴇɴɢᴀɴᴏ sᴇᴜ ᴀʀᴄᴏ ᴇʀᴀ ᴏ ᴄᴏᴍ {user.danoArma} ᴅᴇ ᴅᴀɴᴏ ᴇ {user.speedArma} ᴅᴇ ᴠᴇʟᴏᴄɪᴅᴀᴅᴇ ᴅᴇ ᴀᴛᴀǫᴜᴇ ɴᴇ́?")

        if opcao == 1:
            MenuIni.menucvs1()
        
        elif opcao == 2:
            MenuIni.menucvs2()
        
        if opcao < 1:
            opcao = 2
            MenuIni.menucvs1()
        
        if opcao > 2:
            opcao = 1
            MenuIni.menucvs2()
        
        opcao, escolha = opcoesmenu(escolha, opcao)

if escolha == 1:
    print("ʙᴇʟᴇᴢᴀ ᴇɴᴛᴀ̃ᴏ")
    
if escolha == 2:
    print("ɴᴀ̃ᴏ ᴢᴏᴀ ɴᴀ̃ᴏ ᴄᴀʀᴀ")

for char in "....":
    time.sleep(.5)
    print(char,end="",flush=True)

os.system("cls")
print("Clóvis: ᴠᴀᴍᴏ ɴᴇssᴀ, ᴊᴀ́ ᴛᴏ ʀᴜɪᴍ ᴊᴀ́")

print("""
      .　　　　　　　　　　 ✦ 　　　　   　 　　　˚　　　　　　　　　　　　　　　　　　　　   　　　　　　　
      .　　　　　　　　　　　 　　　. 　　 　　　　　　　 ✦ 　　　　　　　　　　 　 ‍ ‍ ‍ ‍
      　　　　 　　　　　　　　　　　　,　　   　 .　　　　　　　　　　　　　.　　　ﾟ　  　　　.　　　　　
      ✦ 　　　　　　,　　　　　　　.　　　　　　    　　　　 　　　　　　　　　　　　　　　　　　  . 
      　　　　　　　　　　　　　　　　　　    　      　　　　　        　　　　　　　　　　　　　. 　　　　　　　　.　
     .　　　　　　       　   　　　　 　　　　　　　　　　　　　　　　       　   　　　　　　　　　　　　　　　　       　   
     ✦ 　   　　　,　　　　　　　　　　　  　　　　 　　,　　　 ‍ ‍ ‍ ‍ 　 　　　　　　　　　　　　.　　　　　 　　
     .　　　　　　　　　　　　　 　           　　　　　　　　　　　　　　　　　　　. ˚　　　 　   . ,　　　　　　　　
            　    　　　　　　　　　　　　　. .　　　  　　    ✦　 
    ✦　　　　 　　　　　.　　　　　　　　　　　　　.　　　　　　　　　　　　　　　 　　   　　　　　 ✦
    　　　　　　　         　        　　　　 　　 　　　　　　　 　　　　　.　　　　　　　　　　　　　　　　　　.　　
        　　. 　 　　　　　.　　　　 　　　　　   　　　　　.　　　　　　　　　　　.　　　　　　　　　　  
    　 　˚　　 . ✦ ✦　　　　　　　　　　　　　　　　　　　ﾟ　　　　　.　　　　　　　　　　　　　　　.
    　　 　  ‍ ‍ ‍ ‍ ‍ ‍ ‍ ‍ ‍ ‍ ,　 　　　　　　　　　　　　　　* .　　　　　 　　　　　　　　　　　　　　.　　　　　                                
    ✦ 　　　　   　 　　　˚　　　　　　　　　　　　　　*　　　　　　   　　　　　　　　　　　　　　　.　　　　　　　　　　　　　　 ✦                                                                      
      """)

for char in "O céu da noite está estrelado, você olha para a imensidão espacial mas sai da distração com um barulho na trilha da floresta":
    time.sleep(.1)
    print(char, end="", flush= True)
    if keyboard.is_pressed("space"): 
        break
    
time.sleep(.5)
#https://pt.piliapp.com/cool-text/small-caps/
print("Clóvis: ᴠᴏᴄᴇ̂ ᴏᴜᴠɪᴜ ɪssᴏ?")

print("\nUm orc ladrão aparece no seu caminho")

class BatalhaTut:
    
    orc = Monstros.orc(50,5,1)
    vidauser = user.vida
    vidamonstro = orc.vida
    danomonstro = orc.dano
    danouser = user.atk
    
    def menuBatt1():
        print(f"""
            PV atual: {BatalhaTut.vidauser}/{user.vida} || Orc: {BatalhaTut.vidamonstro}/{BatalhaTut.orc.vida}
            1 - Atacar <-
            2 - Tomar poção de vida
            3 - Fugir
              """)

    def menuBatt2():
        print(f"""
            PV atual: {BatalhaTut.vidauser}/{user.vida} || Orc: {BatalhaTut.vidamonstro}/{BatalhaTut.orc.vida}
            1 - Atacar
            2 - Tomar poção de vida <-
            3 - Fugir
              """)
        
    def menuBatt3():
        print(f"""
            PV atual: {BatalhaTut.vidauser}/{user.vida} || Orc: {BatalhaTut.vidamonstro}/{BatalhaTut.orc.vida}
            1 - Atacar
            2 - Tomar poção de vida
            3 - Fugir <-
              """)
    
    def atacar(danouser,vidauser,danomonstro,vidamonstro):
        danom = random.randint((danomonstro-5), danomonstro)
        danou = random.randint((danouser-3), danouser)
        vidauser = vidauser - danom
        vidamonstro = vidamonstro - danou
        print(f"Você atingiu o monstro em cheio! Deu {danou} de dano! Mas não foi de graça, ele te deu {danom} de dano!")
        time.sleep(1.5)
        return vidauser, vidamonstro
        
    def menuprin(opcao,escolha):
        while escolha==0:
            if opcao == 1:
                BatalhaTut.menuBatt1()
                
            elif opcao == 2:
                BatalhaTut.menuBatt2()
                
            elif opcao == 3:
                BatalhaTut.menuBatt3()
                
            opcao,escolha = opcoesmenu(escolha,opcao)
            
            if escolha == 1:
                BatalhaTut.vidauser, BatalhaTut.vidamonstro = BatalhaTut.atacar(user.atk, BatalhaTut.vidauser, BatalhaTut.orc.dano, BatalhaTut.vidamonstro)
            
            elif escolha == 2:
                print("Impossível pegar uma poção agora!")
                time.sleep(2)
            
            elif escolha == 3:    
                print("Fugir agora é impossível, preciso ir com Clóvis")
                time.sleep(2)
                
while BatalhaTut.vidauser > 0 or BatalhaTut.vidamonstro > 0:
    escolha = 0
    BatalhaTut.menuprin(opcao,escolha)

    if BatalhaTut.vidauser <= 0:
        print("morreu otario")
        break
        
    elif BatalhaTut.vidamonstro <= 0:
        print("Você matou o orc!")
        print("cabo o jogo (UᴗU)")
        break
