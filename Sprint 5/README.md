# Resumo da Sprint 5

A *Sprint* 5 foi dividida em duas semanas, onde na primeira semana realizamos um curso de **Apache Spark** (especificamente de **PySpark**) e em seguida estudamos fundamentos de operações analíticas na AWS através dos cursos **Fundamentals of Analytics on AWS - part 1**, **Introduction to Amazon Athena** e **Serverless Analytics**; na segunda semana realizamos os exercícios e o desafio. As três atividades da AWS foram realizadas na plataforma [AWS Skill Builder](https://explore.skillbuilder.aws/learn) e as comprovações de nossa devida participação está na sessão de Certificados mais abaixo e no diretório [Certificados](./Certificados/). 

- **Fundamentals of Analytics on AWS - part 1**: o curso versou essencialmente sobre os desafios e serviços da AWS para os 5 "V"s do Big Data: Volume, Velocidade, Variedade, Veracidade e Valor. Para cada um desses "V", foram dados exemplos reais de como determinados serviços poderiam oferecer uma solução tangível, seus possíveis desdobramentos com o cliente e como essa solução poderia estar relacionado a outros desafios futuros.

- **Introduction to Amazon Athena**: neste curso fomos apresentados a operações básicas de importação de dados à partir do S3, criar bancos, tabelas e realizar queries no Amazon Athena.

- **Serverless Analytics**: Nos foi apresentada uma solução de ETL de *end-to-end* à partir do serviço AWS IoT.

> Os cursos da AWS foram úteis para aprendermos ainda mais como contornar os desafios a ser enfrentados nesse ecossistema, especialmente o curso Fundamentals of Analytics on AWS trouxe uma boa dose de reflexão sobre os serviços para Analytics. Com o aprendizado de Spark temos agora tudo que é necessário para enfrentar projetos com grandes volumes de dados. Não houve maiores dificuldades na resolução dos exercícios, mas aprendemos bastante sobre processo de otimização com o curso de Spark, e com o monitor, além de tudo, como otimizar dados em memória com alguns comandos úteis de Python.

# Sumário

- [Desafio](#desafio)
- [Exercícios](#exercícios)
    - [Exercício 1: Apache Spark - Contador de Palavras](#exercício-1-apache-spark---contador-de-palavras)
    - [Exercício 2: TMDB](#exercício-2-tmdb)
- [Evidências](#evidências)
- [Certificados](#certificados)

# Desafio

# Exercícios
> **REVISAR ISSO AQUI** <-

O Exercício 1 tem como objetivo desenvolver um job de processamento com o framework Spark por meio de um container Docker. Deve ser entregue o código desenvolvido. Para a sua resolução e execução aconteceu em 4 etapas: 1. realizar o *pull* da imagem jupyter/all-spark-notebook; 2. criar o container e ter acesso ao Jupyter Lab; 3. executar o pyspark à partir do contêiner; 4. usar o **Spark Shell** para contar a quantidade de ocorrências de cada palavra contida no arquivo README.md do nosso repositório no GitHub.

O Exercício 2 tem como objetivo criar um processo de extração de dados da API do TMDB utilizando serviços da AWS. O exercício foi separado em duas tarefas: 1. a criação da conta para a obtenção de uma chave para realizar solicitações à API; 2. fazer as requisições utilizando uma estrutura de URL fornecida para o exercício.

Os arquivos fornecidos para os exercícios, bem como as evidências que podem ser encontradas nas sub-pastas do diretório Exercícios. Abaixo fornecemos o caminho para cada exercício específico:

## [Exercício 1: Apache Spark - Contador de Palavras](./Exercícios/exercicio1-spark/)



## [Exercício 2: TMDB](./Exercícios/exercicio2-tmdb/)

# Evidências

# Certificados
Abaixo se encontram três certificados nominais a Pablo Miranda, todos relacionados aos cursos realizados na plataforma [AWS Skill Builder](https://explore.skillbuilder.aws/learn). Para essa *Sprint*, a conclusão dos cursos **Fundamentals of Analytics on AWS pt.1**, **Introduction to Amazon Athena** e **Serverless Analytics** resultaram no fornecimento dos certificados nominais: os certificados se encontram na pastda de [Certificados](./Certificados/) e podem ser acessado nos links abaixo: 

- [Fundamentals of Analytics on AWS pt.1](./Certificados/fundamentals_of_analytics_on_aws.pdf)

- [Introduction to Amazon Athena](./Certificados/introduction_to_amazon_athena.pdf)

- [Serverless Analytics](./Certificados/serverless_analytics.pdf)