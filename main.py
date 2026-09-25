from models.deterministic.bond import Bond
from models.deterministic.dcf import CashFlowPricer
from models.deterministic.fx import FXForward
from models.deterministic.swap import InterestRateSwap

def menu_deterministico():
    opcoes = {
        "1": Bond,
        "2": CashFlowPricer,
        "3": FXForward,
        "4": InterestRateSwap
    }

    while True:
        print("\n" + "="*40)
        print(" MODELOS DETERMINÍSTICOS (BLOCO 1)")
        print("="*40)
        print("1. Títulos de Renda Fixa (Bonds)")
        print("2. Desconto de Fluxos de Caixa (DCF)")
        print("3. Câmbio a Termo (FX Forward)")
        print("4. Swap de Taxa de Juros (IRS)")
        print("0. Voltar ao Menu Principal")
        print("="*40)
        
        escolha = input("Selecione o modelo: ")
        
        if escolha == "0":
            break
            
        if escolha in opcoes:
            classe_selecionada = opcoes[escolha]
            print(f"\n{classe_selecionada.descricao}")
            print("\n[Módulo instanciado com sucesso. Lógica de inputs interativos em construção...]")
            # No futuro, você pode criar métodos estáticos ou funções separadas para lidar com os inputs
            # de cada classe sem poluir este arquivo principal.
        else:
            print("Opção inválida. Tente novamente.")

def menu_principal():
    while True:
        print("\n" + "="*40)
        print(" QUANT SANDBOX - MENU PRINCIPAL")
        print("="*40)
        print("1. Modelos Determinísticos (Renda Fixa/FX)")
        print("2. Simulações Estocásticas (Monte Carlo) - [Em Breve]")
        print("0. Sair")
        print("="*40)
        
        escolha = input("Selecione a categoria: ")
        
        if escolha == "1":
            menu_deterministico()
        elif escolha == "2":
            print("\n[>] Módulo de Monte Carlo será implementado em breve.")
        elif escolha == "0":
            print("Encerrando a Sandbox. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_principal()