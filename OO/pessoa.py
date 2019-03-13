class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    sofia = Pessoa(nome='Sofia')
    valentina = Pessoa(nome="Valentina")
    jacir = Pessoa(sofia, nome='Jacir')
    jacir = Pessoa(valentina, nome = 'Jacir')
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

    print(Pessoa.olhos)
    print(jacir.olhos)
    jacir.olhos = 3
    print(jacir.__dict__)








