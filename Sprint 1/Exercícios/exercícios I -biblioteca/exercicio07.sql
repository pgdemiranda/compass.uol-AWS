-- Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

with autores_x_quantidade as (
select
	a.codautor,
	a.nome,
	count(l.cod) as quantidade
from autor a 
left join livro l on a.codautor = l.autor
group by a.nome, a.codautor
) 
select 
	nome 
from autores_x_quantidade 
where quantidade = 0 
order by nome