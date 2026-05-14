from .exceptions import NotaInvalidaError

class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota: float) -> None:
        if not isinstance(nota, (int, float)) or nota < 0 or nota > 10:
            raise NotaInvalidaError
        self.notas.append(float(nota))

    def get_notas(self) -> list:
        return self.notas

    def limpar_notas(self) -> None:
        self.notas = []

    def get_quantidade_notas(self) -> int:
        return len(self.notas)