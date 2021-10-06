class Cliente:
    def __init__(self, nome):
        self.__nome = nome
      
    @property  
    def get_nome(self):
        return self.nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
