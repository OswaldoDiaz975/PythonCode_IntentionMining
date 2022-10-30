from re import I
import psycopg2
import itertools
## DATABASE CONNECTION AND CURSOR DEFINITION
# Particular business (sales) strategy log
conexion = psycopg2.connect(database="postgres", user="postgres", password="phd1522")
cursor=conexion.cursor()
## DATA RECUPERATION FROM DATABASE
cursor.execute("SELECT strategy_name FROM user_strategies")
lstname=cursor.fetchall()
stname = list(itertools.chain.from_iterable(lstname))
## Trading, Dealing and CRM relationship with sales business
CURRENT_SALES_STRATEGIES = ['billing customer sale','cancel customer order','complete customer order',
                            'customer service','deliver customer order','emit customer quotation',
                            'generate customer order','local stock control','home sale delivery',
                            'register sale','remote stock control','sales record']
TRADING = ['order', 'quotation', 'stock', 'sale', 'price']
DEALING = ['sell', 'buy', 'offer', 'promotion', 'billing', 'cancel']
CRM = ['customer', 'empathy', 'user', 'ecommerce', 'e-commerce', 'omnichannel', 'omni-channel'] ## Customer Relationship Management
## Computing of parameters
TP = 0 ## True Positive. Current sales strategies that also are user strategies
FP = 0 ## False Positive. User strategies that are not current sales strategies
FN = 0 ## False Negative. Current sales strategies that are not user strategies, this will never happen
TN = 0 ## True Negative. Strategies that are not current sales strategies and either are not user strategies
for i in range(len(stname)):
    lst=stname[i].split(' ')
    if stname[i] in CURRENT_SALES_STRATEGIES:
        TP=TP+1
    else: 
        if ((len(lst) == 1 and (len([val for val in TRADING if val in lst]) == 1 or 
            len([val for val in DEALING if val in lst]) == 1 or 
            len([val for val in CRM if val in lst]) == 1)) or
            (len(lst) == 2 and ((len([val for val in TRADING if val in lst]) == 2 or 
            len([val for val in DEALING if val in lst]) == 2 or 
            len([val for val in CRM if val in lst]) == 2) or 
            (len([val for val in TRADING if val in lst]) == 1 and len([val for val in DEALING if val in lst]) == 1) or
            (len([val for val in TRADING if val in lst]) == 1 and len([val for val in CRM if val in lst]) == 1) or
            (len([val for val in DEALING if val in lst]) == 1 and len([val for val in CRM if val in lst]) == 1))) or
            (len(lst)==3 and (len([val for val in TRADING if val in lst]) > 0 or 
            len([val for val in DEALING if val in lst]) > 0 or 
            len([val for val in CRM if val in lst]) > 0))):
            FP=FP+1
        else: 
            TN=TN+1
print('TP : ', TP)
print('FP : ', FP)
print('FN : ', FN)
print('TN : ', TN)
conexion.close()