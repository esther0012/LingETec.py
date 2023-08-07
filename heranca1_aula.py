"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Com base nos conceitos de POO, vamos trabalhar com duas classes (entidades).
implemente a entidade funcionario com estas características cpf, nome e salario.
E a entidade gerente com estas características cpf, nome, salario, senha e
quantidade de funcionários que ele gerencia. Implemente estes itens.

...
15-h1- Conceito de herança: eliminar código repetido e herdar atributos e métodos
16- A subclasse Gerente herda da superclasse Funcionario
17- Altere o construtor da subclasse Gerente.
18- Rode a função main com as alterações realizadas.
19- Os funcionários recebem uma bonificação. Todos os funcionários recebem 10% do
    valor do salário.
    Então: crie o método bonificacao, ele não recebe nada e retorna o valor da bonificação.
20- Mostre a bonificacao das instâncias (objetos) f1 e g1.

"""

class Funcionario(object):                          # Superclasse ou classe pai
    def __init__(self, cpf, nome, salario=0.0):     # Construtor com valor default
        self.cpf = cpf
        self.nome = nome                            # Atributos de instância
        self.salario = salario
    def get_cpf(self):                              # Consulta
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):                  # Altera na memória
        self.nome = novo_nome
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    def __str__(self):                              # Método mágico ou método dunder
        # s = 'Nome: ' + self.nome+ ',  CPF: ' + self.cpf + ', salário: ' + str(self.salario)
        # s = "Nome: {}, CPF: {}, salario: {:.2f}" .format(self.nome, self.cpf, self.salario)
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}"     # f-string
        return s                                    # As linhas acima são equivalentes
    def bonificacao(self):
        vlr_bonificacao = self.salario * 0.10   # Usando uma variável
        return vlr_bonificacao


# A sublcasse Gerente (filha) herda da superclasse Funcionario (pai)
# Sintaxe:
# class NomeSubclasse(NomeSuperclasse):
class Gerente(Funcionario):                         # class NomeSubclasse(NomeSuperclasse):
    def __init__(self, cpf, nome, salario, senha, qtd_gerencia=0):
        # self.cpf = cpf                            # Elimina atributos repetidos
        # self.nome = nome
        # self.salario = salario
        super().__init__(cpf, nome, salario)        # Chama o construtor da superclasse
        self.senha = senha
        self.qtd_gerencia = qtd_gerencia
    # def get_cpf(self):                            # Elimina métodos repetidos
    #     return self.cpf
    # def set_cpf(self, novo_cpf):
    #     self.cpf = novo_cpf
    # def get_nome(self):
    #     return self.nome
    # def set_nome(self, novo_nome):
    #     self.nome = novo_nome
    # def get_salario(self):
    #     return self.salario
    # def set_salario(self, novo_salario):
    #     self.salario = novo_salario
    def get_qtd_gerencia(self):
        return self.qtd_gerencia
    def set_qtd_gerencia(self, nova_qtd):
        self.qtd_gerencia = nova_qtd
    def autentica(self):                            # Solução 1
        senha = input("Senha: ")
        if self.senha == senha:
            print("Acesso permitido.")
            return True
        else:
            print("Acesso negado.")
            return False

    def __str__(self):
        s1 = super().__str__()
        s = s1 + ", Qtd.: {}" .format(self.qtd_gerencia)
        return s

if __name__ == '__main__':
    f1 = Funcionario('123', 'Paulo', 1000.00)   # Cria o objeto f1, chama o construtor
    print(f1)                                   # print(f1.__str__())   # Teste
    # <__main__.Funcionario object at 0x00000159D5FFB2C8>
    print(f'- Funcionário 1:\nNome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')
    print('Salário:', f1.get_salario())
    f1.set_nome('Vinícius')
    print(f'Nome alterado: {f1.get_nome()}')
    f2 = Funcionario('12345', 'Ana')            # Cria o objeto f2, chama o construtor
    print(f2)                                   # print(f1.__str__())   # Teste
    print(f'- Funcionário 2:\nNome: {f2.get_nome()}')
    print(f'CPF: {f2.get_cpf()}')
    print('Salário:', f2.get_salario())
    f2.set_nome('Emily')
    print(f'Nome alterado: {f2.get_nome()}')
    # print(f1.__str__())                print(f1)                        # Teste
    print (vars(f1))
    #print(f2.__str__())               # print(f2)                        # Teste
    print (vars(f2))
    g1 = Gerente('234', 'Paula', 3000.0, 's1', 5)  # g1 é um objeto da classe Gerente
    print(g1)                                      # print(g1.__str__())   # Teste
    # <heranca0_gerente.Gerente object at 0x000001C23ECFB0A0>
    print(f'- Gerente 1:\nCPF: {g1.get_cpf()}')
    print('Nome:', g1.get_nome())
    print('Salário:', g1.get_salario())
    print('Qtd. funcionários:', g1.get_qtd_gerencia())
    g1.set_nome('Alice')
    print(f'Nome alterado: {g1.get_nome()}')
    # print(g1.__str__())                         print(g1), conseguiu usando o __str__?
    print (vars(g1))
    r = g1.autentica()                          # O método retorna True ou False
    print(r)
    print(g1.autentica())                       # Linhas equivalentes
    # r = f1.autentica()                    # Erro, Funcionario não tem método autentica
    # AttributeError: 'Funcionario' object has no attribute 'autentica'
    g2 = Gerente('34', 'Paulo', 5000.0, 's2', 3)
    #print(g2.__str__())                          print(g2), conseguiu usando o __str__?
    print (vars(g2))
    print('- Gerente 2:\nCPF:', g2.get_cpf())
    print('Nome:', g2.get_nome())
    print('Salário:', g2.get_salario())
    print('Qtd. funcionários:', g2.get_qtd_gerencia())
    bonificacao_f1 = f1.bonificacao()               # Usando uma variável e objeto da superclasse
    print("Bonificação de f1", bonificacao_f1)
    print("Bonificação de g1", g1.bonificacao())    # uso com um objeto da subclasse



class Vendedor:
    def __int__(self, nome, cpf, salario, vVendas, pCent):
        super().__int__(nome, cpf, salario, vVendas, pCent)
