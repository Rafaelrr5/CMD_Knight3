import Armas

class user:
    nome = ""
    classe = 0
    espada = arco = flecha = 0
    vida = atk = defesa = energia = 0
    danoArma = speedArma = 0
    ArmaInicial = 0

    
    def criacao(self, classe, vida, atk , defesa, energia, ArmaInicial):
         self.classe = classe
         self.vida = vida
         self.atk = atk
         self.defesa = defesa
         self.energia = energia
         self.ArmaInicial = ArmaInicial
         self.ArmaInicial.danoArma = ArmaInicial.danoArma
         self.ArmaInicial.speedArma = ArmaInicial.speedArma
