import csv
import psycopg2
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## SQL COMMANDS DEFINITION
sql="""INSERT INTO articles(doc_id, doc_text) VALUES (%s,%s)"""
## CSV FILE READING (FILE OF 200 ARTICLES OF BUSINESS WORLD IN GENERAL)
f= open("//articles200.csv", encoding="utf8")
reader = csv.reader(f)
## DATA LOAD TO DATABASE
for row in reader:
    fila=(row[0], row[1])
    print(fila)
    ## DATABASE UPDATING
    cursor.execute(sql, (fila))
    conexion.commit()
conexion.close()
f.close()