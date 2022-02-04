class Pessoa:
    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    marco = Pessoa(nome='Marco')
    mateus = Pessoa(marco, nome='Mateus')
    print(Pessoa.cumprimentar(mateus))
    print(id(mateus))
    print(mateus.cumprimentar())
    print(mateus.nome)
    print(mateus.idade)
    for filho in mateus.filhos:
       print(filho.nome)
    mateus.sobrenome = 'Mendes'
    del mateus.filhos
    print(mateus.__dict__)
    print(marco.__dict__)