# NLW Journey 🚀 Planejador de Viagens
Este é um repositório dedicado ao evento NLW Journey da Rocketseat. Decidi seguir a Trilha **Inteligência Artificial** para fazer um Planejador de Viagens.

![wallpaper](/assets/wallpaper.png)

## 🛠️ Ferramentas e Objetivos
Durante o evento, iremos utilizar conceitos e ferramentas de IA Generativa, consulta na Internet, LLM (*Large Language Models*), Python e suas *Libs* (OpenAI e LangChain). 

O **objetivo** é formar um agente planejador de viagens, o qual há um usuário realizando um *request* (query + instructions), que passa pela *Lib* do LangChain (utilizando DuckDuckGo e Wikipedia para consultas) e o GPT no modelo LLM responde ao solicitado pelo usuário. 

Para aumentar o campo de pesquisa do Chat, iremos fazer o método **RAG**, consultando um site de dicas de viagem. Para isso, pegamos o conteúdo do site, transformarmos em *embedding model* e salvamos em um banco vetorial, conseguindo acessar o conteúdo do site via LangChain.

Além disso, também utilizamos o **Agente Supervisor** do GPT. Com ele podemos aplicar diretrizes específicas, com regras e comandos que aquele Agente vai executar da melhor forma esperada. 

Para integrar a conexão da aplicação com a estrutura do agente é necessário utilizarmos um **container**, como o **Docker**. Com ele, criamos uma imagem dentro de um arquivo que podemos virtualizar tudo que é preciso para o código rodar. Nesse caso, levaremos ao **AWS Cloud** que utiliza *Lambda Function* com *ECR Registry*. 

No AWS temos diversas funções, começando pelo **Elastic Container Registry**, onde criamos um repositório que terá nossa imagem. Além do ECR, utilizamos o **Command Line Interface**, para gerenciar nossos serviços. Utilizamos também o **Lambda**, com ele podemos executar um código sem gerenciar um servidor, pois é um serviço de computador *serveless*. Por fim, criamos um *load balance* pelo **EC2**, para criar uma API exposta do nosso código e colocar nosso agente na internet. 

Para finalizar e utilizar o agente há diversas formas. Eu optei pelo **Postman**. Nele, colocamos nosso http da nossa API, configuramos e fazemos uma *question*. Ao enviar, recebemos a resposta conforme a pesquisa da nossa OpenAI. 

![exemplo](/assets/exemplo.png)