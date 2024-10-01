import psycopg2


def create_database(params):
    """
    Создаем базу данных coursework_5
    """
    conn = psycopg2.connect(dbname="cw5", **params)
    # conn = psycopg2.connect(
    #     host="localhost",
    #     user="postgres",
    #     password="2468",
    #     port=5432
    # )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("""DROP DATABASE IF EXISTS courswork5""")
    cur.execute("""CREATE DATABASE courswork5""")

    cur.close()
    conn.close()
