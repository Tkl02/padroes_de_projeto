#decorators.py

class Componente:
    def operacao(self):
        pass

class Personagem(Componente):
    def __init__(self, nome):
        self.nome = nome
        self.forca = 10
        self.vida = 1
        self.xp = 0
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def operacao(self):
        print(f"Operação no Personagem: {self.nome} | Força: {self.forca} | Vida: {self.vida} | XP: {self.xp}")

class Decorator(Componente):
    def __init__(self, componente):
        self.componente = componente

    def operacao(self):
        self.componente.operacao()

# Em decorators.py

# Em decorators.py

class EquiparItemDecorator(Decorator):
    def __init__(self, componente, nome):
        super().__init__(componente)
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    def equipar_item(self, item):
        print(f"{self.nome} equipou o item: {item}")

    def operacao(self):
        super().operacao()
        print(f"{self.nome} está pronto para a batalha!")

    # Adicionando métodos e propriedades para repassar chamadas ao componente original
    @property
    def forca(self):
        return self.componente.forca

    @property
    def vida(self):
        return self.componente.vida

    @vida.setter
    def vida(self, value):
        self.componente.vida = value

    @property
    def xp(self):
        return self.componente.xp

    @xp.setter
    def xp(self, value):
        self.componente.xp = value
