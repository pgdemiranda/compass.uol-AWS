-- view dimensão data de locação
create view dim_data_locacao as
with datas_das_locacoes as (
    select
    	dataLocacao,
    	horaLocacao,
        substr(dataLocacao, 1, 4) || '-' || 
        substr(dataLocacao, 5, 2) || '-' || 
        substr(dataLocacao, 7, 2) AS data_formatada,
        case when instr(horaLocacao, ':') = 2 
             then '0' || horaLocacao 
             else horaLocacao end as hora_formatada
    from 
        locacao
)
select 
	dataLocacao,
	horaLocacao,
    data_formatada,
    hora_formatada,
    data_formatada || ' ' || hora_formatada || ':00' as data_hora_locacao,
    strftime('%Y', data_formatada) as ano,
    strftime('%m', data_formatada) as mes,
    strftime('%d', data_formatada) as dia,
    cast(strftime('%w', data_formatada) as integer) as dia_semana
from 
    datas_das_locacoes;

-- view dimensão data de entrega
create view dim_data_entrega as
with datas_das_entregas as (
    select
    	dataEntrega,
		horaEntrega,
        dataEntrega,
        horaEntrega,
        substr(dataEntrega, 1, 4) || '-' || 
        substr(dataEntrega, 5, 2) || '-' || 
        substr(dataEntrega, 7, 2) as data_formatada,   
        case 
            when length(trim(horaEntrega)) = 4 then '0' || horaEntrega
            else horaEntrega 
        end as hora_formatada
    from 
        locacao
)
select
	dataEntrega,
	horaEntrega,
    data_formatada,
    hora_formatada,
    data_formatada || ' ' || hora_formatada || ':00' as data_hora_entrega,
    strftime('%Y', data_formatada) as ano,
    strftime('%m', data_formatada) as mes,
    strftime('%d', data_formatada) as dia,
    cast(strftime('%w', data_formatada) as integer) as dia_semana
from 
    datas_das_entregas;

-- view dimensão cliente
create view dim_cliente as
select 
    c.idCliente as id_cliente,
    c.nomeCliente as nome_cliente,
    ci.nomeCidade as cidade_cliente,
    e.nomeEstado as estado_cliente,
    p.nomePais as pais_cliente
from cliente c
inner join cidade ci on c.idCidade = ci.idCidade
inner join estado e on ci.idEstado = e.idEstado
inner join pais p on e.idPais = p.idPais;

-- view dimensão vendedor
create view dim_vendedor as
select 
    v.idVendedor as id_vendedor,
    v.nomeVendedor as nome_vendedor,
    v.sexoVendedor as sexo_vendedor,
    e.nomeEstado as estado_vendedor
from vendedor v
inner join estado e on v.idEstado = e.idEstado;

-- view dimensão carro
create view dim_carro as
select 
    car.idCarro as id_carro,
    car.classiCarro as classi_carro,
    car.marcaCarro as marca_carro,
    car.modeloCarro as modelo_carro,
    car.anoCarro as ano_carro,
    comb.tipoCombustivel as tipo_combustivel,
    d.vlrDiaria as valor_diaria
from carro car
inner join combustivel comb on car.idCombustivel = comb.idCombustivel
inner join diaria d on car.idCarro = d.idCarro;

-- view fato locacao
create view fato_locacao as
select 
    l.idLocacao as id_locacao,
    dc.id_cliente,
    dca.id_carro,
    dv.id_vendedor,
    dca.valor_diaria,
    l.qtdDiaria as qtd_diaria,
    l.kmCarro as km_carro,
    (l.qtdDiaria * dca.valor_diaria) as valor_total,
    dl.data_hora_locacao,
    de.data_hora_entrega,
    dl.ano as ano_locacao,
    dl.mes as mes_locacao,
    dl.dia as dia_locacao,
    dl.dia_semana as dia_semana_locacao,
    de.data_hora_entrega - dl.data_hora_locacao as duracao_locacao_dias
from locacao l
inner join dim_data_locacao dl on l.dataLocacao = dl.dataLocacao and l.horaLocacao  = dl.horaLocacao
inner join dim_data_entrega de on l.dataEntrega = de.dataEntrega and l.horaEntrega = de.horaEntrega
inner join dim_cliente dc on l.idCliente = dc.id_cliente 
inner join dim_carro dca on l.idCarro = dca.id_carro
inner join dim_vendedor dv on l.idVendedor = dv.id_vendedor;