import unittest
import numpy as np
from models.risk.risk_analysis import PortfolioRisk

class TestPortfolioRisk(unittest.TestCase):
    def test_calculo_pnl_correto(self):
        # Arrange (Forjamos 3 cenários estáticos para não depender do Monte Carlo)
        precos_mock = np.array([40.0, 50.0, 60.0])
        strike = 50.0
        quantidade = 100
        premio = 2.0
        
        carteira = PortfolioRisk(precos_mock, strike, quantidade, premio)
        
        # Act
        carteira.calcular_risco()
        
        # Assert
        # Esperamos que o PnL seja [-200, -200, 800]
        pnl_esperado = np.array([-200.0, -200.0, 800.0])
        
        np.testing.assert_array_equal(carteira.pnl_array, pnl_esperado)