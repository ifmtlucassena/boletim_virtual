import pytest
from src.turma import Turma
from src.aluno import Aluno
from src.exceptions import TurmaLotadaError

class TestTurma:
    def setup_method(self):
        self.turma = Turma()

    def test_adicionar_aluno_com_sucesso(self):
        aluno = Aluno("Maria")

        self.turma.adicionar_aluno(aluno)

        assert self.turma.contar_alunos() == 1

    def test_adicionar_aluno_alem_do_limite_lanca_excecao(self):
        turma = Turma(limite=1)

        aluno1 = Aluno("João")
        aluno2 = Aluno("Maria")

        turma.adicionar_aluno(aluno1)

        with pytest.raises(TurmaLotadaError):
            turma.adicionar_aluno(aluno2)

    def test_remover_aluno_por_nome_com_sucesso(self):
        aluno = Aluno("Carlos")

        self.turma.adicionar_aluno(aluno)
        self.turma.remover_aluno_por_nome("Carlos")

        assert self.turma.contar_alunos() == 0

    def test_calcular_media_turma_corretamente(self):
        aluno1 = Aluno("Ana")
        aluno2 = Aluno("Pedro")

        aluno1.adicionar_nota(8.0)
        aluno1.adicionar_nota(10.0)

        aluno2.adicionar_nota(6.0)
        aluno2.adicionar_nota(8.0)

        self.turma.adicionar_aluno(aluno1)
        self.turma.adicionar_aluno(aluno2)

        resultado = self.turma.calcular_media_turma()

        assert resultado == 8.0

    def test_contar_alunos_retorna_total_correto(self):
        aluno1 = Aluno("Ana")
        aluno2 = Aluno("Pedro")

        self.turma.adicionar_aluno(aluno1)
        self.turma.adicionar_aluno(aluno2)

        assert self.turma.contar_alunos() == 2