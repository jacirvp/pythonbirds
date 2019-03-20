class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    # metodos de Classe
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    sofia = Pessoa(nome='Sofia')
    valentina = Pessoa(nome="Valentina")
    jacir = Homem(sofia, nome='Jacir')
    jacir = Mutante(nome='Jacir')
    print(Pessoa.cumprimentar(jacir))
    print(id(jacir))
    print(jacir.cumprimentar())
    print(jacir.nome)

    for filho in jacir.filhos:
        print(filho.nome)

    # atributos dinâmicos - criados em tempo de execução

    jacir.sobrenome = 'Pieniak'
    print(jacir.sobrenome)
    print(jacir.__dict__)

    # deleta o atributo dinâmico em tempo de execução
    del jacir.sobrenome
    print(jacir.__dict__)

    # teste atributos de classe

    print(Pessoa.olhos)
    print(jacir.olhos)
    print(jacir.__dict__)

    # teste metodos de classe

    print(id(Pessoa.olhos), id(jacir.olhos))
    print(Pessoa.metodo_estatico(), jacir.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), jacir.nome_e_atributos_de_classe())

    # teste Herança

    print(isinstance(sofia, Pessoa))
    print(isinstance(jacir, Homem))

    #teste de sobrescrita de atributo de dados
    print(jacir.olhos)
