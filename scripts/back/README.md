# Server end points 

- url = `18.221.120.194:8020`
- `/factors/<table>` Return a json with the factors and their values. The tables that can be `sex_dict` , `edad_dict` , `education_dict` and `marital_dict`
- how to run it :
    - dont forget tu make build the .env file with structure like this 
        - `DB_NAME=postgres ...`
    - `sudo docker build -t ds4a .`
    - `sudo docker run -p 8020:8020 -d --restart=always --env-file test.env --name ds4a ds4a`
- filter builder is capable of filtering the flowing fields: 
    - `u_dpto`, `u_mpio`, `p_sexo`, `p_edad`, `p_est_civil`, `p_nivel_anos`
    - One example of the request at `/filtered_table`:
        - {
	"table":"per",
	"filters":{"u_dpto":["54"], "u_mpio":["405"],"p_sexo":["2.0"], "p_edad":["3.0"], "p_est_civil":["7.0"], "p_nivel_anos":["1.0"]}
}