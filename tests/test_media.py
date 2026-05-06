import pytest
from src.media import Media
from src.exceptions import ListaNotasVaziaError


class TestMedia:
    def setup_method(self):
        self.media = Media()

    def test_media_simples_calcula_corretamente(self):
        resultado = self.media.media_simples([6.0, 8.0, 10.0])
        assert resultado == 8.0

    def test_media_simples_com_lista_vazia_lanca_excecao(self):
        with pytest.raises(ListaNotasVaziaError):
            self.media.media_simples([])

    def test_validar_intervalo_nota_valida(self):
        assert self.media.validar_intervalo(7.5) is True

    def test_validar_intervalo_nota_invalida(self):
        assert self.media.validar_intervalo(11.0) is False

    def test_verificar_discrepancia_quando_diferenca_maior_que_cinco(self):
        assert self.media.verificar_discrepancia([2.0, 8.0]) is True

    def test_verificar_discrepancia_quando_diferenca_menor_ou_igual_a_cinco(self):
        assert self.media.verificar_discrepancia([5.0, 10.0]) is False
