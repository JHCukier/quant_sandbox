import numpy as np

class InterestRateSwap:
    descricao = """
    === INTEREST RATE SWAP (IRS) ===
    O meu entendimento: Um derivativo onde duas partes trocam seus fluxos de caixa,
    geralmente trocando uma taxa fixa por uma taxa variável, buscando previsibilidade
    usando um valor de referência invisível (Valor Nocional, que nunca troca de mãos).
    A r_fixa tem que ser calculada com precisão e algoritmos pesados para que o DCF
    para ambos os lados seja 0.
    
    Matemática:
    
    V_swap = PV_fixa - PV_flutuante
    
             T                             T
    V_swap = Σ [ N * r_fixa / (1+r)^t ] -  Σ [ N * r_flut_t / (1+r)^t ]
            t=1                           t=1

    Onde:
    N        = Valor Nocional (Tamanho do principal do contrato)
    r_fixa   = Taxa fixa acordada (Perna Fixa)
    r_flut_t = Taxa flutuante projetada para o período 't' (Perna Flutuante)
    r        = Taxa de desconto
    """

    def __init__(self, notional: float, fixed_rate: float, discount_rate: float):
        self.notional = notional
        self.fixed_rate = fixed_rate
        self.discount_rate = discount_rate

    def calculate_value(self, floating_rates: list) -> float:
        """
        Calcula o Valor Presente Líquido do Swap para a ponta que RECEBE fixo e PAGA flutuante.
        """
        rates_array = np.array(floating_rates)
        periods = np.arange(1, len(rates_array) + 1)
        
        # OTIMIZAÇÃO: Vetorização dos fatores de desconto
        discount_factors = 1 / ((1 + self.discount_rate) ** periods)
        
        # 1. PV da Perna Fixa (fluxos iguais todos os anos)
        fixed_leg_cfs = self.notional * self.fixed_rate
        pv_fixed = np.sum(fixed_leg_cfs * discount_factors)
        
        # 2. PV da Perna Flutuante (fluxos variam conforme as projeções de taxa)
        floating_leg_cfs = self.notional * rates_array
        pv_floating = np.sum(floating_leg_cfs * discount_factors)
        
        # 3. Resultado líquido da troca
        return float(pv_fixed - pv_floating)