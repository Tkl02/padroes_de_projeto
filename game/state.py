#state
from builder import *
torre = Torre()

class GameState:
    def __init__(self, personagem):
        self.personagem = personagem
        self.state = self.escolher_andar

    def escolher_andar(self):
        opcao = int(input('1-escolher de andar / 3-mostrar status / 4-sair: '))
        if opcao == 1:
            andar = int(input('1:[goblin] 2:[orc] 3:[wivern] 4:[dragon] 5:[demon] - '))
            monstro = torre.escolher_andar(andar)
            print('\033[91m' + f'apareceu um {monstro.nome}' + '\033[0m')
            self.state = self.estado_combate
            self.monstro = monstro
        elif opcao == 3:
            print('\033[92m' + f'\nNome: {self.personagem.nome} | Forca: {self.personagem.forca} | Vida: {self.personagem.vida} | XP: {self.personagem.xp}\n' + '\033[0m')
        elif opcao == 4:
            self.state = self.fim_de_jogo
        else:
            print('Opção inválida')

    def estado_combate(self):
        opt = int(input('--------------------\n1-atacar / 2-fugir:\n-------------------- '))
        if opt == 1:
            if self.personagem.forca >= self.monstro.forca:
                print('Você matou o monstro\n')
                self.personagem.xp += self.monstro.xp
                proximo_nivel(self.personagem)
                print('\033[91m' + f'apareceu um {self.monstro.nome}' + '\033[0m')
            else:
                print('Você não tem força suficiente para derrotar o monstro. Perdeu 1 vida\n')
                self.personagem.vida -= 1
                if self.personagem.vida == 0:
                    print('\033[97m' + 'GAME OVER' + '\033[0m')
                    raise SystemExit
        elif opt == 2:
            print('Você fugiu\n')
            self.state = self.escolher_andar
        else:
            print('\nOpção inválida\n')

    def fim_de_jogo(self):
        print('Fim de jogo')
        raise SystemExit