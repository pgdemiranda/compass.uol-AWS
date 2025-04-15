-- Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
-- O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
-- Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

select
	count(*) as quantidade,
	ed.nome,
	en.estado,
	en.cidade
from editora ed
inner join livro l on ed.codEditora = l.editora
inner join endereco en on ed.endereco = en.codendereco
group by
	ed.nome,
	en.estado,
	en.cidade
order by quantidade desc
limit 5