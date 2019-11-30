select
p.area as "Código de la ciudad"
,ar.area as "Ciudad"
,p.p6040 as "Edad"
,o.oficio as "Código del oficio"
,ocp.ocupacion as "Oficio"
,p.p6020 as "Código del sexo"
,case
	when p.p6020=1 then 'Hombre'
	when p.p6020=2 then 'Mujer'
	else 'No disponible' end as "Sexo"
,p.p6210 as "Código del nivel educativo"
,case
	when p.p6210=1	then 'Ninguno'
	when p.p6210=2 then 'Preescolar'
	when p.p6210=3 then 'Primaria'
	when p.p6210=4 then 'Secundaria'
	when p.p6210=5 then 'Media'
	when p.p6210=6 then 'Superior o universitaria'
	when p.p6210=9 then 'No sabe / no informa'
	else 'No disponible'
--	else 'No informa'
	end as "Máximo nivel educativo"
, round(sum(p.fex_c_2011)) as "Conteo"
from area_personas p left join area_ocupados o
on p.directorio=o.directorio and p.secuencia_p=o.secuencia_p and p.hogar=o.hogar and p.orden=o.orden
left join ocupaciones ocp on o.oficio=ocp.ocup_cod
left join areas ar on ar.area_cod=p.area
where p.mes=9 group by p.area, ar.area, p.p6040, o.oficio, ocp.ocupacion, p.p6020, p.p6210
order by p.area, ar.area, p.p6040, o.oficio, ocp.ocupacion, p.p6020, p.p6210;
