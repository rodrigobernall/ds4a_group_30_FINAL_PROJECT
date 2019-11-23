# Process the data for the vivienda_hogares table and do the SQL copy
find . -type f -name 'Cabecera - Vivienda y Hogares.csv' -execdir mv {} cabecera_vivienda_hogares.csv ';'
find . -name 'cabecera_vivienda_hogares.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'cabecera_vivienda_hogares.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy vivienda_hogares (DIRECTORIO, SECUENCIA_P, P5000, P5010, P5020, P5030, P5040, P5050, P5070, P5080, P5090, P5090S1, P5100, P5110, P5130, P5140, P5210S1, P5210S2, P5210S3, P5210S4, P5210S5, P5210S6, P5210S7, P5210S8, P5210S9, P5210S10, P5210S11, P5210S14, P5210S15, P5210S16, P5210S17, P5210S18, P5210S19, P5210S20, P5210S21, P5210S22, P5210S24, P5220, P5220S1, P6008, P6007, P6007S1, HOGAR, P4000, P4010, P4020, P4030S1, P4030S1A1, P4030S2, P4030S3, P4030S4, P4030S4A1, P4030S5, P4040, REGIS, clase, MES, DPTO, fex_c_2011, AREA) FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;

# Process the data for the ocupados table and do the SQL copy
find . -type f -name 'Cabecera - Ocupados.csv' -execdir mv {} cabecera_ocupados.csv ';'
find . -name 'cabecera_ocupados.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'cabecera_ocupados.csv' -exec psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy ocupados (DIRECTORIO, SECUENCIA_P, ORDEN, HOGAR, REGIS, CLASE, P388, P6440, P6450, P6460, P6460S1, P6400, P6410, P6410S1, P6422, P6424S1, P6424S2, P6424S3, P6426, P6430S1, P6480, P6480S1, P9440, P6500, P6510, P6510S1, P6510S2, P6590, P6590S1, P6600, P6600S1, P6610, P6610S1, P6620, P6620S1, P6585S1, P6585S1A1, P6585S1A2, P6585S2, P6585S2A1, P6585S2A2, P6585S3, P6585S3A1, P6585S3A2, P6585S4, P6585S4A1, P6585S4A2, P6545, P6545S1, P6545S2, P6580, P6580S1, P6580S2, P6630S1, P6630S1A1, P6630S2, P6630S2A1, P6630S3, P6630S3A1, P6630S4, P6630S4A1, P6630S6, P6630S6A1, P6640, P6640S1, P6765, P6765S1, P6772, P6772S1, P6773S1, P6775, P6750, P6760, P550, P6780, P6780S1, P6790, P1800, P1800S1, P1801S1, P1801S2, P1801S3, P1802, P1879, P1805, P6800, P6810, P6810S1, P6850, P6830, P6830S1, P6870, P6880, P6880S1, P6915, P6915S1, P6920, P6930, P6940, P6960, P6980, P6980S1, P6980S2, P6980S3, P6980S4, P6980S5, P6980S6, P6980S7, P6980S7A1, P6980S8, P6990, P9450, P7020, P760, P7026, P7028, P7028S1, P7040, P390, P7045, P7050, P7050S1, P7070, P7075, P7077, P1880, P1881, P1882, P7090, P7100, P7110, P7120, P7130, P7140, P7140S1, P7140S2, P7140S3, P7140S4, P7140S5, P7140S6, P7140S7, P7140S8, P7140S9, P7140S9A1, P7150, P7160, P7170S1, P7170S5, P7170S6, P7180, P514, P515, P7240, P7240S1, OFICIO, RAMA2D, OCI, MES, P6430, RAMA4D, RAMA4DP8, RAMA2DP8, INGLABO, DPTO, fex_c_2011, AREA) FROM {}  CSV DELIMITER ';' HEADER NULL ' '"  \;

# Process the data for the area_personas table and do the SQL copy
find . -type f -name 'Cabecera - Caracter*sticas generales (Personas).csv' -execdir mv {} cabecera_personas.csv ';'
find . -name 'cabecera_personas.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;
find . -name 'cabecera_personas.csv' -exec sed -i header_csv=$(sed 1q {} | sed 's/;/,/g') \;
header_sql=" ($var1) "
find . -name 'cabecera_personas.csv' -exec sed -i '1d' {} \;
find . -name 'cabecera_personas.csv' -exec cat {} > cabecera_personas_concat.csv +
PGPASSWORD=$DB_PASS_FINAL_30 psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30 -c "\\copy personas $header_sql FROM cabecera_personas_concat.csv CSV DELIMITER ';' HEADER NULL ' '"

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
