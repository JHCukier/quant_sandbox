import numpy as np
from bond import Bond

# Criamos um título do Tesouro que custa 1000, paga 5% ao ano, com vencimento em 10 anos.
treasury_bond = Bond(face_value=1000, coupon_rate=0.05, maturity_years=10)

# O cenário muda: a Selic/Fed Funds sobe e o mercado agora exige 6% de rendimento (discount_rate).
preco_justo = treasury_bond.calculate_price(discount_rate=0.06)

print(f"O preço justo do Bond na tela do terminal é: US$ {preco_justo:.2f}")
# Resultado esperado: O preço cai para baixo de 1000, refletindo a gangorra da renda fixa.