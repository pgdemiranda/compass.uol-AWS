-- pais
create table if not exists pais (
    idPais integer primary key,
    nomePais varchar(50) not null
);
-- estado
create table if not exists estado (
    idEstado integer primary key,
    nomeEstado varchar(50) not null,
    idPais integer not null,
    foreign key (idPais) references pais(idPais)
);
-- cidade
create table if not exists cidade (
    idCidade integer primary key,
    nomeCidade varchar(100) not null,
    idEstado integer not null,
    foreign key (idEstado) references estado(idEstado)
);
-- cliente
create table if not exists cliente (
    idCliente integer primary key,
    nomeCliente varchar(100) not null,
    idCidade integer not null,
    foreign key (idCidade) references cidade(idCidade)
);
-- combustivel
create table if not exists combustivel (
    idCombustivel integer primary key,
    tipoCombustivel varchar(50) not null
);
-- carro
create table if not exists carro (
    idCarro integer primary key,
    classiCarro varchar(20) not null unique,
    marcaCarro varchar(50) not null,
    modeloCarro varchar(50) not null,
    anoCarro integer not null,
    idCombustivel integer not null,
    foreign key (idCombustivel) references combustivel(idCombustivel)
);
-- diaria
create table if not exists diaria (
    idDiaria integer primary key,
    idCarro integer not null,
    vlrDiaria decimal(10, 2) not null,
    foreign key (idCarro) references carro(idCarro)
);
-- vendedor
create table if not exists vendedor (
    idVendedor integer primary key,
    nomeVendedor varchar(100) not null,
    sexoVendedor char(1) not null,
    idEstado integer not null,
    foreign key (idEstado) references estado(idEstado)
);
-- locacao
create table if not exists locacao (
    idLocacao integer primary key,
    idCliente integer not null,
    idCarro integer not null,
    idDiaria integer not null,
    dataLocacao date not null,
    horaLocacao time not null,
    qtdDiaria integer not null,
    dataEntrega date not null,
    horaEntrega time not null,
    kmCarro integer not null,
    idVendedor integer not null,
    foreign key (idCliente) references cliente(idCliente),
    foreign key (idCarro) references carro(idCarro),
    foreign key (idDiaria) references diaria(idDiaria),
    foreign key (idVendedor) references vendedor(idVendedor)
);