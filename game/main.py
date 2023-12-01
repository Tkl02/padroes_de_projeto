#main
from builder import *
from observer import *
from state import *
from decorator import EquiparItemDecorator

torre = Torre()
# nome = input('Digite o nome do personagem: ')
# item = input('1 - espada de aco / 2 - cajado magico: ')

nome = 'pzl'
item = 1

if item == 1:
    item = 'espada de aco'
if item == 2:
    item = 'cajado magico'

personagem = Personagem(nome)
personagem.add_observer(XPObserver(personagem))

personagem_com_item = EquiparItemDecorator(personagem, nome)
personagem_com_item.equipar_item(item)


def jogar_jogo(personagem):
    game_state = GameState(personagem)
    while game_state.state is not None:
        game_state.state()

jogar_jogo(personagem_com_item)
