# python-development
Python API Development workdone.

## Installations and Python 3.8 Virtual Environment
Install Visual Studio code.
Install Python 3.8
'''
python3 -m venv {your virtual environment name} /
venv {your virtual environment name} /
cd {your virtual environment name}/bin /
source ./activate
'''

Now, update your Python interpreter as your virtual interpreter path.
Visual Studio Code->View->Command Palette->Python:Select Interpreter

## Install and introduce with FastAPI
'''
pip3 install fastapi[all]
'''

## Run main.py
Go to directory /{your virtual environment} main.py is here.
'''
uvicorn main:app --reload
'''
(--reload helps us for any change no need to restart program)

## Postman Notes
Install Postman, it helps us to test our APIs, I tested my initial APIs by Postman. 

We need to create a schema to get valid reliable data.

HTTP   : CRUD
create : post
read   : get
update : put(all info sent) patch(only changed info sent)
delete : delete

## Postgres/pgadmin4

Create Docker container with postgres image. It can be installed locally too, but I choose to use Docker.

'''
docker volume create --name {your_volume_name} -d local
docker run -it --rm --name {your_container_name} -e POSTGRES_USER="{your_user_name}" -ePOSTGRES_PASSWORD="{your_password}"" -e POSTGRES_DB="{your_db_name}"" -v {your_volume_name}:/var/lib/{your_container_name}/data -p 5432:5432 postgres:latest
'''

I have installed pgadmin locally, and connected to my server/db via my credentials. So, use your credentials above to connect.

ip : 0.0.0.0
port: 5432
 