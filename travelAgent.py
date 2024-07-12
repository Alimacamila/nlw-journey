import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

import json

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
import bs4

from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

llm = ChatOpenAI(model="gpt-3.5-turbo")

# Isolar os métodos em uma função para o Agente de Pesquisa
def reasearchAgent(query, llm):
    tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent (llm, tools, prompt) # Inicializar o agente
    agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt)
    webContext = agent_executor.invoke({"input": query})
    return webContext['output']

def loadData():
    loader = WebBaseLoader(
        web_paths= ("https://www.dicasdeviagem.com/inglaterra",),
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("pagetitleloading background-imaged loading-dark", "postcontentwrap"))),
    ) # Carregar a página e seu conteúdo
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200) # Recurso para separar em pedaços menores
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()
    return retriever

def getRelevantDocs(query):
    retriever = loadData()
    relevant_documents = retriever.invoke(query)
    return relevant_documents

# Montagem da resposta final do Prompt com os detalhes necessários 
def supervisorAgent(query, llm, webContext, relevant_documents):
    prompt_template = """"
    Você é um gerente de uma agência de viagens. Sua resposta final deverá ser um roteiro de viagem completo e detalhado. 
    Utilize o contexto de eventos e preços de passagens, o input do usuário e também os documentos relevantes para elaboração.
    Contexto: {webContext}
    Documentos relevantes: {relevant_documents}
    Usuário: {query}
    Assistente:
    """

    prompt = PromptTemplate(
        input_variables=['webContext', 'relevant_documents', 'query'],
        template= prompt_template
    )

    sequence = RunnableSequence(prompt | llm)
    response = sequence.invoke({"webContext": webContext, "relevant_documents": relevant_documents, "query": query})
    return response


def getResponse(query, llm):
    webContext = reasearchAgent(query, llm)
    relevant_documents = getRelevantDocs(query)
    response = supervisorAgent(query, llm, webContext, relevant_documents)
    return(response)

def lambda_handler(event, context):
    # query = event.get("question")
    body = json.loads(event.get('body', {}))
    query = body.get('question', 'Parametro question não fornecido')
    response = getResponse(query, llm).content
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "applications/json"
        },
        "body": json.dumps({
            "message": "Tarefa concluída com sucesso",
            "details": response,
        })
    }