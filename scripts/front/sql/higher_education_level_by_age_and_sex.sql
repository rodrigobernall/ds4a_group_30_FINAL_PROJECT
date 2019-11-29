select
p.p6040 as "Edad"
,case
	when p.p6020=1 then 'Hombre'
	when p.p6020=2 then 'Mujer'
	else 'No disponible' end as "Sexo"
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
from area_personas p where p.mes=9 and p.area=11 group by p.p6040, p.p6020, p.p6210;
