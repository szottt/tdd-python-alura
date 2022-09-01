from codigo.bytebank import Funcionario


from codigo.bytebank import Funcionario

import pytest
from pytest import mark


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

    # @mark.skip
    def test_quando_o_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(
            entrada_nome, '01/01/1991', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('Ana', '13/03/1997', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_o_funcionario_recebe_um_salario_muito_alto_calcular_bonus_reecebe_1000000_deve_retornar_exceprion(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario('Ana', '13/03/1997', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
