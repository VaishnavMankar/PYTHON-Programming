from typing import Union
import psycopg2
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Database connection details
DB_HOST = "your_db_host"
DB_NAME = "your_db_name"
DB_USER = "your_db_user"
DB_PASS = "your_db_password"

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Items WHERE itemid = %s", (item_id,))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        if not rows:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"items": rows, "q": q}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))