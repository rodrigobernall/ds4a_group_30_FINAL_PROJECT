# Final project - Group 30 (DS4A Colombia 2019)

## Folder structure

- models: contain all reutilizable functions such as predictors and functions. 
- Scripts : where we are going to store notebooks
- Output : plots, table and logbook of the project 
- Input : All data sources

This is Leandro's first commit.

## Database tables

Our database has the following tables:

- `per`: Personas (people.)
- `viv`: Viviendas (houses.)
- `hog`: Hogares (households.)
- `mgn`: Marco geográfico nacional (geographical data.)
- `fall`: Fallecidos (deceased people.)

Intermediate tables:

- `departments`: Departments and their codes. Taken from [the DANE.](https://geoportal.dane.gov.co/consultadivipola.html)
- `municipalities`: Municipalities and their codes. Taken from [the DANE.](https://geoportal.dane.gov.co/consultadivipola.html)
- `edad_dict`: A table that contains the translation of the codes for the ages that are in the `per` table.
