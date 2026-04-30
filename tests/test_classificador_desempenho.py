from src.classificador_desempenho import ClassificadorDesempenho
from src.exceptions import StatusInconclusivoError


class TestClassificadorDesempenho:
    def setup_method(self):
        self.classificador = ClassificadorDesempenho()

    def test_definir_situacao_aprovado_quando_media_maior_ou_igual_a_sete(self):
        pass

    def test_definir_situacao_recuperacao_quando_media_entre_quatro_e_seis_virgula_nove(self):
        pass

    def test_definir_situacao_reprovado_quando_media_menor_que_quatro(self):
        pass

    def test_definir_situacao_com_media_nula_lanca_excecao(self):
        pass

    def test_pode_realizar_exame_quando_em_recuperacao(self):
        pass

    def test_formatar_resumo_retorna_string_com_nome_media_e_situacao(self):
        pass

    def test_atingiu_criterio_aprovacao_quando_media_suficiente(self):
        pass
