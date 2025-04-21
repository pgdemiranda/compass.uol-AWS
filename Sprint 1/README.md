# Resumo da Sprint 1

A Sprint 1 foi dividida em duas semanas. A primeira semana esteve relacionado aos temas de Scrum, Segurança da Informação, Git e Markdown; a segunda semana esteve relacionado essencialmente a SQL e ao desafio envolvendo modelagem relacional e dimensional.

Do conteúdo da primeira semana, o que foi aprendido pode ser resumido em:

- **Scrum**: conceitos elementares de Scrum enquanto *framework* ágil, os diferentes papéis, o entendimento de eventos, incluindo a ideia de **Sprint**, **Daily** e **Retrospective**, e o foco na colaboração e entrega rápida.

- **Fundamentos da Segurança da Informação**: foram mostrado conceitos de segurança da informação, classificação da informação, tipos de engenharia social (e de como se proteger delas), diretrizes da segurança da informação, no sentido de como praticá-la no dia a dia, e elementos da segurança em relação a IA generativa.

- **Git**: foi apresentado elementos de versionamento, comandos essenciais para o fluxo de versionamento local (e remoto também), noções de merge e branches e o estudo finalizou com uma exploração de elementos na página do GitHub.

- **Markdown**: foi disponibilizado material básico sobre a sintaxe utilizada para formular esse próprio arquivo readme.

Na segunda semana foi aprendido:

- **Sql**: os elementos básicos para realizar uma query, os operadores aritméticos, lógicos e de comparação, funções agregadas, joins (utilizando especialmente **LEFT** e **INNER** joins nos exercícios), as diferenças entre **UNION** e **UNION ALL**, subqueries (o foco foi em **Common Table Expressions**), além de tratamento de dados e manipulação de tabelas.

- **Modelagem Relacional e Dimensional:** como esse foi o tema do Desafio, houve um foco em explicar o planejamento e os tipos de modelagem de banco de dados. Em relação a Modelagem Relacional, foi discutido a nomeclatura, a ideia de entidade, relacionamento e os tipos de modelos relacionais. Sobre a Modelagem Dimensional foi discutido o que é granularidade dos dados, as dimensões, as tabelas fato, o que são os cubos de dados, e a noção e os usos de cubos OLAP, especialmente em relação aos OLTP.

> Pessoalmente nenhum desses cursos e conceitos me eram estranhos: já tenho experiência profissional no uso de Git e SQL, uso Markdown em diferentes projetos no meu repositório do GitHub, e as noções de Modelagem, bem como de Segurança da Informação, foram vistos e revistos na minha graduação em Ciência de Dados, além da pós que frequento em Eng. e Ciência de Dados. **Dito isto, o conteúdo desses cursos é sempre interessante de ser revisto, pois é sempre possível aprender e exercitar algo novo.**

