from bond import Bond
from dcf import CashFlowPricer
from fx import FXForward

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

# ==========================================
# TESTE 3: CÂMBIO (FX FORWARD)
# ==========================================
print(FXForward.descricao)
# Spot USD/BRL a 5.00, Selic a 10.5%, Fed Funds a 5%, prazo de 1 ano
contrato_fx = FXForward(spot_rate=5.00, domestic_rate=0.105, foreign_rate=0.05, years=1.0)
taxa_futura = contrato_fx.calculate_forward_rate()
print(f"[>] RESULTADO: O câmbio a termo de 1 ano é R$ {taxa_futura:.4f}\n")