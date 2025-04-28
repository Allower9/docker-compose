from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DATABASE_HOST = os.getenv("API_DB_HOST", "localhost")
DATABASE_PORT = os.getenv("API_DB_PORT", "5432")
DATABASE_NAME = os.getenv("API_DB_NAME", "api")
DATABASE_USER = os.getenv("API_DB_USER", "apiuser")
DATABASE_PASS = os.getenv("API_DB_PASS", "apipass")

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

@app.get("/")
async def root():
    cursor.execute(
        "SELECT version();"
    )
    item = cursor.fetchone()
    return {"message": "Hello World",
            "postgres_version": item[0]}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"} 
