import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="phd1522")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT sentences.doc_id FROM  public.sentences ORDER BY doc_id, sentence_id")
ldoc=cursor.fetchall()
doc = list(itertools.chain.from_iterable(ldoc))
cursor.execute("SELECT sentences.sentence_id FROM  public.sentences ORDER BY doc_id, sentence_id")
lsentence=cursor.fetchall()
sentence = list(itertools.chain.from_iterable(lsentence))
cursor.execute("SELECT sentences.pos_tags FROM  public.sentences ORDER BY doc_id, sentence_id")
lpos=cursor.fetchall()
pos = list(itertools.chain.from_iterable(lpos))
## SQL COMMANDS SPECIFICATION
pg_update = """Update sentences set ner_tags = %s where doc_id = %s and sentence_id = %s"""
## NER (Named Entity Recognition) TAGGING OF SENTENCES
k=0
for i in pos:
  ner=[]
  for j in i:
    neri='OTHER'
    if j=='VB' or j=='VBD' or j=='VBG' or j=='VBN' or j=='VBP' or j=='VBZ':
      neri='VERB'
    elif j=='NN' or j=='NNS':
      neri='NOUN'
    elif j=='JJ':
      neri='ADJECTIVE'
    elif j=='JJR':
      neri='ADJECTIVE COMPARATIVE'
    elif j=='JJS':
      neri='ADJECTIVE SUPERLATIVE'
    elif j=='RB':
      neri='ADVERB'
    elif j=='RBR':
      neri='ADVERB COMPARATIVE'
    elif j=='RBS':
      neri='ADVERB SUPERLATIVE'
    ner.append(neri)
  ## DATABASE UPDATING
  cursor.execute(pg_update, (ner, doc[k],sentence[k]))
  k=k+1
  conexion.commit()
conexion.close()