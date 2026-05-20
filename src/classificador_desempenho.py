from .exceptions import StatusInconclusivoError


class ClassificadorDesempenho:
    def definir_situacao(self, media: float) -> str:
        if media is None:
            raise StatusInconclusivoError
        if media >= 7.0:
            return "APROVADO"
        if media >= 4.0:
            return "RECUPERACAO"
        return "REPROVADO"

    def pode_realizar_exame(self, media: float) -> bool:
        return media >= 4.0 and media < 7.0

    def formatar_resumo(self, nome: str, media: float) -> str:
        situacao = self.definir_situacao(media)
        return f"Aluno: {nome} | Média: {media} | Situação: {situacao}"

    def atingiu_criterio_aprovacao(self, media: float) -> bool:
        return media >= 7.0
