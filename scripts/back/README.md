# Server end points 

- `/factors/<table>` Return a json with the factors and their values. The tables that can be `edad_dict` , `education_dict` and `marital_dict`
- how to run it :
    - dont forget tu make build the .env file with structure like this 
        - `DB_NAME=postgres`
    - `sudo docker build -t ds4a .`
    - `sudo docker run -p 8020:8020 -d --restart=always --env-file test.env --name ds4a ds4a`