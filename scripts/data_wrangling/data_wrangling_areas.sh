# Unzip the files
for file in `ls`; do unzip $file; done

# Process the data for the area_vivienda_hogares table and do the SQL copy
find . -type f -name '*rea - Vivienda y Hogares.csv' -execdir mv {} area_vivienda_hogares.csv ';'
find . -name 'area_vivienda_hogares.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'area_vivienda_hogares.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy area_vivienda_hogares FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;

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
