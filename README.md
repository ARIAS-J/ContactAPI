
# Rest API - Contacts

## How to run


```bash
  git clone https://github.com/No-Hex/ContactAPI

  cd ContactAPI
```

```bash
  cd backend

  pip install -r requirements.txt
```
## Variables de entorno

Crear un archivo .env y añadir las siguientes variables con la informacion
requerida.

```bash
SECRETKEY='' #Secret Key de Django

DATABASE_NAME=''
DATABASE_USER=''
DATABASE_PASS=''
DATABASE_HOST=''
DATABASE_PORT=''
```
Migraciones
```bash
  py manage.py makemigrations

  py manage.py migrate
```
## Run server.
```bash
  py manage.py runserver
```
## Tech Stack

**Framework:** Django, Django REST framework

**Language:** Python

**Database:** PostgreSQL