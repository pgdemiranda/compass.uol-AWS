-- pais
insert into pais (nomePais)
select distinct paisCLiente 
from tb_locacao 
where paisCLiente is not null;

-- estado
insert into estado (idEstado, nomeEstado, idPais)
select 
    row_number() over (order by tl.estadoCliente, p.idPais) as id,
    tl.estadoCliente,
    p.idPais
from (select distinct estadoCliente, paisCliente from tb_locacao where estadoCliente is not null) tl
inner join pais p ON tl.paisCliente = p.nomePais;

-- cidade
insert into cidade (idCidade, nomeCidade, idEstado)
select
	row_number() over (order by c.cidade, e.idEstado) as id,
	c.cidade,
	e.idEstado
from (select distinct l.cidadeCliente as cidade, l.estadoCliente as estado from tb_locacao l where l.cidadeCliente is not null) c
inner join estado e on c.estado = e.nomeEstado;

-- cliente
insert into cliente (idCliente, nomeCliente, idCidade)
select
    row_number() over (order by c.nome) as id,
    c.nome,
    c.idCidade
from (
    select distinct
        tl.nomeCliente as nome,
        ci.idCidade
    from tb_locacao tl
    join cidade ci on tl.cidadeCliente = ci.nomeCidade
    where tl.nomeCliente is not null
) c;

-- combustivel
insert into combustivel (idCombustivel, tipoCombustivel)
select
    row_number() over (order by tipoCombustivel) as id,
    tipoCombustivel
from (
    select distinct tipoCombustivel 
    from tb_locacao 
    where tipoCombustivel is not null
);

-- carro
insert into carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
select 
    row_number() over (order by t.modeloCarro, t.anoCarro) as id,
    t.classiCarro,
    t.marcaCarro,
    t.modeloCarro,
    t.anoCarro,
    c.idCombustivel
from (
    select distinct
        classiCarro,
        marcaCarro,
        modeloCarro,
        anoCarro,
        tipoCombustivel
    from tb_locacao
    where classiCarro is not null
    and marcaCarro is not null
    and modeloCarro is not null
    and anoCarro is not null
    and tipoCombustivel is not null
) t
inner join combustivel c on t.tipoCombustivel = c.tipoCombustivel;

-- diaria 
insert into diaria (idDiaria, idCarro, vlrDiaria)
select
    row_number() over (order by idCarro, vlrDiaria) as id,
    idCarro,
    vlrDiaria
from (
    select distinct
        c.idCarro,
        t.vlrDiaria
    from tb_locacao t
    inner join carro c on t.modeloCarro = c.modeloCarro 
                      and t.marcaCarro = c.marcaCarro
                      and t.anoCarro = c.anoCarro
    where t.vlrDiaria is not null
) dados_unicos;

-- vendedor
insert into vendedor (idVendedor, nomeVendedor, sexoVendedor, idEstado)
select
    row_number() over (order by nomeVendedor) as id,
    nomeVendedor,
    sexoVendedor,
    e.idEstado
from (
    select distinct
        t.nomeVendedor,
        t.sexoVendedor,
        t.estadoVendedor
    from tb_locacao t
    where t.nomeVendedor is not null
      and t.sexoVendedor is not null
      and t.estadoVendedor is not null
) dados_vendedor
inner join estado e on dados_vendedor.estadoVendedor = e.nomeEstado;

-- locacao
insert into locacao (idLocacao, idCliente, idCarro, idDiaria, dataLocacao, horaLocacao, qtdDiaria, dataEntrega, horaEntrega, kmCarro, idVendedor)
select
    tl.idLocacao,
    cli.idCliente,
    car.idCarro,
    dia.idDiaria,
    tl.dataLocacao,
    tl.horaLocacao,
    tl.qtdDiaria,
    tl.dataEntrega,
    tl.horaEntrega,
    tl.kmCarro,
    ven.idVendedor
from tb_locacao tl
inner join cliente cli on tl.nomeCliente = cli.nomeCliente
inner join cidade c_cli on cli.idCidade = c_cli.idCidade and c_cli.nomeCidade = tl.cidadeCliente
inner join carro car on tl.modeloCarro = car.modeloCarro 
                     and tl.marcaCarro = car.marcaCarro 
                     and tl.anoCarro = car.anoCarro
inner join diaria dia on dia.idCarro = car.idCarro and dia.vlrDiaria = tl.vlrDiaria
inner join vendedor ven on tl.nomeVendedor = ven.nomeVendedor
inner join estado e_ven on ven.idEstado = e_ven.idEstado and e_ven.nomeEstado = tl.estadoVendedor
where tl.idLocacao is not null
group by tl.idLocacao;