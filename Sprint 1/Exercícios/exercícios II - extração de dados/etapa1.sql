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