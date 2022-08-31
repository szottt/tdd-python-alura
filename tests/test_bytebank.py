from codigo.bytebank import Funcionario


from codigo.bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_13_10_1991_deve_retornar_31(self):
        entrada = '13/10/1991'  # GIVEN
        esperado = 31

        funcionario_teste = Funcionario('Teste', entrada, 1000)
        resultado = funcionario_teste.idade()  # When

        assert resultado == esperado  # Then
