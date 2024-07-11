# NLW Journey 🚀 Planejador de Viagens
Este é um repositório dedicado ao evento NLW Journey da Rocketseat. Decidi seguir a Trilha **Inteligência Artificial** para fazer um Planejador de Viagens.

![wallpaper](/assets/wallpaper.png)

## 🛠️ Ferramentas e Objetivos
Durante o evento, iremos utilizar conceitos e ferramentas de IA Generativa, consulta na Internet, LLM (Large Language Models), Python e suas Libs (OpenAI e LangChain). 

O **objetivo** é formar um agente planejador de viagens, o qual há um usuário realizando um request (query + instructions), que passam pela Lib do LangChain (utilizando DuckDuckGo e Wikipedia para consultas) e o GPT no modelo LLM responde ao solicitado pelo usuário. 

Para aumentar o campo de pesquisa do Chat, iremos fazer o método **RAG**, consultando um site de dicas de viagem. Para isso, pegamos o conteúdo do site, transformarmos em embedding model e salvamos em um banco vetorial, conseguindo acessar o conteúdo do site via LangChain.

Além disso, também utilizamos o **Agente Supervisor** do GPT. Com ele podemos aplicar diretrizes específicas, com regras e comandos que aquele Agente vai executar da melhor forma esperada. 