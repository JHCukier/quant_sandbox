from bond import Bond
from dcf import CashFlowPricer
from fx import FXForward
from swap import InterestRateSwap

def validar_teste(nome_teste, valor_calculado, valor_esperado, tolerancia=0.01):
    """Função auxiliar para comparar o resultado do código com o gabarito matemático."""
    sucesso = abs(valor_calculado - valor_esperado) <= tolerancia
    status = "[OK]" if sucesso else "[FALHA]"
    print(f"{status} {nome_teste}")
    if not sucesso:
        print(f"    -> Esperado: {valor_esperado:.4f} | Calculado: {valor_calculado:.4f}")

print("========================================")
print(" SUÍTE DE TESTES UNITÁRIOS - BLOCO 1")
print("========================================\n")

# --- TESTES: BOND ---
print("--- Testando Módulo Bond ---")
# Cenário 1: Cupom igual ao desconto (Preço = Valor de Face)
b1 = Bond(face_value=1000, coupon_rate=0.05, maturity_years=10)
validar_teste("1. Bond ao Par", b1.calculate_price(0.05), 1000.00)

# Cenário 2: Cupom maior que o desconto (Negociado com Prêmio)
b2 = Bond(face_value=1000, coupon_rate=0.08, maturity_years=5)
validar_teste("2. Bond com Prêmio", b2.calculate_price(0.05), 1129.88)

# Cenário 3: Zero-Coupon (Negociado com Desconto profundo)
b3 = Bond(face_value=1000, coupon_rate=0.0, maturity_years=10)
validar_teste("3. Bond Zero-Coupon", b3.calculate_price(0.10), 385.54)


# --- TESTES: DCF ---
print("\n--- Testando Módulo DCF ---")
# Cenário 1: Fluxos constantes
dcf1 = CashFlowPricer(discount_rate=0.10)
validar_teste("1. Fluxos Constantes", dcf1.calculate_npv([100, 100, 100]), 248.68)

# Cenário 2: Queima de caixa inicial e crescimento forte (Startup)
dcf2 = CashFlowPricer(discount_rate=0.15)
validar_teste("2. Curva de Startup", dcf2.calculate_npv([-500, 200, 600, 1000]), 682.71)

# Cenário 3: Taxa de desconto zero (Soma simples do caixa)
dcf3 = CashFlowPricer(discount_rate=0.0)
validar_teste("3. Taxa Zero", dcf3.calculate_npv([10, 20, 30]), 60.00)


# --- TESTES: FX FORWARD ---
print("\n--- Testando Módulo FX Forward ---")
# Cenário 1: Juro doméstico maior (Moeda local desvaloriza no termo)
fx1 = FXForward(spot_rate=5.00, domestic_rate=0.105, foreign_rate=0.05, years=1)
validar_teste("1. Risco Doméstico (BR>US)", fx1.calculate_forward_rate(), 5.2619)

# Cenário 2: Juros iguais (Termo igual ao Spot)
fx2 = FXForward(spot_rate=5.00, domestic_rate=0.05, foreign_rate=0.05, years=2)
validar_teste("2. Paridade Perfeita", fx2.calculate_forward_rate(), 5.0000)

# Cenário 3: Juro estrangeiro maior (Moeda local valoriza no termo)
fx3 = FXForward(spot_rate=5.00, domestic_rate=0.02, foreign_rate=0.08, years=1)
validar_teste("3. Juro Externo Maior", fx3.calculate_forward_rate(), 4.7222)


# --- TESTES: INTEREST RATE SWAP ---
print("\n--- Testando Módulo Swap (Recebendo Fixo) ---")
# Cenário 1: Expectativa de flutuante igual à taxa fixa
s1 = InterestRateSwap(notional=1_000_000, fixed_rate=0.08, discount_rate=0.08)
validar_teste("1. Swap Justo (Zero)", s1.calculate_value([0.08, 0.08, 0.08]), 0.00)

# Cenário 2: Taxas flutuantes despencam (Recebedor do Fixo tem lucro massivo)
s2 = InterestRateSwap(notional=1_000_000, fixed_rate=0.10, discount_rate=0.05)
validar_teste("2. In The Money (Lucro)", s2.calculate_value([0.04, 0.04, 0.04]), 163394.88)

# Cenário 3: Taxas flutuantes disparam (Recebedor do Fixo tem prejuízo)
s3 = InterestRateSwap(notional=1_000_000, fixed_rate=0.05, discount_rate=0.10)
validar_teste("3. Out of The Money (Prejuízo)", s3.calculate_value([0.12, 0.15]), -146281.00)

print("\n========================================")