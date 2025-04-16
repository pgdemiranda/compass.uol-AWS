-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
-- e que estas vendas estejam com o status concluída.  
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

with vendedores_x_vendas as (
select
	vdo.cdvdd,
	vdo.nmvdd,
	count(vda.cdven) as qtd_vendas
from tbvendedor vdo
left join tbvendas vda on vdo.cdvdd = vda.cdvdd
where vda.status = 'Concluído'
group by vdo.cdvdd, vdo.nmvdd
)
select
	cdvdd,
	nmvdd
from vendedores_x_vendas
order by qtd_vendas desc
limit 1

