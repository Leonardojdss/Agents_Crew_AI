import pandas as pd
from crewai_tools import BaseTool

class coleta_de_dados_transacionais(BaseTool):
    name: str = "coleta de dados transacionais"
    description: str = "Está ferramenta realiza a coleta do ultimo arquivo de dados transacionais do banco."
    
    def _run(self, argument: str) -> str:
        # dados do CSV
        data_int = "data/input/transacoes_banco_outubro_2024.csv"
        data = pd.read_csv(data_int)
        df = pd.DataFrame(data)

        # obter estatisticas descritivas dos dados
        media_transacao = df['Valores Transacionados (R$)'].mean()
        maior_transacao = df.loc[df['Valores Transacionados (R$)'].idxmax()]
        menor_transacao = df.loc[df['Valores Transacionados (R$)'].idxmin()]

        # Formatar o resultado
        resultado = (
            f"Média de transações em R$: {media_transacao}\n"
            f"Máximo valor transacionado em R$: {maior_transacao}\n"
            f"Mínimo valor transacionado em R$: {menor_transacao}\n"
        )

        return resultado
