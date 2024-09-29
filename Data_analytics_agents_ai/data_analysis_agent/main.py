from crewai import Crew
from data_analysis_agent.tasks.tasks import coleta_de_dados, analise_dos_dados, criacao_de_email
from data_analysis_agent.agents.agents import Analista_de_engenharia_de_dados, analista_de_dados, Revisor_de_email

crew = Crew(
    agents=[Analista_de_engenharia_de_dados, analista_de_dados, Revisor_de_email],
    tasks=[coleta_de_dados, analise_dos_dados, criacao_de_email],
    verbose=True,
    memory=True
)

start_agents = crew.kickoff()
