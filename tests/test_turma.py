from src.turma import Turma
from src.aluno import Aluno
from src.exceptions import TurmaLotadaError


class TestTurma:
    def setup_method(self):
        self.turma = Turma()

    def test_adicionar_aluno_com_sucesso(self):
        pass

    def test_adicionar_aluno_alem_do_limite_lanca_excecao(self):
        pass

    def test_remover_aluno_por_nome_com_sucesso(self):
        pass

    def test_calcular_media_turma_corretamente(self):
        pass

    def test_contar_alunos_retorna_total_correto(self):
        pass
