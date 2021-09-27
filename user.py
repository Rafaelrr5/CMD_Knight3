from Armas import Arco,Espada

class user:
    
    def __init__(self, classe, vida, atk , defesa, energia, ArmaInicial):
        ArmaInicial = Espada(2,1)
        self.classe = classe
        self.vida = vida
        self.atk = atk
        self.defesa = defesa
        self.energia = energia
        
        if classe == 1:
            self.ArmaInicial = Espada(2,1)
        elif classe == 2:
            self.ArmaInicial = Arco(2,1)
    
        self.danoArma = ArmaInicial.dano
        self.speedArma = ArmaInicial.speed

