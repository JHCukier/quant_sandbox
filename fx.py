class FXForward:
    descricao = """
    === CONTRATO FUTURO DE CÂMBIO (FX FORWARD) ===
    O meu aprendizado: É a taxa de troca entre duas moedas.
    A variável mais importante aqui não é adivinhar notícias políticas,
    mas a Paridade da Taxa de Juros. O preço futuro de uma moeda é travado
    pela diferença de juros entre os dois países, senão haveria oportunidade de lucro sem risco (arbitragem).

    Matemática:
                  (1 + r_d)^t
    F = Spot * -----------------
                  (1 + r_f)^t

    Onde:
    F    = Preço Forward (Preço futuro no contrato)
    Spot = Preço de câmbio à vista (hoje)
    r_d  = Taxa de juros doméstica (ex: Selic no Brasil)
    r_f  = Taxa de juros estrangeira (ex: Fed Funds nos EUA)
    t    = Prazo em anos
    """

    def __init__(self, spot_rate: float, domestic_rate: float, foreign_rate: float, years: float):
        self.spot_rate = spot_rate
        self.domestic_rate = domestic_rate
        self.foreign_rate = foreign_rate
        self.years = years

    def calculate_forward_rate(self) -> float:
        """
        Calcula a taxa a termo (Forward) baseada na paridade de juros.
        """
        forward = self.spot_rate * ((1 + self.domestic_rate) ** self.years) / ((1 + self.foreign_rate) ** self.years)
        return float(forward)