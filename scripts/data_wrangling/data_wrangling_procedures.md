# Data wrangling log

1. We downloaded our raw data from the DANE website as Stata files and compressed it.
1. The compressed file was uploaded to a personal Dropbox account ([link]('https://www.dropbox.com/sh/y6mye017c5oitfy/AAC7ci0RWx17eBRIQumfA6TYa?dl=1))
1. We used the notebook `scripts/data_wrangling/convert_to_postgresql.ipynb` to convert the files to CSV and save them locally as a zipped file.
1. The zipped file (`exportados.zip`) was unzipped in a local Unix machine. There was one set of files per each department.
1. We unzipped each and every file and deleted the header (using `sed`) and a column that was a by-product of the Stata to CSV conversion. In order to do that, we ungzipped every file in each folder, used `cut` (from Bash) to get rid of the excess column and gzipped again.
1. We used Bash to classify the files in folders. For instance, for the `per` dataset (persons,) we used `mkdir per` and then `mv *per_list.csv.gz per` to get all the files into the same directory.
1. We gzipped the files again and concatenated them (using `cat`) into one big file per table.
1. We used `psql \copy` to upload the gzipped files to the AWS RDS PostgreSQL instance. This part was done manually with this command (here `per` is the example table): `\copy per from program 'gzip -dc per_concatenated.csv.gz' DELIMITER ',' CSV`

A Bash script with the commands used can be found in the current directory.
