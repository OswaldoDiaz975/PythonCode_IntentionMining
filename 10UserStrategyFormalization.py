import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
# Particular business (sales) strategy log
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT DISTINCT strategy_name, ROUND(weight,2) FROM strategyweight WHERE weight<>0 ORDER BY ROUND(weight,2) DESC")
lstname=cursor.fetchall()
stname = list(itertools.chain.from_iterable(lstname))
## SQL COMMANDS SPECIFICATION
# Data load of strategies with the supervising rules application
sql = """INSERT INTO user_strategy(strategy_name, ponderation) VALUES(%s,%s)"""
## USER STRATEGIES FORMALIZATION FOR  THE SPECIFIC SALES BUSINESS 
name=""
pond=0
for i in range(len(stname)):
    if i%2==0:
        name=stname[i]
    else:
        pond=stname[i] 
    if name!="" and pond!=0:
        ## DATABASE UPDATING
        cursor.execute(sql, (name,pond))
        conexion.commit()
        name=""
        pond=0         
conexion.close()