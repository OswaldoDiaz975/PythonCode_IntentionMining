import csv
import psycopg2
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='test'")
cursor=conexion.cursor()
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_qel(strategy_name) VALUES (%s)"""
## CSV FILE READING (QUALITY EVENT LOG OF BUSINESS "SALES BUSINESS IN PARTICULAR")
f= open("//qel.csv")
reader = csv.reader(f)
for row in reader:	
    ## DATABASE UPDATING
    cursor.execute(sql, (row))
    conexion.commit()
conexion.close()
f.close()