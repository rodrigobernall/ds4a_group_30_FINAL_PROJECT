# DATA WRANGLING LOG

## Census data

1. We downloaded our raw data from the DANE website as Stata files and compressed it.
1. The compressed file was uploaded to a personal Dropbox account ([link]('https://www.dropbox.com/sh/y6mye017c5oitfy/AAC7ci0RWx17eBRIQumfA6TYa?dl=1))
1. We used the notebook `scripts/data_wrangling/convert_to_postgresql.ipynb` to convert the files to CSV and save them locally as a zipped file.
1. The zipped file (`exportados.zip`) was unzipped in a local Unix machine. There was one set of files per each department.
1. We unzipped each and every file and deleted the header (using `sed`) and a column that was a by-product of the Stata to CSV conversion. In order to do that, we ungzipped every file in each folder, used `cut` (from Bash) to get rid of the excess column and gzipped again.
1. We used Bash to classify the files in folders. For instance, for the `per` dataset (persons,) we used `mkdir per` and then `mv *per_list.csv.gz per` to get all the files into the same directory.
1. We gzipped the files again and concatenated them (using `cat`) into one big file per table.
1. We used `psql \copy` to upload the gzipped files to the AWS RDS PostgreSQL instance. This part was done manually with this command (here `per` is the example table): `\copy per from program 'gzip -dc per_concatenated.csv.gz' DELIMITER ',' CSV`

A Bash script with the commands used can be found in the current directory.

The `municipalities` table had from its original source a unique identifier for each municipality, but this identifier was incompatible with the other data sources because it was concatenated to the department identifier. For instance, Medellín's id was `05001`, and we needed it to be just `001` (`05` is the identifier of the department of which Medellín is the capital.) In order to correct this situation, we created a new column and updated it with a SQL `UPDATE` statement:

```SQL
update municipalities set divipol_municipality_clean=subquery.right
from(select divipol_municipality, right(divipol_municipality, 3) from municipalities) as subquery
where municipalities.divipol_municipality=subquery.divipol_municipality;

```
## Great survey data

Since the downloaded data has commas as decimal delimiters, we had to replace them with dots. We renamed all the files that corresponded to the same table because they had different names, and then replaced the delimiters with a `sed` regex. For instance, for the `area_ocupados` table, we did this (while in a directory that contained the original zipped files from the DANE):

```Bash
for file in `ls`; do unzip $file; done
find . -type f -name '*rea - Ocupados.csv' -execdir mv {} area_ocupados.csv ';'
find -name 'area_ocupados.csv' -exec sed -i 's/\([0-9]\),/\1./g' {} \;

```
See an explanation of the sed command [here](https://stackoverflow.com/questions/38593855/replacing-commas-in-a-csv-file-with-sed-for-mongoimport). For the `find` command used to renema the file read [here](https://unix.stackexchange.com/a/261048)
