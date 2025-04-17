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