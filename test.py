import random

class Personagem:
    def __init__(self):
        self.nome = "Guerreiro"
        self.cabeca = 1
        self.peito = 1
        self.perna = 1
        self.forca = 1
        self.experiencia_atual = 0
        self.nivel = 1

    def ganhar_experiencia(self, xp):
        self.experiencia_atual += xp
        if self.experiencia_atual >= self.experiencia_necessaria():
            self.passar_de_nivel()

    def experiencia_necessaria(self):
        return int(120 * 1.2 ** (self.nivel - 1))

    def passar_de_nivel(self):
        self.experiencia_atual = 0
        self.nivel += 1
        self.forca += 10
        print(f"Parabéns! Você alcançou o nível {self.nivel} e ganhou 10 pontos de força.")

class Monstro:
    def __init__(self, nome, xp):
        self.nome = nome
        self.xp = xp

def batalha(personagem, monstro):
    print(f"Encontrou um {monstro.nome}!")
    if personagem.forca == monstro.xp:
        print("Empate! Você e o monstro são igualmente fortes.")
    elif personagem.forca > monstro.xp:
        personagem.ganhar_experiencia(monstro.xp)
        print(f"Você derrotou o {monstro.nome} e ganhou {monstro.xp} XP.")
    else:
        print(f"Você foi derrotado pelo {monstro.nome}. Game Over.")
        exit()

def main():
    personagem = Personagem()

    monstros_por_nivel = {
        1: Monstro("Goblin", 4),
        2: Monstro("Orc", 9),
        3: Monstro("Wivern", 19),
        4: Monstro("Dragão", 39),
        5: Monstro("God", "end_game")
    }

    while personagem.nivel <= 5:
        print(f"\nEstá no Nível {personagem.nivel}")
        print("Escolha sua ação:")
        print("1. Andar para o próximo nível")
        print("2. Ver Status")
        escolha = input(">>> ")

        if escolha == "1":
            monstro_atual = monstros_por_nivel[personagem.nivel]
            batalha(personagem, monstro_atual)
        elif escolha == "2":
            print(f"\nStatus do Personagem:")
            print(f"Nível: {personagem.nivel}")
            print(f"Força: {personagem.forca}")
            print(f"XP Atual: {personagem.experiencia_atual}/{personagem.experiencia_necessaria()}")
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
