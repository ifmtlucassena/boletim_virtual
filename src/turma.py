
from .exceptions import TurmaLotadaError
from .media import Media


class Turma:
    def __init__(self, limite: int = 40):
        self.limite = limite
        self.alunos = []
        self.media = Media()

    def adicionar_aluno(self, aluno) -> None:
        if len(self.alunos) >= self.limite:
            raise TurmaLotadaError

        self.alunos.append(aluno)

    def remover_aluno_por_nome(self, nome: str) -> None:
        self.alunos = [aluno for aluno in self.alunos if aluno.nome != nome]

    def calcular_media_turma(self) -> float:
        if not self.alunos:
            return 0.0

        medias = []

        for aluno in self.alunos:
            notas = aluno.get_notas()

            if len(notas) > 0:
                media_aluno = self.media.media_simples(notas)
                medias.append(media_aluno)

        if len(medias) == 0:
            return 0.0

        return sum(medias) / len(medias)

    def contar_alunos(self) -> int:
        return len(self.alunos)
