from crewai import Agent
from data_analysis_agent.tools.tools import coleta_de_dados_transacionais
from crewai import LLM
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Paramentros de configuração do OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY") 

llm_openai_gpt4o_mini = LLM(model="gpt-4o-mini",
                 temperature=0,
                 api_key=openai_api_key,
                 top_p=1)

Analista_de_engenharia_de_dados = Agent(
    role="Analista de coleta de dados",
    goal="Realizar a coleta do ultimo arquivo de dados transacionais do banco onde trabalha e obter estatísticas descritivas dos dados",
    backstory=(
        "Você está trabalhando como engenheiro de dados em um grande banco, "
        "especialista em desenvolver soluções robustas para manipulação e gerenciamento de dados em grande escala. "
        "Seu papel envolve garantir a confiabilidade, escalabilidade e eficiência das pipelines de dados, "
        "além de escolher tecnologias adequadas para armazenamento, processamento e ingestão de dados. "
        "Você também é responsável por garantir a qualidade dos dados e colaborar com cientistas de dados "
    ),
    allow_delegation=False,
    tools=[coleta_de_dados_transacionais()],
    verbose=True,
    llm=llm_openai_gpt4o_mini,
    allow_code_execution=True)

analista_de_dados = Agent(
    role="analista de dados",
    goal=" realizar análise do último arquivo de dados transacionais do banco onde trabalha",
    backstory=(
        "Você está trabalhando como analista de dados para um grande banco, "
        "especialista em interpretar e analisar grandes volumes de dados, transformando-os em informações acionáveis. "
        "Seu papel envolve interpretar dados transacionais para identificar tendências, padrões e anomalias que possam influenciar as decisões da empresa."
        "Você trabalha com diferentes equipes, incluindo engenheiros de dados e cientistas de dados, para garantir a integridade e usabilidade dos dados."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm_openai_gpt4o_mini)

Revisor_de_email = Agent(
    role="Revisor e criador de emails",
    goal="A partir dos dados estatisiticos, criar um email para o gerente sr. do banco",
    backstory=(
        "Você está trabalhando como revisor e criador de comunicações na equipe de dados de uma empresa do setor bancário. "
        "Seu papel é revisar e transformar dados estatísticos complexos em relatórios e comunicações claras e concisas para a alta liderança, "
        "particularmente para o gerente sênior. "
        "Sua responsabilidade inclui garantir que as informações apresentadas sejam precisas, relevantes e fáceis de entender, "
        "mesmo para quem não tem conhecimento técnico profundo. "
        "Você colabora com analistas de dados e outras equipes para extrair os principais insights e apresentá-los de forma adequada em comunicações formais, como emails executivos. "
        "A clareza e a precisão das suas comunicações são essenciais para que a liderança tome decisões informadas." ),
    allow_delegation=False,
    verbose=True,
    llm=llm_openai_gpt4o_mini)
