-- Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero).
-- As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
-- Observação: Apenas vendas com status concluído.

select
	t.cddep,
	t.nmdep,
	t.dtnasc,
	sum(v.qtd * v.vrunt) as valor_total_vendas
from tbvendas v
inner join tbdependente t on v.cdvdd = t.cdvdd
where v.status = 'Concluído'
group by v.cdvdd
order by valor_total_vendas
limit 1