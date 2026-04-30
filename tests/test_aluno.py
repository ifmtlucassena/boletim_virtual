from src.aluno import Aluno
from src.exceptions import NotaInvalidaError


class TestAluno:
    def setup_method(self):
        self.aluno = Aluno("João Silva")

    def test_adicionar_nota_valida(self):
        pass

    def test_adicionar_nota_negativa_lanca_excecao(self):
        pass

    def test_adicionar_nota_acima_de_dez_lanca_excecao(self):
        pass

    def test_get_notas_retorna_lista(self):
        pass

    def test_limpar_notas_esvazia_lista(self):
        pass

    def test_get_quantidade_notas_retorna_total_correto(self):
        pass
