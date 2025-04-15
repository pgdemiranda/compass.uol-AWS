-- Apresente a query para listar o autor com maior número de livros publicados. 
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes. 

select
    a.codAutor,
    a.nome,
    count(*) as quantidade_publicacoes
from autor a
inner join livro l on a.codautor = l.autor
group by a.nome
order by quantidade_publicacoes desc
limit 1