from cargo import Cargo
from funcionario import Funcionario
from dependente import Dependente


cargo1 = Cargo(10000, 'Gerente')
cargo2 = Cargo(1000, 'Estagiário')

funcionario1 = Funcionario('Davi da Silva', '111111', cargo1)
funcionario2 = Funcionario('Ale Ine','22222', cargo1)
funcionario3 = Funcionario('Theus Desemprego','33333', cargo2)

funcionario1.add_dependente('joao','44444')
funcionario1.add_dependente('carlos','55555')
funcionario1.add_dependente('joao da silva','66666')

funcionario1.rem_dependente('44444')
for dependente in funcionario1.dependentes:
    print(dependente.nome)