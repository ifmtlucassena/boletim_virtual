import pytest
from src.classificador_desempenho import ClassificadorDesempenho
from src.exceptions import StatusInconclusivoError


class TestClassificadorDesempenho:
    def setup_method(self):
        self.classificador = ClassificadorDesempenho()

    def test_definir_situacao_aprovado_quando_media_maior_ou_igual_a_sete(self):
        assert self.classificador.definir_situacao(7.0) == "APROVADO"

    def test_definir_situacao_recuperacao_quando_media_entre_quatro_e_seis_virgula_nove(self):
        assert self.classificador.definir_situacao(5.0) == "RECUPERACAO"

    def test_definir_situacao_reprovado_quando_media_menor_que_quatro(self):
        assert self.classificador.definir_situacao(3.0) == "REPROVADO"

    def test_definir_situacao_com_media_nula_lanca_excecao(self):
        with pytest.raises(StatusInconclusivoError):
            self.classificador.definir_situacao(None)

    def test_pode_realizar_exame_quando_em_recuperacao(self):
        assert self.classificador.pode_realizar_exame(5.0) is True

    def test_formatar_resumo_retorna_string_com_nome_media_e_situacao(self):
        resumo = self.classificador.formatar_resumo("João Silva", 8.0)
        assert "João Silva" in str(resumo)
        assert "APROVADO" in str(resumo)

    def test_atingiu_criterio_aprovacao_quando_media_suficiente(self):
        assert self.classificador.atingiu_criterio_aprovacao(7.0) is True