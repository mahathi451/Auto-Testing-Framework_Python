from src.calculator import Calculator

class TestIntegration:
    def test_full_calculation_flow(self):
        calc = Calculator()
        result = calc.add(10, calc.multiply(2, 5))
        assert result == 20

    def test_error_propagation(self):
        calc = Calculator()
        try:
            calc.divide(10, 0)
        except ValueError:
            assert True
        else:
            assert False
