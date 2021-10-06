class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes


    def dar_Like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome   
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Duracao: {self.duracao} - Likes: {self._likes}'
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'

class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]
    @property
    def listagem(self):
        return self._programa

    def __len__(self):
        return len(self._programa)

vingadores = Filme('vingadores - guerra infinita', 2018, 180)
atlanta = Serie('Atlanta', 2010, 8)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_Like()
demolidor.dar_Like()
demolidor.dar_Like()
demolidor.dar_Like()
demolidor.dar_Like()
atlanta.dar_Like()
atlanta.dar_Like()
tmep.dar_Like()
tmep.dar_Like()
tmep.dar_Like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'{demolidor in playlist_fim_de_semana}')