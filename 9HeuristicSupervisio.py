import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
# Particular business (sales) strategy log
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_rule.strategy_name FROM  public.strategy_rule ORDER BY strategy_num")
lstname=cursor.fetchall()
stname = list(itertools.chain.from_iterable(lstname))
cursor.execute("SELECT strategy_rule.rule_name FROM  public.strategy_rule ORDER BY strategy_num")
lstrul=cursor.fetchall()
strul = list(itertools.chain.from_iterable(lstrul))
## SQL COMMANDS SPECIFICATION
# Data load of strategies with the supervising rules application
sql = """INSERT INTO strategy_weight(strategy_name, weight) VALUES(%s,%s)"""
## SUPERVISED MACHINE LEARNNING THOUGH THE BUSINESS RULES (HEURISTIC RULES)
# Verification of supervising rules
TRADING = ['order', 'quotation', 'stock', 'sale', 'price', 'customer', 'user']
DEALING = ['seller', 'buyer', 'bill', 'offer', 'promotion', 'billing']

for i in range(len(stname)):
    lst=stname[i].split(' ')
    # Ponderation by structure of strategy (3 points)
    wei1=0
    if (len(strul[i][0]))==4:
         wei1=1
    if (len(strul[i][0]))==9:
        wei1=2
    if (len(strul[i][0]))==55:
        wei1=3 
    # Verification of TRADING and DEALING supervising rules and ponderation (6 points)
    wei2=0
    if len([val for val in TRADING if val in lst]) > 0:
        strul[i].append("TRADING")
        wei2=wei2+len([val for val in TRADING if val in lst])
    if len([val for val in DEALING if val in lst]) > 0:
        strul[i].append("DEALING")
        wei2=wei2+len([val for val in DEALING if val in lst])
    wei=wei1+wei2
    ponderacion=wei/9
    ## DATABASE UPDATING
    cursor.execute(sql, (stname[i],ponderacion))
    conexion.commit()
conexion.close()