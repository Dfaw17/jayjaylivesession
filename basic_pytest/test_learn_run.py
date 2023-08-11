# pytest
# pytest basic_pytest/test_learn_run.py
# pytest basic_pytest/test_learn_run.py::TestMatematikaDasar2 -v
# pytest basic_pytest/test_learn_run.py::TestMatematikaDasar2::test_pengurangan -v
# pytest -v
# pytest -q

class TestMatematikaDasar:

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


class TestMatematikaDasar2:

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