# Sumário
- [Desafio](#desafio)
- [Exercícios](#exercícios)
  - [Exercícios I - Biblioteca](#exercícios-i---biblioteca)
  - [Exercícios I - Loja](#exercícios-i---loja)
  - [Exercícios II - Extração de Dados](#exercícios-ii---extração-de-dados)
- [Evidências](#evidências)
  - [Exercícios I - Biblioteca](#exercícios-i---biblioteca-1)
  - [Exercícios I - Loja](#exercícios-i---loja-1)
  - [Exercícios II - Extração de Dados](#exercícios-ii---extração-de-dados-1)
- [Certificados](#certificados)

# Desafio

# Exercícios
## Exercícios I - Biblioteca

1. Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas. Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.

[Resposta Ex.1](./Exercícios/exercícios%20I%20-%20biblioteca/ex1.sql)

2. Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente. Atenção às colunas esperadas no resultado final:  titulo, valor.

[Resposta Ex.2](./Exercícios/exercícios%20I%20-%20biblioteca/ex2.sql)

3. Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

[Resposta Ex.3](./Exercícios/exercícios%20I%20-%20biblioteca/ex3.sql)

4. Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

[Resposta Ex.4](./Exercícios/exercícios%20I%20-%20biblioteca/ex4.sql)

5. Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

[Resposta Ex.5](./Exercícios/exercícios%20I%20-%20biblioteca/ex5.sql)

6. Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

[Resposta Ex.6](./Exercícios/exercícios%20I%20-%20biblioteca/ex6.sql)

7. Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

[Resposta Ex.7](./Exercícios/exercícios%20I%20-%20biblioteca/ex7.sql)

## Exercícios I - Loja
8. Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

[Resposta Ex.8](./Exercícios/exercícios%20I%20-%20loja/ex8.sql)

9. Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

[Resposta Ex.9](./Exercícios/exercícios%20I%20-%20loja/ex9.sql)

10. A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído. As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

[Resposta Ex.10](./Exercícios/exercícios%20I%20-%20loja/ex10.sql)

11. Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

[Resposta Ex.11](./Exercícios/exercícios%20I%20-%20loja/ex11.sql)

12. Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas. Observação: Apenas vendas com status concluído.

[Resposta Ex.12](./Exercícios/exercícios%20I%20-%20loja/ex12.sql)

13. Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas). As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

[Resposta Ex.13](./Exercícios/exercícios%20I%20-%20loja/ex13.sql)

14. Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente. Observação: Apenas vendas com status concluído.

[Resposta Ex.14](./Exercícios/exercícios%20I%20-%20loja/ex14.sql)

15. Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

[Resposta Ex.15](./Exercícios/exercícios%20I%20-%20loja/ex15.sql)

16. Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º). Obs: Somente vendas concluídas.

[Resposta Ex.16](./Exercícios/exercícios%20I%20-%20loja/ex16.sql)

## Exercícios II - Extração de Dados
1. Exportar o resultado da query que obtém os 10 livros mais caros para um arquivo CSV. Utilizar o caractere ";" (ponto e vírgula) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nomes de cabeçalho que listamos abaixo: CodLivro Titulo CodAutor NomeAutor Valor CodEditora NomeEditora 

[Arquivo CSV da Etapa 1](./Exercícios/exercícios%20II%20-%20extração%20de%20dados/etapa1.csv)

2. Exportar o resultado da query que obtém as 5 editoras com maior quantidade de livros na biblioteca para um arquivo CSV. Utilizar o caractere "|" (pipe) como separador. Lembre-se que o conteúdo do seu arquivo deverá respeitar a sequência de colunas e seus respectivos nome de cabeçalho que listamos abaixo: CodEditora NometEditora QuantidadeLivros

[Arquivo CSV da Etapa 2](./Exercícios/exercícios%20II%20-%20extração%20de%20dados/etapa2.csv)

# Evidências
## Exercícios I - Biblioteca
1. Ao realizar a query do exercício 1, podemos observar que foi retornado com sucesso a lista e todos os livros publicados após 2014 ordenados em ordem crescente pela coluna cod e com todas as colunas esperadas:
![Evidência exercício 1](./Exercícios/exercícios%20I%20-%20biblioteca/evidências/exercicio01.png)

2. A consulta do exercício 2 retornou com sucesso a lista dos 10 livros mais caros (feito com o uso da cláusula LIMIT), ordenados de modo decrescente pela coluna valor e com as colunas esperadas:
![Evidência exercício 2](./Exercícios/exercícios%20I%20-%20biblioteca/evidências/exercicio02.png)

3. A query do exercício 3 retorna com sucesso as editoras com mais livros na biblioteca, para isso foi utilizado a função agregadora COUNT com a cláusula GROUP BY. Apesar de ter sido limitada a 5 editoras, a consulta retorna com sucesso apenas 2, refletindo a ausência de outras editoras que atendam o parâmetro da query. O resultado foi ordenado pela quantidade de livros e retorna as colunas requisitadas:
![Evidência exercício 3](./Exercícios/exercícios%20I%20-%20biblioteca/evidências/exercicio03.png)

4. A consulta do exercício 4 retorna com sucesso a quantidade (feita com a função agregadora COUNT) de livros publicado por cada autor, ordenado pelo nome dos autores em ordem crescente e com as colunas requisitadas, incluindo a quantidade de livros publicados por cada um deles, obtido com o LEFT JOIN entre as tabelas autor e livro:
![Evidência exercício 4](./Exercícios/exercícios%20I%20-%20biblioteca/evidências/exercicio04.png)

5. Ao executar a consulta do exercício 5, recebe-se a lista dos autores que publicaram livros através de editoras que não possuem endereço na região sul do Brasil (feita com uma filtragem nos estados do sul brasileiro), o resultado foi obtido com diferentes INNER joins entre três tabelas e está ordenado de forma crescente pela coluna nome e não há nomer repetidos no retorno (para isso foi utilizada a função DISTINCT:
![Evidência exercício 5](./Exercícios/exercícios%20I%20-%20biblioteca/evidências/exercicio05.png)

6. A query do exercício 6 retorna o autor com maior números de livros publicados, contendo as colunas codautor, nome e quantidade_publicacoes:
![Evidência exercício6](./Exercícios/exercícios%20I%20-%20biblioteca/evidências/exercicio06.png)

7. A consulta do exercício 7 retorna a lista dos autores com nenhum publicação, sendo apresentados em ordem crescente. **Esse foi o primeiro exercício que utilizei uma subquery**, e a sua utilização facilitou bastante a formulação da consulta:
![Evidência exercício 7](./Exercícios/exercícios%20I%20-%20biblioteca/evidências/exercicio07.png)


## Exercícios I - Loja
8. A query do exercício 8 lista o código e o nome do vendedor com o maior número de vendas concluídas, o resltado foi obtido com a ajuda de uma subquery:
![Evidência exercício 8](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio08.png)

9. Aqui, a consulta do exercício 9 retornou com sucesso o código e o nome do produto mais vendido entre as datas requeridas, obtido com a ajuda de uma subquery, a cláusula LIMIT 1 e ordenação decrescente da quantidade de vendas:
![Evidência exercício 9](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio09.png)

10. Essa consulta, a do exercício 10, retorna a comissão dos vendedores apresentadas de modo decrescente e arredondadas na segunda casa decimal. Foi uma consulta possível ao calcular a quantidade de vendas utilizando a função SUM para somar os valores da multiplicação dos valores unitários de cada venda pela quantidade, e a função ROUND para arredondar a soma desses valores multiplicados pelo percentual de comissão e divididos por 100 para obter a devida comissão:
![Evidência exercício 10](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio10.png)

11. A consulta do exercício 11 retorna os clientes com maior gasto na loja à partir das vendas concluídas somadas de cada cliente, obtidas na soma com a função SUM da multiplicação entre a quantidade e o valor unitário de cada produto:
![Evidência exercício 11](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio11.png)

12. A query do exercício 12 lista os dependentes do vendedor com menor valor total bruto em vendas, obtidos com um INNER join entre as tabelas de vendas e de dependentes:
![Evidência exercício 12](./Exercícios/exercícios%20I%20-%20loja/ex12.sql)

13. A consulta do exercício 13 listou os 10 produtos menos vendidos por E-Commerce ou por Matriz, resultado obtido com a ajuda da função SUM da coluna qtd e a filtragem pela coluna nmcanalvendas:
![Evidência exercício 13](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio13.png)

14. A query do exercício 14 lista o gasto médio de cada estado arredondado na segunda casa decimal utilizando a função ROUND e a função agregadora AVG para obtér a média da multiplicação da quantidade pelo valor unitário de cada produto na tabela vendas, ordenados por essa média de forma decrescente:
![Evidência exercício 14](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio14.png)

15. A consulta do exercício 15 foi obtida com uma filtragem simples na coluna deletado (que possui valores inteiros 0 para não e 1 para sim) da tabela vendas:
![Evidência exercício 15](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio15.png)

16. É possível observar, ao rodar a consulta do exercício 16, o resultado da média da quantidade vendida de cada produto agregado por estado do Brasil, com valores arredondados na quarta casa decimal, mais uma vez obtidos com a ajuda das funções ROUND e AVG da coluna qtd da tabela vendas, sendo ordenados por duas colunas (estado e nome do produto):
![Evidência exercício 16](./Exercícios/exercícios%20I%20-%20loja/evidências/exercicio16.png)

## Exercícios II - Extração de Dados
1. A query foi realizada renomeando as colunas com os *alias* requeridos no exercício e realizada da maneira abaixo: 

```sql
select
	l.cod as CodLivro,
	l.titulo as Titulo,
	a.codautor as CodAutor,
	a.nome as NomeAutor,
	l.valor as Valor,
	e.codeditora as CodEditora,
	e.nome as NomeEditora
from livro l
left join autor a on a.codautor = l.autor
left join editora e on e.codeditora = l.editora
order by l.valor desc
limit 10
```

Os dados foram exportados tendo como delimitador o ";" sendo possível observar na evidência abaixo que os dados ficaram organizados, já que o delimitador escolhido permmite a tabulação desejada evitando que a coluna **NomeAutor**, por exemplo, que têm dados separados por ",", permaneçam estruturados.

![Evidência Etapa 1](./Exercícios/exercícios%20II%20-%20extração%20de%20dados/evidências/etapa1.png)


2. Igualmente, a query foi realizada renomeando as colunas com os *alias* requeridos no exercício e realizada da maneira abaixo:

```sql
select
	ed.codeditora as CodEditora,
	ed.nome as NometEditora,
	count(l.cod) as QuantidadeLivros
from editora ed
inner join livro l on ed.codEditora = l.editora
inner join endereco en on ed.endereco = en.codendereco
group by
	ed.nome,
	en.estado,
	en.cidade
order by QuantidadeLivros desc
limit 5
```
Os dados foram exportados tendo como delimitador o pipe "|". Da mesma maneira, todos os dados ficaram tabulados como desejados como pode ser observado na evidência abaixo:

![Evidência Etapa 2](./Exercícios/exercícios%20II%20-%20extração%20de%20dados/evidências/etapa2.png)

# Certificados
Não foi necessário apresentar nenhum certificado já que nessa Sprint não houve nenhum curso fora da Udemy.