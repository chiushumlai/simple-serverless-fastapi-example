from fastapi import APIRouter
import psycopg2
from psycopg2.extras import RealDictCursor
import json

from app.core import config

router = APIRouter()
# host = config.settings.postgres_host
# port = config.settings.postgres_port
# username = config.settings.postgres_username
# password = config.settings.postgres_password
# database = config.settings.postgres_database

host = "cicd-test-csl.cgmxl7co3jeh.us-east-1.rds.amazonaws.com"
port = 5432
username = "postgres"
password = "abcd1234"
database = "postgres"

@router.get("/")
async def root():
    conn = psycopg2.connect(
        host = host,
        port = port,
        database = database,
        user = username,
        password = password
    )
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('''select now()''')
    results = cur.fetchall()
    # json_result = json.dumps(results)
    # print(json_result)
    return {"message": results}

@router.get("/create")
async def create_db():
    conn = psycopg2.connect(
        host = host,
        port = port,
        database = database,
        user = username,
        password = password
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('''create table customerInfo (id SERIAL PRIMARY KEY, name text, age float)''')
    # results = cur.fetchall()
    # json_result = json.dumps(results)
    # print(json_result)
    return {"message": "successfully created"}

@router.get("/insert")
async def insert_db():
    conn = psycopg2.connect(
        host = host,
        port = port,
        database = database,
        user = username,
        password = password
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('''insert into customerInfo (name, age) values ('abc', extract(minute from now()))''')
    # results = cur.fetchall()
    # json_result = json.dumps(results)
    # print(json_result)
    return {"message": "successfully inserted"}

@router.get("/show")
async def insert_db():
    conn = psycopg2.connect(
        host = host,
        port = port,
        database = database,
        user = username,
        password = password
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('''select * from customerInfo''')
    results = cur.fetchall()
    json_result = json.dumps(results)
    return json_result