import numpy as np

class GeometricBrownianMotion:
    def __init__(self, mu: float, sigma: float):
        """
        Inicializa o modelo estocástico do Movimento Browniano Geométrico.
        
        :param mu: Taxa esperada de retorno (drift). Em precificação neutra ao risco, é a taxa livre de risco (r).
        :param sigma: Volatilidade do ativo (desvio padrão anualizado).
        """
        self.mu = mu
        self.sigma = sigma

    def simulate_paths(self, S0: float, T: float, dt: float, num_paths: int) -> np.ndarray:
        """
        Gera os caminhos simulados usando a solução analítica exata do GBM.
        """
        # Calcula o número de passos de tempo
        num_steps = int(T / dt)
        
        # 1. Sorteio do Ruído (Processo de Wiener)
        # Cria o Z ~ N(0,1) (a função standard_normal já garante o 0 de média e 1 de variância) 
        # para cada passo de tempo (dt) e cada cenário (simulação de um caminho) (MATRIZ 2D)
        Z = np.random.standard_normal((num_steps, num_paths))
        # Usei matrizes substituindo os laços de repetiçãos (for loops)para resolver bem mais rápido
        # rodar 10.000 cenários durante 252 dias usando loops nativos do Python, o cálculo demoraria minutos,
        # pois a linguagem processa uma linha de cada vez
        # Já sendo matrizes, O NumPy envia a matriz inteira direto para a memória cache do processador (em blocos contíguos),
        # resolvendo tudo quase instantaneamente com operações lineares.
        # As matrizes tem os cenários como colunas e o tempo como linhas
        
        # 2. O Arrasto de Volatilidade (Volatility Drag)
        # Equivalente a: (mu - (sigma^2) / 2) * dt
        drift = (self.mu - 0.5 * self.sigma**2) * dt
        
        # 3. O Choque Estocástico
        # Equivalente a: sigma * sqrt(dt) * Z
        diffusion = self.sigma * np.sqrt(dt) * Z
        
        # 4. A Variação Logarítmica Diária
        daily_log_returns = drift + diffusion
        
        # 5. Acumulação no Tempo e Exponenciação
        # Matriz de preços preenchida com S0 na primeira linha
        paths = np.zeros((num_steps + 1, num_paths))
        paths[0] = S0
        
        # Aplica a base de Euler (e^x) na soma acumulada dos retornos
        paths[1:] = S0 * np.exp(np.cumsum(daily_log_returns, axis=0))
        # O axis=0 é a bússola do NumPy para saber em qual direção ele deve calcular a soma cumulativa na matriz. 
        # Em matrizes 2D (tabelas), o NumPy adota a seguinte regra direcional:
        # axis=0: Operação vertical (de cima para baixo, percorrendo as linhas).
        # axis=1: Operação horizontal (da esquerda para a direita, percorrendo as colunas).  
        # Como as nossas linhas representam a passagem dos dias (tempo) e as colunas representam os cenários independentes,
        # usar np.cumsum(..., axis=0) manda o computador acumular os retornos no tempo dentro do mesmo cenário, 
        # sem misturar o dinheiro do Cenário 1 com o do Cenário 2.
        
        return paths