import psycopg2
import itertools
import nltk
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="phd1522")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT sentences.doc_id FROM  public.sentences ORDER BY doc_id, sentence_id")
ldoc=cursor.fetchall()
doc = list(itertools.chain.from_iterable(ldoc))
cursor.execute("SELECT sentences.sentence_id FROM  public.sentences ORDER BY doc_id, sentence_id")
lsentenceid=cursor.fetchall()
sentenceid = list(itertools.chain.from_iterable(lsentenceid))
cursor.execute("SELECT sentences.lemmas FROM  public.sentences ORDER BY doc_id, sentence_id")
lsentencetx=cursor.fetchall()
sentencetx = list(itertools.chain.from_iterable(lsentencetx))
## SQL COMMANDS SPECIFICATION
pg_update = """Update sentences set pos_tags = %s where doc_id = %s and sentence_id = %s"""
## POS (Part Of Speech) TAGGING OF SENTENCES
l=0
for i in sentencetx:
    postag=nltk.pos_tag(i)
    pos=[]
    for j in postag:
        pos.append(j[1])
    ## DATABASE UPDATING
    cursor.execute(pg_update, (pos, doc[l],sentenceid[l]))
    conexion.commit()
    l+=1
conexion.close()