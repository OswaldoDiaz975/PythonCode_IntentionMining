import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
# Particular business (sales) strategy log
conexion = psycopg2.connect(database="postgres", user="postgres", password="espe")
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
TRADING = ['sale', 'sell', 'seller', 'purchase', 'buy', 'buyer', 'bill', 'billing']
DEALING = ['order', 'orders' 'quot', 'quotation', 'stock', 'sale', 'sales', 'price', 'customer', 'user', 'users']

for i in range(len(stname)):
    lst=stname[i].split(' ')
    # Ponderation by structure of strategy 
    wei1=0
    if strul[i][0] == 'VERB':
         wei1=1
    if strul[i][0] == 'NOUN VERB':
        wei1=2
    if strul[i][0] == 'NOUN VERB NOUN' or strul[i][0] == 'ADJECTIVE NOUN VERB' or strul[i][0] == 'NOUN VERB ADVERB':
        wei1=3 
    # Verification of TRADING and DEALING supervising rules and ponderation
    wei2=0
    if len([val for val in TRADING if val in lst]) > 0:      
        strul[i].append("TRADING")
        wei2=wei2+len([val for val in TRADING if val in lst])
    if len([val for val in DEALING if val in lst]) > 0:
        strul[i].append("DEALING")
        wei2=wei2+len([val for val in TRADING if val in lst])
    wei=wei1*wei2
    ponderacion=wei/12 # 12 tokens en total
    ## DATABASE UPDATING
    cursor.execute(sql, (stname[i],ponderacion))
    conexion.commit()
conexion.close()