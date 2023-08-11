import pytest


class TestMatematikaDasar:

    def test_penjumlahan(self):
        a = 5
        b = 3
        c = 8
        assert c == a + b

    @pytest.mark.regression()
    def test_pengurangan(self):
        a = 5
        b = 3
        c = 2
        assert c == a - b

    def test_perkalian(self):
        a = 5
        b = 3
        c = 15
        assert c == a * b

    @pytest.mark.regression()
    def test_pembagian(self):
        a = 10
        b = 2
        c = 5
        assert c == a / b


class TestMatematikaDasar2:

    @pytest.mark.regression()
    def test_penjumlahan(self):
        a = 5
        b = 3
        c = 8
        assert c == a + b

    def test_pengurangan(self):
        a = 5
        b = 3
        c = 2
        assert c == a - b

    def test_perkalian(self):
        a = 5
        b = 3
        c = 15
        assert c == a * b

    def test_pembagian(self):
        a = 10
        b = 2
        c = 5
        assert c == a / b
