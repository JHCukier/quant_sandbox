import math

class BlackScholesPricer:
    """
    Motor analítico para precificação exata de opções europeias.
    
    Equação de Black-Scholes-Merton:
    C = S_0 * N(d1) - K * e^{-rT} * N(d2)
    
    Onde:
    d1 = (ln(S0/K) + (r + sigma^2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    N(x) = Função de Distribuição Acumulada Normal
    """
    
    def _norm_cdf(self, x: float) -> float:
        """
        Calcula a Distribuição Normal Acumulada N(x) usando a função Erro (erf) nativa do Python.
        """
        return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

    def price_european_call(self, S0: float, K: float, T: float, r: float, sigma: float) -> float:
        """
        Calcula o preço exato da Call Europeia.
        """
        # Se a opção já venceu (T=0), o preço é apenas o payoff imediato
        if T <= 0:
            return max(S0 - K, 0.0)
            
        d1 = (math.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        
        call_price = S0 * self._norm_cdf(d1) - K * math.exp(-r * T) * self._norm_cdf(d2)
        
        return call_price