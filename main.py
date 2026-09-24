from bond import Bond
from dcf import CashFlowPricer

# ==========================================
# TESTE ESTÁTICO 1: TÍTULO DE RENDA FIXA
# ==========================================
print(Bond.descricao)
treasury_bond = Bond(face_value=1000, coupon_rate=0.05, maturity_years=10)
preco_bond = treasury_bond.calculate_price(discount_rate=0.06)
print(f"[>] Preço do Bond: US$ {preco_bond:.2f}\n")

# ==========================================
# TESTE ESTÁTICO 2: DCF GENÉRICO
# ==========================================
print(CashFlowPricer.descricao)
# Instancia a calculadora com uma taxa de desconto de 10%
pricer = CashFlowPricer(discount_rate=0.10)

# Simula uma empresa que lucra 100, 150 e 200 nos próximos 3 anos
fluxos_projetados = [100.0, 150.0, 200.0]

valor_presente = pricer.calculate_npv(fluxos_projetados)
print(f"[>] Valor Presente Líquido (DCF): US$ {valor_presente:.2f}")