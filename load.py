import psycopg2

def load_to_postgres(records):
    conn = psycopg2.connect(
        host="localhost",
        database="crypto",
        user="postgres",
        password="yourpassword"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id SERIAL PRIMARY KEY,
            name TEXT,
            symbol TEXT,
            price_usd NUMERIC,
            timestamp TIMESTAMP
        );
    """)

    for r in records:
        cur.execute("""
            INSERT INTO crypto_prices (name, symbol, price_usd, timestamp)
            VALUES (%s, %s, %s, %s)
        """, (r["name"], r["symbol"], r["price_usd"], r["timestamp"]))

    conn.commit()
    cur.close()
    conn.close()
