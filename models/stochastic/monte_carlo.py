import numpy as np

class MonteCarloEngine:
    def __init__(self, num_paths: int = 10000, dt: float = 1/252):
        """
        Motor de Simulação de Monte Carlo.

        Fórmulas de Precificação (Opção de Compra Europeia):
        1. Liquidação (Payoff) no Vencimento (T): 
        Payoff = max(S_T - K, 0)
        2. Esperança Matemática do Retorno: 
        E[Payoff] = media_aritmetica(todos_os_cenarios_simulados)
        3. Valor Presente (Desconto Contínuo no Tempo): 
        PV = E[Payoff] * exp(-r * T)
        
        :param num_paths: Quantidade de cenários paralelos a serem simulados.
        :param dt: Passo de tempo (default 1/252 representa 1 dia útil em anos).
        """
        self.num_paths = num_paths
        self.dt = dt

    def price_european_call(self, model, S0: float, K: float, T: float, r: float) -> float:
        """
        Precifica uma Opção de Compra (Call) Europeia usando os cenários do modelo fornecido.
        
        :param model: Instância de um modelo estocástico (ex: GeometricBrownianMotion).
        :param S0: Preço atual do ativo subjacente.
        :param K: Preço de exercício (Strike) da opção.
        :param T: Tempo até o vencimento (em anos).
        :param r: Taxa livre de risco (para desconto do valor futuro).
        """
        # 1. Delega a geração da matriz de preços para o modelo injetado
        paths = model.simulate_paths(S0, T, self.dt, self.num_paths)
        
        # 2. Isola apenas a última linha da matriz (os preços finais no vencimento T)
        terminal_prices = paths[-1]
        
        # 3. Calcula o Payoff da Call Europeia: Max(S_T - K, 0)
        payoffs = np.maximum(terminal_prices - K, 0)
        
        # 4. Calcula a média de todos os milhares de cenários futuros
        # Pela Lei dos Grandes Números, se rodarmos num_paths suficientes 
        # (como 10.000 ou 100.000), a média simples de todos esses pagamentos futuros
        # converge para a resposta correta da Equação Diferencial.
        expected_payoff = np.mean(payoffs)
        
        # 5. Traz o valor esperado do futuro para o presente descontando a taxa livre de risco
        discount_factor = np.exp(-r * T)
        present_value = expected_payoff * discount_factor
        
        return present_value