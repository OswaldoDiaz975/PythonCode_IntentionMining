import psycopg2
import itertools
import nltk
from nltk.stem import WordNetLemmatizer
## DATABASE CONNECTION AND CURSOR DEFINITION
conexion = psycopg2.connect("host='localhost' port='5432' dbname='postgres' user='postgres' password='test'")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT articles.doc_id FROM  public.articles ORDER BY doc_id")
ldoc=cursor.fetchall()
docid = list(itertools.chain.from_iterable(ldoc))
cursor.execute("SELECT articles.doc_text FROM  public.articles ORDER BY doc_id")
ldoc=cursor.fetchall()
doctext = list(itertools.chain.from_iterable(ldoc))
## SQL COMMANDS SPECIFICATION
sql="""INSERT INTO sentences(doc_id, sentence_id, sentence_text, tokens, lemmas, pos_tags, ner_tags) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
## PARSING OF ARTICLES AND TOKENIZING AND LEMMATIZING OF SENTENCES
nltk.download("wordnet", "F:/SML/Codigo/nltk_data/")
lmtzr = WordNetLemmatizer()
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
lemmatizer = WordNetLemmatizer()
articles = []
articles=doctext
sentences = []
token = []
lema = []
post = []
nert = []
for i in range(len(articles)):
    articles[i] = articles[i].replace(",",";")
for i in range(len(articles)):
    sentences += nltk.word_tokenize(articles[i])
for i in range(len(articles)):
    sentence = tokenizer.tokenize(articles[i])
    for j in range(len(sentence)):
        token = nltk.word_tokenize(sentence[j])
        for k in range(len(token)):
            lem=lmtzr.lemmatize(token[k])
            if lem == token[k]:
                lema.append(lmtzr.lemmatize(token[k],'v'))
            else:
                lema.append(lem)
        fila=(docid[i],"O"+str(j+1),sentence[j],token,lema,post,nert) 
        ## DATABASE UPDATING
        cursor.execute(sql, (fila))
        conexion.commit()
        lema=[]
conexion.close()