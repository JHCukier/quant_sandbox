import numpy as np

class Bond:
# Atributo de classe: pertence ao conceito, não precisa ser instanciado
    descricao = """
    === TÍTULOS DE RENDA FIXA (BONDS) ===
    O meu aprendizado: O Bond é um título de dívida com cupons periódicos.
    Se as taxas de juros sobem, o valor presente do título cai, pois ele pagará
    juros pré-fixados menores q o mercado.

    Matemática:
             T
    Preço =  Σ  [ C / (1 + r)^t ]  +  [ F / (1 + r)^T ]
            t=1

    Onde:
    C = Pagamento do Cupom (Valor de Face * Taxa do Cupom)
    F = Valor de Face (Principal devolvido no vencimento)
    r = Taxa de desconto exigida pelo mercado
    T = Prazo até o vencimento (Maturity)
    """

    # O Construtor: define o estado inicial do objeto financeiro
    def __init__(self, face_value: float, coupon_rate: float, maturity_years: int):
        # O 'self.' acopla os parâmetros passados às variáveis internas da instância
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.maturity_years = maturity_years

    def calculate_price(self, discount_rate: float) -> float:
        """
        Calcula o Valor Presente (Preço Justo) do Bond usando a taxa de mercado atual.
        """
        # 1. Valor monetário que o título paga periodicamente
        coupon_payment = self.face_value * self.coupon_rate
        
        # 2. Vetorização de tempo: cria um array [1, 2, 3, ..., maturity_years]
        # OTIMIZAÇÃO: Utiliza vetorização do NumPy em vez de loops 'for' nativos. 
        # Isso desloca o processamento para código compilado em C, garantindo 
        # escalabilidade e baixa latência ao calcular milhares de títulos simultaneamente.
        periods = np.arange(1, self.maturity_years + 1)
        
        # 3. Matemática matricial: desconta todos os cupons de uma única vez
        discount_factors = 1 / ((1 + discount_rate) ** periods)
        present_value_coupons = np.sum(coupon_payment * discount_factors)
        
        # 4. Desconta a devolução do dinheiro principal no último ano
        present_value_face = self.face_value / ((1 + discount_rate) ** self.maturity_years)
        
        # 5. O preço final é a soma dos fluxos
        return present_value_coupons + present_value_face