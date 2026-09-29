from models.stochastic.gbm import GeometricBrownianMotion
from models.stochastic.monte_carlo import MonteCarloEngine

def validar_teste(nome, condicao):
    if condicao:
        print(f"[OK] {nome}")
    else:
        print(f"[FALHA] {nome}")

print("\n========================================")
print("--- Testes do Motor Estocástico ---")

# Teste 1: Validação Estrutural da Matriz (Shape)
gbm = GeometricBrownianMotion(mu=0.05, sigma=0.2)
paths = gbm.simulate_paths(S0=100, T=1.0, dt=1/252, num_paths=100)
# 1 ano de 252 dias úteis deve gerar 253 linhas (incluindo o dia 0) e 100 colunas
validar_teste("1. Matriz de caminhos gerada com dimensões corretas (253, 100)", paths.shape == (253, 100))
validar_teste("2. Preço inicial (S0) respeitado na primeira linha", paths[0, 0] == 100.0)

# Teste 2: Precificação Lógica de uma Call Europeia
engine = MonteCarloEngine(num_paths=10000, dt=1/252)
# Opção de compra no dinheiro (Strike = Preço Atual)
call_price = engine.price_european_call(model=gbm, S0=100, K=100, T=1.0, r=0.05)
# O preço da Call deve ser maior que zero, mas não pode custar mais que a própria ação
validar_teste(f"3. Preço da Call lógico (>0 e <100) -> Calculado: R$ {call_price:.2f}", 0 < call_price < 100)

print("========================================\n")