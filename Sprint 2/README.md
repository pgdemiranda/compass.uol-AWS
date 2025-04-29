# Resumo da Sprint 2

A Sprint 2 foi dividida em duas semanas. A primeira semana esteve relacionado a um conteúdo extenso de Python; a segunda semana esteve relacionado essencialmente a realização dos exercícios e do desafio envolvendo análise de dados.

- **Python**:

- **Ciência de Dados**:

# Sumário

# Desafio

# Exercícios
Foram realizadas quatro bateria de exercícios e para cada uma delas estão disponibilizados os arquivos com a resolução dos arquivos no formato **.py**, além das evidências em formato **.png**. Excepcionalmente para a bateria de "ETL com Python" a resolução dos arquivos foi disponibilizada em um Jupyter Notebook no formato **.ipynb** e o output das questões armazenadas em arquivos **.txt** conforme requisitado.

- [Pasta para os exercícios de Python Básico](./Exercícios/basico/)

- [Pasta para os exercícios de Python Avançado I](./Exercícios/avancado_I/)

- [Pasta para os exercícios de Python Avançado II](./Exercícios/avancado_II/)

- [Pasta para os exercícios de ETL com Python](./Exercícios/etl/)

## Exercícios Python Básico
1. Resposta do exercício 1:
- [Exercício 1](./Exercícios/basico/ex1.py)

2. Resposta do exercício 2:
- [Exercício 2](./Exercícios/basico/ex2.py)

3. Resposta do exercício 3:
- [Exercício 3](./Exercícios/basico/ex3.py)

4. Resposta do exercício 4:
- [Exercício 4](./Exercícios/basico/ex4.py)

5. Resposta do exercício 5:
- [Exercício 5](./Exercícios/basico/ex5.py)

6. Resposta do exercício 6:
- [Exercício 6](./Exercícios/basico/ex6.py)

7. Resposta do exercício 7:
- [Exercício 7](./Exercícios/basico/ex7.py)

8. Resposta do exercício 8:
- [Exercício 8](./Exercícios/basico/ex8.py)

9. Resposta do exercício 9:
- [Exercício 9](./Exercícios/basico/ex9.py)

10. Resposta do exercício 10:
- [Exercício 10](./Exercícios/basico/ex10.py)

11. Resposta do exercício 11:
- [Exercício 11](./Exercícios/basico/ex11.py)

12. Resposta do exercício 12:
- [Exercício 12](./Exercícios/basico/ex12.py)

13. Resposta do exercício 13:
- [Exercício 13](./Exercícios/basico/ex13.py)

14. Resposta do exercício 14:
- [Exercício 14](./Exercícios/basico/ex14.py)

## Exercícios Python Avançado I
15. Resposta do exercício 15:
- [Exercício 15](./Exercícios/avancado_I/ex15.py)

16. Resposta do exercício 16:
- [Exercício 16](./Exercícios/avancado_I/ex16.py)

17. Resposta do exercício 17:
- [Exercício 17](./Exercícios/avancado_I/ex17.py)

18. Resposta do exercício 18:
- [Exercício 18](./Exercícios/avancado_I/ex18.py)

19. Resposta do exercício 19:
- [Exercício 19](./Exercícios/avancado_I/ex19.py)

## Exercícios Python Avançado II
20. Resposta do exercício 20:
- [Exercício 20](./Exercícios/avancado_II/ex20.py)

21. Resposta do exercício 21:
- [Exercício 21](./Exercícios/avancado_II/ex21.py)

22. Resposta do exercício 22:
- [Exercício 22](./Exercícios/avancado_II/ex22.py)

23. Resposta do exercício 23:
- [Exercício 23](./Exercícios/avancado_II/ex23.py)

24. Resposta do exercício 24:
- [Exercício 24](./Exercícios/avancado_II/ex24.py)

25. Resposta do exercício 25:
- [Exercício 25](./Exercícios/avancado_II/ex25.py)

26. Resposta do exercício 26:
- [Exercício 26](./Exercícios/avancado_II/ex26.py)

## Exercícios Python ETL
Jupyter notebook com as respostas das questões de ETL
- [ETL com Python](./Exercícios/etl/etl.ipynb)

1. Etapa-1:
[txt etapa-1](./Exercícios/etl/etapa-1.txt)

2. Etapa-2:
[txt etapa-2](./Exercícios/etl/etapa-2.txt)

