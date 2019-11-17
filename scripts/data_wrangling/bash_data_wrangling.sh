#!/bin/bash
cd exportacion.zip

gunzip *.csv.gz

for file in *;
	do cut -d "," -f1 $file --complement  > "cut_"$file;
done


for type in mgn viv fall per hog;
	do mkdir $type;
	mv *"cut_"*$type"_list.csv" $type;
	gzip -r $type;
done

PGPASSWORD=$DB_PASS_FINAL_30 psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30

for type in mgn viv fall per hog;
	do cd $type;
	echo "I'm in "$(pwd);
	for file in `ls`; do \copy $type from program "'gzip -dc "$file"' DELIMITER ',' CSV HEADER NULL"; done;
	cd ..;
done
