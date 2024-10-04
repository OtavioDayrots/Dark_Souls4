#Classe pai de todos os personagens.
class Personagens:
    def __init__(self, vida, velocidade, dano) -> None:
        self.vida = vida
        self.velocidade = velocidade
        self.dano = dano

#Classe de todas as armas.
class Armas:
    def __init__(self, dano, alcance, poder='NULL') -> None:
        self.dano = dano
        self.alcance = alcance
        self.poder = poder
