from src.media import Media
from src.exceptions import ListaNotasVaziaError


class TestMedia:
    def setup_method(self):
        self.media = Media()

    def test_media_simples_calcula_corretamente(self):
        pass

    def test_media_simples_com_lista_vazia_lanca_excecao(self):
        pass

    def test_validar_intervalo_nota_valida(self):
        pass

    def test_validar_intervalo_nota_invalida(self):
        pass

    def test_verificar_discrepancia_quando_diferenca_maior_que_cinco(self):
        pass

    def test_verificar_discrepancia_quando_diferenca_menor_ou_igual_a_cinco(self):
        pass
