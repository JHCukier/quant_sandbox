import numpy as np
import pandas as pd

class PortfolioRisk:
    def __init__(self, precos_simulados, strike, quantidade, premio_pago):
        self.precos_simulados = precos_simulados
        self.strike = strike
        self.quantidade = quantidade
        self.custo_inicial = quantidade * premio_pago
        self.pnl_array = None

    def calcular_risco(self):
        # Payoff de Call: max(Preço - Strike, 0)
        payoff = np.maximum(self.precos_simulados - self.strike, 0)
        
        # PnL = (Payoff * Quantidade) - Custo Inicial
        self.pnl_array = (payoff * self.quantidade) - self.custo_inicial
        
        # VaR Histórico Simulado (1º percentil)
        var_99 = np.percentile(self.pnl_array, 1)
        return var_99

    def exportar_csv(self, nome_arquivo="simulacao_pnl.csv"):
        if self.pnl_array is None:
            raise ValueError("Execute calcular_risco() antes de exportar.")
            
        df = pd.DataFrame({
            'Preco_Simulado': self.precos_simulados,
            'Lucro_Prejuizo': self.pnl_array
        })
        df.to_csv(nome_arquivo, index=False, sep=';', decimal=',')