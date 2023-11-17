from mobs import *
from observer import *
from state import *

torre = Torre()
nome = input('Digite o nome do personagem: ')
personagem = Personagem(nome)
personagem.add_observer(XPObserver(personagem))

def jogar_jogo(personagem):
    game_state = GameState(personagem)
    while game_state.state is not None:
        game_state.state()

jogar_jogo(personagem)