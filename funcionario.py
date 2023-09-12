from pessoa import Pessoa
from cargo import Cargo
from dependente import Dependente

class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, cargo: Cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo
        self.dependentes = []

    def add_dependente(self, nome, cpf):
        self.dependentes.append(Dependente(nome, cpf))
    
    def rem_dependente(self, cpf):
        for dependente in self.dependentes:
            if cpf in self.dependentes:
                self.dependentes.remove(dependente)
