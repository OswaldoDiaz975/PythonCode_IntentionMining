<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_candidate.strategy_name FROM  public.strategy_candidate")
lstrategies=cursor.fetchall()
strategies = list(itertools.chain.from_iterable(lstrategies))
cursor.execute("SELECT strategy_qel.strategy_name FROM  public.strategy_qel")
lstlog=cursor.fetchall()
stlog = list(itertools.chain.from_iterable(lstlog))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_rule(strategy_num, strategy_name, rule_name) VALUES (%s,%s,%s)"""
## MERGE THE KNOWLEDGEBASE STRATEGIES AND THE QUALITY EVENT LOG STRATEGIES
#Knowledge base strategies are processed in compliance with the sentence structure rule
num=0
for i in strategies:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
# Quality Event Log strategies are processed in compliance with the sentence structure rule
for i in stlog:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
    rul_name=[]
=======
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_candidate.strategy_name FROM  public.strategy_candidate")
lstrategies=cursor.fetchall()
strategies = list(itertools.chain.from_iterable(lstrategies))
cursor.execute("SELECT strategy_qel.strategy_name FROM  public.strategy_qel")
lstlog=cursor.fetchall()
stlog = list(itertools.chain.from_iterable(lstlog))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_rule(strategy_num, strategy_name, rule_name) VALUES (%s,%s,%s)"""
## MERGE THE KNOWLEDGEBASE STRATEGIES AND THE QUALITY EVENT LOG STRATEGIES
#Knowledge base strategies are processed in compliance with the sentence structure rule
num=0
for i in strategies:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
# Quality Event Log strategies are processed in compliance with the sentence structure rule
for i in stlog:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
    rul_name=[]
>>>>>>> 6eda7405585fe860ddc2a3aa35bd8a5f0a597e5e
=======
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_candidate.strategy_name FROM  public.strategy_candidate")
lstrategies=cursor.fetchall()
strategies = list(itertools.chain.from_iterable(lstrategies))
cursor.execute("SELECT strategy_qel.strategy_name FROM  public.strategy_qel")
lstlog=cursor.fetchall()
stlog = list(itertools.chain.from_iterable(lstlog))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_rule(strategy_num, strategy_name, rule_name) VALUES (%s,%s,%s)"""
## MERGE THE KNOWLEDGEBASE STRATEGIES AND THE QUALITY EVENT LOG STRATEGIES
#Knowledge base strategies are processed in compliance with the sentence structure rule
num=0
for i in strategies:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
# Quality Event Log strategies are processed in compliance with the sentence structure rule
for i in stlog:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
    rul_name=[]
>>>>>>> 6eda7405585fe860ddc2a3aa35bd8a5f0a597e5e
=======
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_candidate.strategy_name FROM  public.strategy_candidate")
lstrategies=cursor.fetchall()
strategies = list(itertools.chain.from_iterable(lstrategies))
cursor.execute("SELECT strategy_qel.strategy_name FROM  public.strategy_qel")
lstlog=cursor.fetchall()
stlog = list(itertools.chain.from_iterable(lstlog))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_rule(strategy_num, strategy_name, rule_name) VALUES (%s,%s,%s)"""
## MERGE THE KNOWLEDGEBASE STRATEGIES AND THE QUALITY EVENT LOG STRATEGIES
#Knowledge base strategies are processed in compliance with the sentence structure rule
num=0
for i in strategies:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
# Quality Event Log strategies are processed in compliance with the sentence structure rule
for i in stlog:
    rul_name=[]
    num+=1
    st=i.split(" ")
    if len(st)==1:
        rul_name.append("VERB")
    if len(st)==2:
        rul_name.append("NOUN VERB")
    if len(st)==3:
        rul_name.append("NOUN VERB NOUN / ADEJCTIVE NOUN VERB / NOUN VERB ADVERB")
    ## DATABASE UPDATING
    cursor.execute(sql, (num, i, rul_name))
    conexion.commit()
    rul_name=[]
>>>>>>> 6eda7405585fe860ddc2a3aa35bd8a5f0a597e5e
conexion.close()