3. Etapa-3:
[txt etapa-3](./Exercícios/etl/etapa-3.txt)

4. Etapa-4:
[txt etapa-4](./Exercícios/etl/etapa-4.txt)

5. Etapa-5:
[txt etapa-5](./Exercícios/etl/etapa-5.txt)

# Evidências
## Exercícios Python Básico
## Exercícios Python Avançado I
## Exercícios Python Avançado II

## Exercícios Python ETL
1. O enunciado da etapa 1 diz: "Apresente o ator/atriz com maior número de filmes e a respectiva quantidade. A quantidade de filmes encontra-se na coluna Number of movies do arquivo". O código desenvolvido abre e lê o arquivo **.csv** como uma lista de dicionário (gerando assim uma relação chave-valor), usa a função `max()` para retornar o valor máximo percorrido com uma função lambda na coluna 'Number of Movies'.

![input etapa 1](./Exercícios/etl/evidencias/etapa1-input.png)

O resultado é gravado no arquivo **etapa-1.txt** com a informação desejada das colunas 'Actor' e 'Number of Movies':

![output etapa 1](./Exercícios/etl/evidencias/etapa1-output.png)

2. O enunciado da etapa 2 pede: "Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os atores. Estamos falando aqui da média da coluna Gross". O código abaixo abre o arquivo, converte os dados em uma lista de dicionário, calcula-se a média dividindo a soma dos valores da coluna 'Gross' pelo número de elementos da lista.

![input etapa 2](./Exercícios/etl/evidencias/etapa2-input.png)

O resultado foi então registrado no arquivo **etapa-2.txt** com a média bruta das bilheterias e formatado para apresentar o resultado com duas casas decimais:

![output etapa 2](./Exercícios/etl/evidencias/etapa2-output.png)

3. O enunciado da etapa 3 é a seguinte: "Apresenta o ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados. Considere a coluna Average per Movie para fins de cálculo". O código lê o arquivo e o converte em uma lista de dicionário e com a ajuda de uma função lambda e da função `max()`, retorna o valor máximo da coluna 'Average per Movie'.

![input etapa 3](./Exercícios/etl/evidencias/etapa3-input.png)

O resultado foi registrado no arquivo **etapa-3.txt** trazendo o nome do ator com o maior valor médio por filme:

![output etapa 3](./Exercícios/etl/evidencias/etapa3-output.png)

4. Para a etapa 4 é requisitado: "A coluna #1 Movie contém o filme de maior bilheteriea em que o autor atuou. Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela quantidade de vezes em que estão presentes. Considere a ordem decrescente e, em segundo nível, o nome do filme. 

Ao escrever no arquivo, considere o padrão de saída (sequencia) - O filme (nome filme) aparece (quantidade) vez(es) no dataset, adicionando um resultado a cada linha". O código escrito é um pouco mais complexo: ele começa com um dicionário vazio, percorre a lista de filmes adicionando os filmes a essa lista, e se o filme já está lá, o contador é incrementado em um para cada vez que ele aparece de novo na iteração.

![input etapa 4](./Exercícios/etl/evidencias/etapa4-input.png)

O resultado é registrado com a ajuda da função `enumerate()` que recupera o índice da lista, além do nome dos filmes e de quantas vezes foram registradas após a iteração. A função lambda é responsável ainda por ordenar a lista de forma decrescente à partir da quantidade de registros de cada filme. Os registros foram realizados conforme a formatação requisitada:

![output etapa 4](./Exercícios/etl/evidencias/etapa4-output.png)

5. Por fim, para a etapa 5 o enunciado pede: "Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (coluna Total Gross), em ordem decrescente. Ao escrever no arquivo, considere o padrão de saída (nome do ator) - (receita total bruta), adicionando um resultado a cada linha". O código lê os dados, ordena a lista de maneira decrescente pela coluna 'Total Gross' com a ajuda de uma função lambda, mantendo os valores como float para que isso não atrapalhe a ordenação.

![input etapa 5](./Exercícios/etl/evidencias/etapa5-input.png)

Os registros são salvos contendo ordenadamente o nome de cada ator e atriz, e o valor total da receita bruta:

![output etapa 5](./Exercícios/etl/evidencias/etapa5-output.png)

# Certificados
Não foi realizado nenhum curso fora da plataforma Udemy, portanto não foi necessário apresentar nenhum certificado.