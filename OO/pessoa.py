class Pessoa():

    def __init__(self, *filhos, nome=None, idade=35,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    julio = Pessoa(nome='Júlio', idade=25)
    luciano = Pessoa(renzo, julio, nome='Luciano')
    print(renzo.cumprimentar())
    print(luciano.filhos)
    renzo.sobrenome = 'Ramalho'
    del renzo.sobrenome
    for filho in luciano.filhos:
        print(filho.nome)
print(luciano.__dict__)
print(renzo.__dict__)