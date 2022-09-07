from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
import psycopg2
import json

class DatabaseCursor(object):
    
    def __init__(self, conn_config_file):
        with open(conn_config_file) as config_file:
            self.conn_config = json.load(config_file)

    def __enter__(self):
        self.conn = psycopg2.connect(
            "dbname='"
            + self.conn_config["dbname"]
            + "' "
            + "user='"
            + self.conn_config["user"]
            + "' "
            + "host='"
            + self.conn_config["host"]
            + "' "
            + "password='"
            + self.conn_config["password"]
            + "' "
            + "port="
            + self.conn_config["port"]
            + " "
        )
        #  
        self.cur = self.conn.cursor()
        self.cur.execute("SET search_path TO " + self.conn_config["schema"])

        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # some logic to commit/rollback
        self.conn.commit()
        self.conn.close()


description = """🚀 FastAPI + PostgreSQL """

app = FastAPI(
    title = "LOIC API Project 01",
    description = description,
    version = "0.0.1",
    contact = {
        "name": "Loic K",
        "url": "https://www.linkedin.com/in/loickonan/",
    },
    license_info = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

@app.get("/")
async def docs_redirect():
    """WELCOME TO THE WORLD AIRPORTS DATABASE API
    Api's base route that displays the information created above in the Api Info section."""
    return RedirectResponse(url="/docs")

@app.get("/airports2")
async def airports2():
    """Display all the AIRPORTS from the World."""
    sql = "select * from airports2"

    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()


@app.get("/airport/{country}")
async def airports2(country):
    """Display all the AIRPORTS from a specific country."""
    sql = f"""SELECT * from airports2 
              WHERE country = '{country}'"""

    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchall()


@app.get("/airportCount")
async def airports2(country: str):
    """Display the total number of AIRPORTS from a specific country."""
    sql = f"""SELECT count(*) from airports2 
              WHERE country = '{country}'"""

    with DatabaseCursor(".config.json") as cur:
        cur.execute(sql)
        return cur.fetchone()


if __name__ == "__main__":
    uvicorn.run("api:app", port=8000, reload=True)