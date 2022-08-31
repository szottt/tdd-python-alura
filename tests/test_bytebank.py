from codigo.bytebank import Funcionario


from codigo.bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_13_10_1991_deve_retornar_31(self):
        entrada = '13/10/1991'  # GIVEN
        esperado = 31

        funcionario_teste = Funcionario('Teste', entrada, 1000)
        resultado = funcionario_teste.idade()  # When

        assert resultado == esperado  # Then

    def test_quando_sobrenoome_recebe_Igor_Szot_deve_retornar_apenas_Szot(self):
        entrada = 'Igor Szot '
        esperado = 'Szot'

        igor = Funcionario(entrada, '13/10/1991', 1000)
        resultado = igor.sobrenome()

        assert resultado == esperado
