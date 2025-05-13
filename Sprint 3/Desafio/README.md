# Desafio da Sprint 3 - Docker e Python

## Entregáveis

- [] dois arquivos no formato **.py** contendo o código usado para a execução de cada etapa correspondente do problema;

- [] dois arquivos **Dockerfile** contendo as resoluções de cada etapa correspondendo do problema;

- [] um arquivo **docker-compose.yaml** contendo a resolução do problema proposto;

- [] um arquivo **.csv** após o processo de limpeza;

- [] um arquivo **.txt** com as respostas dos questionamentos da etapa 5;

- [] duas imagens de gráficos geradas no formato png.

## Sumário

## Desafio 

O objetivo do desafio dessa sprint é a prática de Docker e Python combinando os conhecimentos que foram adquiridos no PB.

A preparação para o desafio envolveu o download do arquivo [concert_tours_by_women.csv](./etapa-1/concert_tours_by_women.csv) e a disponibilidade dos recursos envolvendo a containerização das soluções requisitadas. O desafio foi realizado em 5 etapas distintas:

Na **primeira etapa** foi requisitada a entrega de um script chamado **etl.py** que fará a limpeza dos dados do arquivo csv disponibilizado, resultando em um arquivo nomeado como **csv_limpo.csv** exatamente como na imagem abaixo:

![imagem_csv_limpo](./etapa-1/Sprint+3+-+Resultado+CSV.png)

Para a **segunda etapa** o script **job.py** deverá realizar o processamento dos dados e realizar uma série de perguntas:

1. Qual é a artista que mais aparece nessa lista e possui a maior média de seu faturamento bruto (Actual gross)?

2. Das turnês que aconteceram dentro de um ano, qual a turnê com a maior média de faturamento bruto (Average gross)

3. Quais são as 3 turnês que possuem o show (unitário) mais lucrativo? Cite também o nome de cada artista e o valor por show. Utilize a coluna "Adjusted gross (in 2022 dollars)". Caso necessário, crie uma coluna nova para essa conta.

4. Para a artista que mais aparece nessa lista, e que tenha o maior somatório de faturamento bruto, crie um gráfico de linhas que mostra o faturamento por ano da turnê (use a coluna Start Year). Apenas os anos com turnês.

5. Faça um gráfico de colunas demonstrando as 5 artistas com mais shows na lista.

Na **terceira etapa** vamos criar um arquivo **Dockerfile** para executar o script criado na etapa 1.

Para a **quarta etapa** vamos criar um arquivo **Dockerfile** para executar o script criado na etapa 2.

Finalmente, na **quinta etapa** vamos criar um arquivo **docker-compose** para conectar os dois contêineres e rodar a aplicação completa utilizando um volume em uma pasta local criada especificamente para isso, o nome do diretório deve ser **/volume**. A execução do desafio deve ser somente pelo **docker-compose**.

**ATENÇÂO**: a solução para as primeira e segunda etapa foram prototipadas em um **jupyter notebook**, que, apesar de não ser um entregável, também se encontra na pasta Desafio como [prototipagem.ipynb](prototipagem.ipynb).

# Etapa 1

# Etapa 2

# Etapa 3

# Etapa 4

# Etapa 5