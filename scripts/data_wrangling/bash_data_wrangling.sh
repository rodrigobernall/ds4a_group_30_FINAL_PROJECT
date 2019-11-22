#!/bin/bash
cd exportacion.zip

gunzip *.csv.gz

for file in `ls`
	do sed '1d' $file  > "headless_"$file;
	mv "headless_"$file $file;
done

for file in *;
	do cut -d "," -f1 $file --complement  > "cut_"$file;
	mv "cut_"$file $file;
done


for type in mgn viv fall per hog;
	do mkdir $type;
	mv *$type"_list.csv" $type;
	gzip -r $type;
done

for type in mgn viv fall per hog;
	do cd $type;
	echo "I'm in "$(pwd);
	cat *gz > $type"_concat"
	mv $type"_concat" $type"_concat.csv.gz"
	cd ..;
done


PGPASSWORD=$DB_PASS_FINAL_30 psql -h $DB_HOST_FINAL_30 -d $DB_NAME_FINAL_30 -U $DB_USER_FINAL_30
