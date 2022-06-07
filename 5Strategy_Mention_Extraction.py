import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect(database="postgres", user="postgres", password="test")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT sentences.doc_id FROM  public.sentences ORDER BY doc_id, sentence_id")
ldoc=cursor.fetchall()
docid = list(itertools.chain.from_iterable(ldoc))
cursor.execute("SELECT sentences.sentence_id FROM  public.sentences ORDER BY doc_id, sentence_id")
lsentenceid=cursor.fetchall()
sentenceid = list(itertools.chain.from_iterable(lsentenceid))
cursor.execute("SELECT sentences.ner_tags FROM  public.sentences ORDER BY doc_id, sentence_id")
lnertags=cursor.fetchall()
ner_tags = list(itertools.chain.from_iterable(lnertags))
cursor.execute("SELECT sentences.lemmas FROM  public.sentences ORDER BY doc_id, sentence_id")
llemmas=cursor.fetchall()
lemmas= list(itertools.chain.from_iterable(llemmas))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO strategy_mention(mention_id, mention_text, doc_id, sentence_id, begin_index, end_index) VALUES (%s,%s,%s,%s,%s,%s)"""
## ELEMENTS OF STRATEGY MENTIONS : "VERB", "NOUN", "ADJECTIVE", "ADVERB", "ADVERB COMPARATIVE", 
## "ADJECTIVE COMPARATIVE", "ADJECTIVE SUPERLATIVE", "ADVERB SUPERLATIVE"
for i in range(len(sentenceid)):
	mention_text= ""
	begin_index=0
	nertags=ner_tags[i]
	end_index=len(nertags)-1
	lemma=lemmas[i]
	k=0
	for j in nertags:
		if begin_index<end_index and (j=="VERB" or j=="NOUN" or j=="ADJECTIVE" or j=="ADVERB" or j=="ADVERB COMPARATIVE"
		or j=="ADJECTIVE COMPARATIVE" or j=="ADJECTIVE SUPERLATIVE" or j=="ADVERB SUPERLATIVE"):
			if mention_text=="" and k!=0:
				begin_index=k
			mention_text=mention_text+" "+str(lemma[k])
		k+=1
	mention_id="M"+str(i+1)
	mentiont=mention_text[1:].split(" ")
	end_index=len(mentiont)-1
	## DATABASE UPDATING
	cursor.execute(sql, (mention_id, mention_text[1:], docid[i], sentenceid[i],begin_index, end_index))
	conexion.commit()
conexion.close()