import Armas

class user:
            
    def __init__(self, nome, classe, vida, atk , defesa, energia, ArmaInicial):
        ArmaInicial = Armas.Espada(2,1)
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.atk = atk
        self.defesa = defesa
        self.energia = energia
        
        if classe == 1:
            self.ArmaInicial = Armas.Espada(2,1)
        elif classe == 2:
            self.ArmaInicial = Armas.Arco(2,1)
    
        self.danoArma = ArmaInicial.dano
        self.speedArma = ArmaInicial.speed

    @property
    def nome(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._nome

    @nome.setter
    def nome(self, nome):
        print("setter of x called")
        self._nome = nome