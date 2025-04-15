-- Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. 
-- Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

select distinct(a.nome)
from editora e
inner join endereco en on e.endereco = en.codendereco
inner join livro l on e.codeditora = l.editora
inner join autor a on l.autor = a.codautor
where en.estado not in ('RIO GRANDE DO SUL', 'SANTA CATARINA', 'PARANÁ')
order by a.nome
