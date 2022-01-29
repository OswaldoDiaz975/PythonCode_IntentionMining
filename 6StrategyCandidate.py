<<<<<<< HEAD
<<<<<<< HEAD
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_mention.mention_text FROM  public.strategy_mention")
lmentions=cursor.fetchall()
mentions = list(itertools.chain.from_iterable(lmentions))
cursor.execute("SELECT sentences.ner_tags FROM  public.sentences ORDER BY doc_id, sentence_id")
lnertags=cursor.fetchall()
nertags = list(itertools.chain.from_iterable(lnertags))
cursor.execute("SELECT sentences.lemmas FROM  public.sentences ORDER BY doc_id, sentence_id")
llemmas=cursor.fetchall()
lemmas= list(itertools.chain.from_iterable(llemmas))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_candidate(strategy_id, strategy_name) VALUES (%s,%s)"""
## EXTRACTING STRATEGIES ACCORDING THE ENGLISH SENTENCES STRUCTURES:
## "VERB"
## "NOUN" + "VERB"
## "ADJECTIVE" + "NOUN" + "VERB"
## "NOUN" + "VERB" + "ADVERB"
s=1
rul_id=""
for i in range(len(lemmas)):
	mentiont=mentions[i].split(" ")
	nertagst=nertags[i]
	lemmast=lemmas[i]
	nert=""
	for j in range(len(lemmast)):
		if (lemmast[j] in mentiont):
			nert+=" "+nertagst[j]
	nerst=nert[1:].split(" ")
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="VERB" and j<len(mentiont):
			st_name=str(mentiont[j].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="NOUN" and j+1<len(nerst) and nerst[j+1]=="VERB" and j+1<len(mentiont) and j<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="ADJECTIVE" and j+1<len(nerst) and nerst[j+1]=="NOUN" and j+2<len(nerst) and nerst[j+2]=="VERB" and j+2<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())+" "+str(mentiont[j+2].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1			
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="NOUN" and j+1<len(nerst) and nerst[j+1]=="VERB" and j+2<len(nerst) and nerst[j+2]=="ADVERB" and j+2<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())+" "+str(mentiont[j+2].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1	
=======
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_mention.mention_text FROM  public.strategy_mention")
lmentions=cursor.fetchall()
mentions = list(itertools.chain.from_iterable(lmentions))
cursor.execute("SELECT sentences.ner_tags FROM  public.sentences ORDER BY doc_id, sentence_id")
lnertags=cursor.fetchall()
nertags = list(itertools.chain.from_iterable(lnertags))
cursor.execute("SELECT sentences.lemmas FROM  public.sentences ORDER BY doc_id, sentence_id")
llemmas=cursor.fetchall()
lemmas= list(itertools.chain.from_iterable(llemmas))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_candidate(strategy_id, strategy_name) VALUES (%s,%s)"""
## EXTRACTING STRATEGIES ACCORDING THE ENGLISH SENTENCES STRUCTURES:
## "VERB"
## "NOUN" + "VERB"
## "ADJECTIVE" + "NOUN" + "VERB"
## "NOUN" + "VERB" + "ADVERB"
s=1
rul_id=""
for i in range(len(lemmas)):
	mentiont=mentions[i].split(" ")
	nertagst=nertags[i]
	lemmast=lemmas[i]
	nert=""
	for j in range(len(lemmast)):
		if (lemmast[j] in mentiont):
			nert+=" "+nertagst[j]
	nerst=nert[1:].split(" ")
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="VERB" and j<len(mentiont):
			st_name=str(mentiont[j].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="NOUN" and j+1<len(nerst) and nerst[j+1]=="VERB" and j+1<len(mentiont) and j<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="ADJECTIVE" and j+1<len(nerst) and nerst[j+1]=="NOUN" and j+2<len(nerst) and nerst[j+2]=="VERB" and j+2<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())+" "+str(mentiont[j+2].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1			
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="NOUN" and j+1<len(nerst) and nerst[j+1]=="VERB" and j+2<len(nerst) and nerst[j+2]=="ADVERB" and j+2<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())+" "+str(mentiont[j+2].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1	
>>>>>>> 6eda7405585fe860ddc2a3aa35bd8a5f0a597e5e
=======
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_mention.mention_text FROM  public.strategy_mention")
lmentions=cursor.fetchall()
mentions = list(itertools.chain.from_iterable(lmentions))
cursor.execute("SELECT sentences.ner_tags FROM  public.sentences ORDER BY doc_id, sentence_id")
lnertags=cursor.fetchall()
nertags = list(itertools.chain.from_iterable(lnertags))
cursor.execute("SELECT sentences.lemmas FROM  public.sentences ORDER BY doc_id, sentence_id")
llemmas=cursor.fetchall()
lemmas= list(itertools.chain.from_iterable(llemmas))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_candidate(strategy_id, strategy_name) VALUES (%s,%s)"""
## EXTRACTING STRATEGIES ACCORDING THE ENGLISH SENTENCES STRUCTURES:
## "VERB"
## "NOUN" + "VERB"
## "ADJECTIVE" + "NOUN" + "VERB"
## "NOUN" + "VERB" + "ADVERB"
s=1
rul_id=""
for i in range(len(lemmas)):
	mentiont=mentions[i].split(" ")
	nertagst=nertags[i]
	lemmast=lemmas[i]
	nert=""
	for j in range(len(lemmast)):
		if (lemmast[j] in mentiont):
			nert+=" "+nertagst[j]
	nerst=nert[1:].split(" ")
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="VERB" and j<len(mentiont):
			st_name=str(mentiont[j].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="NOUN" and j+1<len(nerst) and nerst[j+1]=="VERB" and j+1<len(mentiont) and j<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="ADJECTIVE" and j+1<len(nerst) and nerst[j+1]=="NOUN" and j+2<len(nerst) and nerst[j+2]=="VERB" and j+2<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())+" "+str(mentiont[j+2].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1			
	for j in range(len(nerst)):
		st_id="S"+str(s)
		st_name=""
		if nerst[j]=="NOUN" and j+1<len(nerst) and nerst[j+1]=="VERB" and j+2<len(nerst) and nerst[j+2]=="ADVERB" and j+2<len(mentiont):
			st_name=str(mentiont[j].lower())+" "+str(mentiont[j+1].lower())+" "+str(mentiont[j+2].lower())
		if st_name!="" and len(st_name)>1 and st_name[0]!="'" and st_name[0]!="."and st_name[0]!='"':
    		## DATABASE UPDATING
			cursor.execute(sql, (st_id, st_name))
			conexion.commit()
			s+=1	
>>>>>>> 6eda7405585fe860ddc2a3aa35bd8a5f0a597e5e
conexion.close()