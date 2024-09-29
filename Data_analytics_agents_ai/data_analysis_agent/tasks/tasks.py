# tasks.py
from crewai import Task
from data_analysis_agent.agents.agents import Analista_de_engenharia_de_dados, analista_de_dados, Revisor_de_email

coleta_de_dados = Task(
        description=("1. Coletar o ultimo arquivo de dados transacionais do banco,\
                     utilizando a ferramenta coleta_de_dados_transacionais."),
        expected_output=("É esperado que o agente de engenharia de dados colete o arquivo CSV de dados transacionais e compartilhe com o analista de dados todos os dados"),
        agent=Analista_de_engenharia_de_dados
    )

analise_dos_dados = Task(
        description=("Realizar a análise do último arquivo de dados transacionais do banco"),
        expected_output=("1. Através das estatisticas descritivas realizar uma analise dos dados transacionais do banco e obter insigts para o compartilhar com a gerencia."),
        agent=analista_de_dados,
        context=[coleta_de_dados]
    )

criacao_de_email = Task(
        description=("1. A partir dos dados estatísticos, criar um email para o gerente sênior do banco."),	
        expected_output=("É esperado que o agente de revisor e criador de emails crie \
                         um email com os dados estatísticos para o gerente sênior do banco."),
        agent=Revisor_de_email,
        context=[analise_dos_dados]
    )
