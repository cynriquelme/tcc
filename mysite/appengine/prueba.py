import psycopg2
conn = psycopg2.connect(user="postgres", password="postgres", database="proyecto_tcc", host="127.0.0.1", port="5432")
print("Successfully connected!")