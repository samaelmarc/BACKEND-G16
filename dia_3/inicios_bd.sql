-- sql > Strure Query Languaje
-- DML , Data Manipulation Languaje ( Lenguaje de manipulacion de datos)
-- DDL Data Definition Languaje ( Lenguaje de Definicion de Datos)

-- Primero DDL, sirve como se almacenara los datos , para definir las columnas , tablas entre otros
-- Siempre los comandos en sql tienen que finalizar en ";"
create database if not exists pruebas;
use  pruebas;
create table personas (
	id int primary key auto_increment,
    nombre text null,
    apellido varchar(50),
    fecha_nacimiento date,
    nacionalidad varchar(100) default 'peruano'
    -- primary key (id) -- forma aislada
);

select uuid();
-- DML , Data Manipulation Languaje ( Lenguaje de manipulacion de datos)
-- agregar informacion a la tabla
 
 insert into personas(id,nombre, apellido, fecha_nacimiento) values(default,'samael','jimenez','1992-08-01');
 
 -- si no declaro las columnas que voy a insertar me veo en la obligacion de colocar los valores
 -- a todas las columnas y siguiendo el mismo orden  que use al momento  de crear la tabla
 
insert into personas values(default,'juana','martinez','2000-08-01','URUGUAYA');
insert into personas(id,nombre, apellido, fecha_nacimiento,nacionalidad) values
						(default,'bryan','urquizo','1995-08-01','peruano'),
                        (default,'Maria','Retamozo','1998-08-01','salvadoreña');

select id,nombre from personas;

select*from personas;

select* -- columnas
from personas -- tabla
where nombre = 'samael'; -- condicional

select * from personas
where nacionalidad = 'peruano'
 and id = 3;
 
select * from personas where nombre like '%a%'; -- %% no interesa donde se ubica el caracter
select * from personas where nombre like '%_u%'; 3

-- devolver todas las personas donde cuyo nombre tenga la letra 'r' o en su apellido tenga la letra 'a'

select * from personas where nombre like '%r%' or apellido like '%a%';

select * from personas where id in (1,2,3);
select * from personas where id = 1 or id = 2 or id = 3;
-- caso: sucede a diario en las apis que no estan paginadas, significa que muestra toda la informacion
-- innecesariamente para estos casos se utiliza el siguiente codigo example
select * from personas limit 2; -- 2 elementos  por pagina
select * from personas limit 2 offset 2; -- offset sirve para indicar cuantos se tiene que saltar

-- actualizaciones
update personas 
set nombre = 'rodrigo', apellido = 'flores'
where id = 1;
select *  from personas where id = 1;
-- borrar 
delete from personas where id = 4;
select *from personas;

-- creamos otra tabla DIRECCIONES para ver la integridad , formas normales
