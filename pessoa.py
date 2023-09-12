from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    @abstractmethod
    def mostra_dados():
        pass