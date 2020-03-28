

Create table if not exists test (
    valor_01 int not null Identity (1,3),
    valor_02 int not null,
    Resultado int,
    usuario varchar(30) not null,
    constraint primary key (id)
) default chartset = 'utf8';