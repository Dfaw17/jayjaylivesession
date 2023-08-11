import pytest


class TestMatematikaDasar:

    tester = "DAFFA"

    @pytest.mark.skipif(tester != "FAWWAZ", reason="tester is not fawwaz")
    def test_penjumlahan(self):
        a = 5
        b = 3
        c = 8
        assert c == a + b

    @pytest.mark.skip(reason = "library not support for this test case, waiting library upgrade")
    def test_pengurangan(self):
        a = 5
        b = 3
        c = 10
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


class TestMatematikaDasar2:

    @pytest.mark.xfail(reason = "bugs from third party")
    def test_penjumlahan(self):
        a = 5
        b = 3
        c = 9
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
