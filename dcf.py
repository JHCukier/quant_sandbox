import numpy as np

class CashFlowPricer:
    descricao = """
    === DESCONTO DE FLUXOS DE CAIXA (DCF) ===
    O meu aprendizado: Traz uma série de fluxos de caixa futuros e variáveis 
    para o valor presente, descontando o custo de oportunidade (taxa de desconto).
    Calcula o Net Present Value (Valor Presente Líquido) para tal
    """

    # O Construtor: define o estado inicial do objeto financeiro
    def __init__(self, discount_rate: float):
        # A taxa de desconto é o custo de oportunidade (ex: 0.10 para 10%)
        self.discount_rate = discount_rate

    def calculate_npv(self, cash_flows: list) -> float:
        """
        Calcula o Valor Presente Líquido (NPV) de uma lista de fluxos de caixa.
        """
        # 1. Converte a lista normal do Python para um array de alta performance
        cf_array = np.array(cash_flows)
        
        # 2. Cria o vetor de tempo: [1, 2, 3, ...] com base na quantidade de fluxos,
        # Poupando entradas
        periods = np.arange(1, len(cf_array) + 1)
        
        # OTIMIZAÇÃO: Vetorização do fator de desconto (sem loops 'for')
        discount_factors = 1 / ((1 + self.discount_rate) ** periods)
        
        # 3. Multiplica os fluxos pelos fatores de desconto e soma tudo (Net Present Value)
        npv = np.sum(cf_array * discount_factors)
        
        return float(npv)