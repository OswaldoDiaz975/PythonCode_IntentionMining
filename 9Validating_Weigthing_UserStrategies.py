import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
# Particular business (sales) strategy log
conexion = psycopg2.connect(database="postgres", user="postgres", password="phd1522")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_rule.strategy_name FROM  public.strategy_rule ORDER BY strategy_num")
lstname=cursor.fetchall()
stname = list(itertools.chain.from_iterable(lstname))
cursor.execute("SELECT strategy_rule.rule_name FROM  public.strategy_rule ORDER BY strategy_num")
lstrul=cursor.fetchall()
strul = list(itertools.chain.from_iterable(lstrul))
cursor.execute("SELECT heuristic_rule.hrule_name FROM  public.heuristic_rule ORDER BY hrule_name")
lhrul=cursor.fetchall()
hrul = list(itertools.chain.from_iterable(lhrul))
## SQL COMMANDS SPECIFICATION
# Data load of strategies with the supervising rules application
sql = """INSERT INTO strategy_weight(strategy_name, weight) VALUES(%s,%s)"""
## VALIDATING AND WEIGHTED THROUGH THE BUSINESS RULES (HEURISTIC RULES)
# Verification of supervising rules
TRADING = ['order', 'quotation', 'stock', 'sale', 'price']
DEALING = ['sell', 'buy', 'offer', 'promotion', 'billing', 'cancel']
CRM = ['customer', 'empathy', 'user', 'ecommerce', 'e-commerce', 'omnichannel', 'omni-channel'] ## Customer Relationship Management

for i in range(len(stname)):
    lst=stname[i].split(' ')
    # Ponderation by structure of strategy (3 points)
    wei1=0
    if (strul[i][0])=="VERB" or (strul[i][0])=="NOUN":
         wei1=1
    if (strul[i][0])=="NOUN VERB" or (strul[i][0])=="VERB NOUN":
        wei1=2
    if (strul[i][0])=="NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB": 
        wei1=3 
    # Verification of TRADING, DEALING and CRM heuriatic rules validation and ponderation, 9 points as maximun (TOTAL POINTS = 12)
    wei2=0
    if len([val for val in TRADING if val in lst]) > 0:
        strul[i].append("TRADING")
        wei2=wei2+len([val for val in TRADING if val in lst])*3
    if len([val for val in DEALING if val in lst]) > 0:
        strul[i].append("DEALING")
        wei2=wei2+len([val for val in DEALING if val in lst])*3
    if len([val for val in CRM if val in lst]) > 0:
        strul[i].append("CRM")
        wei2=wei2+len([val for val in CRM if val in lst])*3
    wei=wei1+wei2
    weight=wei/12
    ## DATABASE UPDATING
    if not stname[i] in hrul:
        cursor.execute(sql, (stname[i],weight))
        conexion.commit()
conexion.close()