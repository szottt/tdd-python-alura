from bytebank import Funcionario

#igor = Funcionario('Igor Szot', '13/03/1991', 1000)
# print(igor.idade())


def test_idade():
    func_test = Funcionario('teste', '13/10/1991', 1240)
    print(f'Teste = {func_test.idade()}')


test_idade()
