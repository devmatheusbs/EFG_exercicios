class Livro():
    def __init__(self, titulo, autor, editora, genero, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.genero = genero
        self.data_publicacao = data_publicacao
    qtd_copias = 0
    def add_copia(self, qtd):
        self.qtd_copias += qtd
    def del_copia(self, qtd):
        self.qtd_copias -= qtd
    
o_hobbit = Livro('O hobbit', 'J. R. R. Tolkien', 'HarperCollins', 'Ficção', '2019')
o_hobbit.add_copia(1)
print(vars(o_hobbit), o_hobbit.qtd_copias)       
