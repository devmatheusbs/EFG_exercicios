class livro:
    def __init__(self,titulo,autor,data,editora,genero,qtd=0):
        self.titulo=titulo
        self.autor=autor
        self.data=data
        self.editora=editora
        self.genero=genero
        self.qtd=qtd

    def info(self):
        print(f"Título: {self.titulo}\n Autor: {self.autor}\n Data: {self.data}\n Editora: {self.editora}\n Gênero: {self.genero}\n Quantidade em Estoque: {self.qtd}")
    
    def add_livro(self,qtd):
        self.qtd+=qtd
    
    def rem_livro(self,qtd):
        if qtd>self.qtd:
            print("Operação Inválida. Estoque: ",self.qtd)
        elif qtd<=self.qtd:
            self.qtd-=qtd

        
        
    
        