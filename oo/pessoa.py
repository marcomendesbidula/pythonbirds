class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    marco = Mutante(nome='Marco')
    mateus = Homem(marco, nome='Mateus')
    print(Pessoa.cumprimentar(mateus))
    print(id(mateus))
    print(mateus.cumprimentar())
    print(mateus.nome)
    print(mateus.idade)
    for filho in mateus.filhos:
       print(filho.nome)
    mateus.sobrenome = 'Mendes'
    del mateus.filhos
    mateus.olhos = 2
    del mateus.olhos
    print(mateus.__dict__)
    print(marco.__dict__)
    print(Pessoa.olhos)
    print(mateus.olhos)
    print(marco.olhos)
    print(id(Pessoa.olhos), id(mateus.olhos), id(marco.olhos))
    print(Pessoa.metodo_estatico(), mateus.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), mateus.nome_e_atributos_de_classe())
    pessoa = Pessoa('anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(marco, Pessoa))
    print(isinstance(marco, Homem))
    print(marco.olhos)
    print(mateus.cumprimentar())
    print(marco.cumprimentar())
