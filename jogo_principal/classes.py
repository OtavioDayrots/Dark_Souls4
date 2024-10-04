#Classe pai de todos os personagens.
class Personagens:
    def __init__(self, img, largura, altura, pos_x, pos_y, vida, velocidade, dano) -> None:
        self.vida = vida
        self.velocidade = velocidade
        self.dano = dano
        self.img = img
        self.largura = largura
        self.altura = altura
        self.pos_x = pos_x
        self.pos_y = pos_y

#Classe de todas as armas.
class Armas:
    def __init__(self, dano, alcance, poder) -> None:
        self.dano = dano
        self.alcance = alcance
        self.poder = poder
