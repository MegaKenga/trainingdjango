# A simple online catalog for NDA company
This is a small django application, introducing online catalog
of products with categories and brands. In plans: a cart and mail notifications services

## Pre-requisites
- python 3.8+ installed
- psql connection available

## Installation:
```shell
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration:
1. Create .env file and populate it with values. Please check .env.example for reference
2. Run initial database commands: 
    ```shell
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```
3. Run collect static command
    ```shell
    python3 manage.py collectstatic
    ```


## Run the app
```shell
python3 manage.py runserver
```