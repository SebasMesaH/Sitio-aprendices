create database sena;
use sena;

create table aprendiz(
id int(11) primary key not null,
nombre_completo varchar(100) not null,
telefono int(15) not null,
curso varchar(45) not null,
promedio int(1) not null)
engine=InnoDB charset=utf8;



