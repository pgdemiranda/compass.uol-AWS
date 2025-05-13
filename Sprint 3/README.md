# Resumo da Sprint 3

Como de costume, a Sprint 3 foi dividida em duas semanas, onde na primeira semana exploramos tópicos relacionados a Contêiner com a ferramenta Docker, aliado a orquestração com Docker Swarm e Kubernetes, além de Expressões Regulares (*Regex*) e serviços essenciais da AWS - Amazon Web Services.

- **Docker**:

- **Expressões Regulares**

- **AWS**: 

# Sumário

- [Desafio](#desafio)
- [Exercícios](#exercícios)
- [Evidências](#evidências)
- [Certificados](#certificados)

# Desafio

O README.md, bem como os arquivos pertinentes ao Desafio se encontram na pasta [Desafio](./Desafio/)

Todas as evidências do desafio se encontra na própria pasta de [Evidências](./Evidências/)

# Exercícios

O objetivo dos exercícios é praticar Python com Contêineres Docker, sendo necessária a entrega de arquivos **Dockerfile** e scripts no formato **.py**, além das evidências da execução bem sucedida.

Todos os arquivos dos exercícios, bem como as evidências podem ser encontrados na pasta [Exercícios](./Exercícios/), abaixo fornecemos o caminho para cada etapa específica: 

- [Etapa 1](./Exercícios/etapa-1/)

- [Etapa 2](./Exercícios/etapa-2/)

## Etapa 1

- Entregável:
    - [Dockerfile da Etapa 1](./Exercícios/etapa-1/Dockerfile)

- Comandos utilizados:
    - `docker build -t carguru .`
    - `docker run carguru`

## Etapa 2

- Entregáveis:
    - [Script em Python](./Exercícios/etapa-2/app.py)
    - [Dockerfile da Etapa 2](./Exercícios/etapa-2/Dockerfile)

- Comandos utilizados:
    - `docker build -t mascarar-dados .`
    - `docker run -it mascarar-dados`

# Evidências

## Etapa I

1. A primeira etapa foi selecionar a imagem adequada para rodar no contêiner já que várias imagens são disponibilizadas no DockerHub - https://hub.docker.com/_/python e as nossas considerações foram as seguintes:
- Decidimos escolher **a última atualização da penúltima versão do Python** para minimizarmos possíveis problemas de compatibilidade, já que a versão atual ainda está recebendo atualizações. 
- Entre as diferentes tags (**alpine**, **slim**, **bookworm**, **bullseye** e **windows server core**) a própria documentação do site oferece algumas orientações em relação a *single* e *share* *tags*, além do que exatamente são essas tags (em relação a tamanho e distribuições). Selecionamos a tag **alpine** pertencente ao *Alpine Linux project* por ser a imagem mais leve e na qual podemos adicionar o que for necessário no Dockerfile. Adicionalmente, a imagem com a tag **alpine não apresentou nenhuma vulnerabilidade**.
- O código escrito no Dockerfile foi o seguinte:

```Dockerfile
FROM python:3.13.3-alpine

WORKDIR /app

COPY carguru.py /app/carguru.py

CMD ["python3", "carguru.py"]
```

No diretório [etapa-1](./Exercícios/etapa-1/) além do Dockerfile se encontra o script [carguru](./Exercícios/etapa-1/carguru.py) que foi entregue para esse exercício. Com o comando `FROM python:3.13.3-alpine` indicamos a imagem base que vai ser usada na construção do contêiner, definimos o diretório /app como o diretório de trabalho com `WORKDIR /app` que é onde vamos rodar nosso comando para rodar o script carguru, mas antes vamos copiá-lo do diretório base para o diretório /app com o comando `COPY carguru.py /app/carguru.py` e daí rodá-lo com `CMD ["python3", "carguru.py"]` que executa o script dentro do contêiner.

Abaixo o tamanho da imagem no python3.13.3-alpine
![alpine](./Exercícios/etapa-1/evidencias/amostra-1_alpine.png)

Em relação ao tamanho da imagem no python3.13.3-slim
![slim](./Exercícios/etapa-1/evidencias/amostra-2_slim.png)


> ATENÇÃO, REFAZER ESSA PARTE DAS AMOSTRAS COM IMAGENS RODADAS AMANHÃ NO HORÁRIO DA BOLSA!

2. A amostra à seguir demonstra que o contêiner foi construído com sucesso utilizando o comando `docker build -t carguru .`, onde construímos o contêiner com **docker build**, atribuímos a tag etapa-1 com o comando **-t carguru** e assinalamos que a construção deve ser feita no diretório atual com **.**; e em seguida foi rodado com sucesso com o comando `docker run etapa-1`. onde rodamos o contêiner do qual foi atribuído a tag **carguru**:
-> quebrado ![construido e rodando](./Exercícios/etapa-1/evidencias/amostra-3_build.png)

3. Como toda vez que o código for acionado, ele deve trazer o nome de um carro diferente, rodamos o script dentro do contêiner várias vezes para nos certificarmos que era esse o caso e que ele roda sem complicações:
-> quebrado ![rodando](./Exercícios/etapa-1/evidencias/amostra-4_run.png)

## Etapa II


```Dockerfile
FROM python:3.13.3-alpine

WORKDIR /app

COPY mascarar-dados.py /app/mascarar-dados.py

CMD ["python3", "mascarar-dados.py"]
```

https://docs.python.org/3/library/hashlib.html

https://docs.python.org/3/library/hashlib.html#hashlib.sha1

https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest

# Certificados