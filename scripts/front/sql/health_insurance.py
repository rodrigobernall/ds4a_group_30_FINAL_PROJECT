select case when p.p6090=1 then 'Sí' when p.p6090=2 then 'No' else 'No informa' end as "¿Afiliado a salud?", round(sum(p.fex_c_2011)) as "Conteo" from area_personas p where p.mes=9 group by p.p6090;
