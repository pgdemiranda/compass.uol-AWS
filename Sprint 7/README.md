# Resumo da Sprint 7

A *Sprint* 7 foi dividida em duas semanas, onde na primeira semana realizamos dois cursos que forneceram treinamentos de modelagem e de produtividade com um serviço de LLM da AWS, e na segunda semana nos dedicamos exclusivamente ao desafio. Esses foram os cursos e uma breve descrição de seu conteúdo:

- **Modelagem de dados para Data Warehouse**: esse curso nos trouxe conhecimento básico em modelagem de dados no contexto de *Data Warehouses*, discutindo arquiteturas **OLTP** e **OLAP** e tabelas de dimensão e tabelas de fato, bem como de todos os elementos envolvidos para a formulação delas.

- **Amazon Q Developer for Programmers and DevOps AWS AI coding**: o curso forneceu o conhecimento técnico para utilizar, em favor de nossa produtividade, o serviço **AWS Q Developer** para a criação, refatoração e revisão de código e na sua documentação, além de assistência em etapas de CI/CD.

> Essa foi uma *Sprint* curta no sentido de material para os estudos, mas igualmente desafiadora em relação à aplicação prática dos nossos conhecimentos no Desafio, ou na entrega do Desafio dessa *Sprint*. Já havíamos feito parte da entrega na *Sprint* passada, a catalogação dos dados na camada **TRUSTED** para a posterior carga na camada **REFINED**, agora precisamos realizar a modelagem dos dados para essa nova camada com a finalidade de garantirmos consistência e qualidade para o posterior exame utilizando **AWS Quicksight**.

# Sumário

- [Desafio](#desafio)

- [Exercícios](#exercícios)

- [Evidências](#evidências)

- [Certificados](#certificados)

# Desafio

O Desafio dessa *Sprint* foi realizada em duas entregas: 

1. **Modelagem de Dados Camada Refined**. Aqui, a modelagem tem origem à partir da camada **TRUSTED**, e é estruturada à partir dos princípios da modelagem multidimensional, permitindo consultas sob diferentes perspectivas. Devem ser criadas no AWS Glue Data Catalog as tabelas e, se necessário, views, de acordo com a modelagem de dados solicitada. 

2. **Processamento Camada Refined**. Para essa entrega, deve ser criada a camada **REFINED**, transformada e armazenada conforme o nosso modelo. Essa entrega precisa ser feita com o Apache Spark com jobs que processe dados à partir da camada **TRUSTED**, que persista os dados em `.parquet` e particionados, se necessário.

O README.md, bem como os arquivos pertinentes ao Desafio se encontram no diretório [Desafio](./Desafio/).

Todas as evidências do desafio se encontra na própria pasta de [Evidências](./Evidências/).

# Exercícios

Não houve nenhum exercício durante esta *Sprint*.

# Evidências

Não houve exercícios, de modo que não foi necessário coletar nenhuma evidência.

# Certificados

Não houve cursos fora da plataforma *Udemy*.