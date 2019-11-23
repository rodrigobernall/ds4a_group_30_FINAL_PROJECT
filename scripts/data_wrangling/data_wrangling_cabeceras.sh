# Process the data for the area_vivienda_hogares table and do the SQL copy
find . -type f -name 'Cabecera - Vivienda y Hogares.csv' -execdir mv {} cabecera_vivienda_hogares.csv ';'
find . -name 'cabecera_vivienda_hogares.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'cabecera_vivienda_hogares.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy vivienda_hogares (DIRECTORIO, SECUENCIA_P, P5000, P5010, P5020, P5030, P5040, P5050, P5070, P5080, P5090, P5090S1, P5100, P5110, P5130, P5140, P5210S1, P5210S2, P5210S3, P5210S4, P5210S5, P5210S6, P5210S7, P5210S8, P5210S9, P5210S10, P5210S11, P5210S14, P5210S15, P5210S16, P5210S17, P5210S18, P5210S19, P5210S20, P5210S21, P5210S22, P5210S24, P5220, P5220S1, P6008, P6007, P6007S1, HOGAR, P4000, P4010, P4020, P4030S1, P4030S1A1, P4030S2, P4030S3, P4030S4, P4030S4A1, P4030S5, P4040, REGIS, clase, MES, DPTO, fex_c_2011, AREA)
FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;

# Process the data for the area_ocupados table and do the SQL copy
find . -type f -name '*rea - Ocupados.csv' -execdir mv {} area_ocupados.csv ';'
find . -name 'area_ocupados.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_ocupados.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_ocupados FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;

# Process the data for the area_personas table and do the SQL copy
find . -type f -name '*rea - Caracter*sticas generales (Personas).csv' -execdir mv {} area_personas.csv ';'
find . -name 'area_personas.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_personas.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_personas FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;

# Process the data for the area_fuerza_trabajo table and do the SQL copy
find . -type f -name '*rea - Fuerza de trabajo.csv' -execdir mv {} area_fuerza_trabajo.csv ';'
find . -name 'area_fuerza_trabajo.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_fuerza_trabajo.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_fuerza_trabajo FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;

# Process the data for the area_desocupados table and do the SQL copy
find . -type f -name '*rea - Desocupados.csv' -execdir mv {} area_desocupados.csv ';'
find . -name 'area_desocupados.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_desocupados.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_desocupados FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;


# Process the data for the area_inactivos table and do the SQL copy
find . -type f -name '*rea - Inactivos.csv' -execdir mv {} area_inactivos.csv ';'
find . -name 'area_inactivos.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_inactivos.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_inactivos FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;


# Process the data for the area_otras_actividades_ayudas table and do the SQL copy
find . -type f -name '*rea - Otras actividades y ayudas en la semana.csv' -execdir mv {} area_otras_actividades_ayudas.csv ';'
find . -name 'area_otras_actividades_ayudas.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_otras_actividades_ayudas.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_otras_actividades_ayudas FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;


# Process the data for the area_otros_ingresos table and do the SQL copy
find . -type f -name '*rea - Otros ingresos.csv' -execdir mv {} area_otros_ingresos.csv ';'
find . -name 'area_otros_ingresos.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_otros_ingresos.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_otros_ingresos FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;
