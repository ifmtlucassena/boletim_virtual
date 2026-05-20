import pytest
from src.aluno import Aluno
from src.exceptions import NotaInvalidaError


class TestAluno:
    def setup_method(self):
        self.aluno = Aluno("João Silva")

    def test_adicionar_nota_valida(self):
        self.aluno.adicionar_nota(8.5)
        assert 8.5 in self.aluno.get_notas()

    def test_adicionar_nota_negativa_lanca_excecao(self):
        with pytest.raises(NotaInvalidaError):
            self.aluno.adicionar_nota(-1.0)

    def test_adicionar_nota_acima_de_dez_lanca_excecao(self):
        with pytest.raises(NotaInvalidaError):
            self.aluno.adicionar_nota(10.1)

    def test_get_notas_retorna_lista(self):
        self.aluno.adicionar_nota(5.0)
        self.aluno.adicionar_nota(7.0)
        assert self.aluno.get_notas() == [5.0, 7.0]

    def test_limpar_notas_esvazia_lista(self):
        self.aluno.adicionar_nota(10.0)
        self.aluno.limpar_notas()
        assert self.aluno.get_notas() == []

    def test_get_quantidade_notas_retorna_total_correto(self):
        self.aluno.adicionar_nota(10.0)
        self.aluno.adicionar_nota(9.0)
        assert self.aluno.get_quantidade_notas() == 2
