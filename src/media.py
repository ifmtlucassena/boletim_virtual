from .exceptions import ListaNotasVaziaError

class Media:
    def media_simples(self, notas: list) -> float:
        if len(notas) == 0:
            raise ListaNotasVaziaError
        return sum(notas) / len(notas)

    def validar_intervalo(self, nota: float) -> bool:
        return nota >= 0.0 and nota <= 10.0

    def verificar_discrepancia(self, notas: list) -> bool:
        if len(notas) == 0:
            raise ListaNotasVaziaError
        return max(notas) - min(notas) > 5.0
