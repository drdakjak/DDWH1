
import pandas as pd
import numpy as np
import requests
import json
import urllib
import re
import time
from IPython.display import display, HTML

comments_a = []

data = pd.read_excel('',sheetname='E3')

for i in range(10):
    if(len(data['Zdůvodnění '+str(i)].values)> 10):
        comments_a.extend(data['Zdůvodnění '+str(i)].values)

comments_a = list(np.unique(comments_a))

comments_rs = random.sample(comments_a,300)

for i in range(11):
    print(data[data['Název']=='The agency/structure dilemma : a coordination solution']['Zdůvodnění '+str(i)].values)

comments = []

comments.append(['Publikace je mimo okruh mé specializace, nehodnotím.',1])
comments.append(['Publikace je mimo dosah mé odborné specializace',1])
comments.append(['Knihu nemohu hodnotit, neboť jsem jejím spoluatorem a editorem.',2])
comments.append([ 'Hodnocení nebylo možno provést vzhledem k nedostatku poskytnutých podkladů. ',3])
comments.append(['Publikace je mimo okruh mé specializace, nehodnotím.',1])
comments.append(['Publikace je mimo okruh mé specializace, nehodnotím.',1])
comments.append(['Publikace je mimo dosah mé specilizace, nemohu hodnotit.',1])
comments.append(['Nemohu hodnotit. Je to mimo můj obor.',1])
comments.append(['Publikace je mimo dosah mé specializace',1])
comments.append(['Mimo můj obor.',1])
comments.append(['Publikace je mimo dosah mé specilizace, nemohu hodnotit.',1])
comments.append(['Publikace je mimo okruh mé specializace, nehodnotím.',1])
comments.append(['Nemohu hodnotit, nemám kvalifikaci v tomto oboru.',1])
comments.append(['Je to mimo moji kvalifikaci.',1])
comments.append(['Publikace je mimo dosah mé odborné specializace',1])
comments.append(['není dostatek podkladů pro hodnocení.',3])
comments.append(['Nemám dostatek podkladů pro hodnocení. ',1])
comments.append(['Hodnocení nebylo možno provést vzhledem k nedostatku poskytnutých podkladů. ',3])
comments.append(['Nemohu hodnotit, téma je mimo mou kvalifikaci.',1])
comments.append(['Publikace je mimo dosah mé odborné specializace',1])
comments.append(['Mimo můj obor- nehodnotím.',1])
comments.append(['není dostatek podkladů pro hodnocení',3])
comments.append(['Publikace je mimo okruh mé specializace, nehodnotím.',1])
comments.append(['Publikace je mimo okruh mé specializace.',1])
comments.append(['Hodnocení této práce se vymyká mému odbornému zaměření.',1])
comments.append(['Práce je zcela mimo mé odborné zaměření.',1])
comments.append(['Práce je mimo moji kvalifikaci.',1])
comments.append(['Publikace je mimo dosah mé odborné specializace',1])
comments.append(['Výstup je mimo moji vědeckou kvalifikaci.',1])
comments.append(['Práce je mimo dosah mé odborné specializace',1])
comments.append(['Publikace je mimo okruh mé specializace, nehodnotím.',1])
comments.append(['Mimo můj obor.',1])
comments.append(['Publikace je mimo okruh mé specializace.',1])
comments.append(['Práce je mimo dosah mé odborné specializace',1])
comments.append(['Jsem spoluautorkou - konflikt zájmů, nemohu tedy posuzovat.',2])
comments.append(['Jsem spoluautorkou- nemohu hodnotit..',2])
comments.append([ 'Hodnocení nebylo možno provést vzhledem k nedostatku poskytnutých podkladů. ',3])
comments.append([ 'Hodnocení nebylo možno provést vzhledem k nedostatku poskytnutých podkladů. ',3])
comments.append(['Nedostatek materialu. ',3])
comments.append(['Jsem zaujatý, protože už mnoho let spolupracuji s autorem knihy.',2])
comments.append(['Nedostatek materialu',3])
comments.append([ 'Hodnocení nebylo možno provést vzhledem k nedostatku poskytnutých podkladů.',3])
comments.append([' Nehodnotím, jsem autorem.',2])
comments.append(['Není na základě čeho hodnotit. Žádné posudky nejsou k tomuto výsledku v systému k dispozici. ',3])
comments.append(['The book is not available.',3])
comments.append(['Not available.',3])
comments.append(['Publikace není dostupná fyzicky ani elektronicky. ',3])
comments.append(['The book is not available.',3])
comments.append(['Book not available',3])
comments.append(['The book is missing.',3])
comments.append(['Nothing available - text, reviews, citations ...',3])
comments.append(['Not available.',3])
comments.append(['Není k dispozici k hodnocení.',3])
comments.append(['není na základě čeho provésti evaluaci...',3])
comments.append(['The book is not available.',3])
comments.append(['Publikace není dostupná fyzicjy ano elektronicky.',3])
comments.append(['The book is not available.',3])
comments.append(['Book was not available',3])
comments.append(['Book was not available',3])
comments.append(['The text is not available.',3])
comments.append(['text unavailable...',3])
comments.append(['It is not available.',3])
comments.append(['text not available',3])
comments.append(['Publication is not available.',3])
comments.append(['Text není k dispozici, ani odborné posudky.',3])
comments.append(['The text is not available.',3])
comments.append(['The result is not available.',3])
comments.append(['The book is not available.',3])
comments.append(['The result is not available.',3])
comments.append(['I cooperate with authors in submitting organisation. ',2])
comments.append(['unable to judge',1])
comments.append(['conflict of interest - faculty collegue...',2])
comments.append([ 'This is too far from my scope of expertise to allow me to make an evaluation.',2])
comments.append([ 'The topic is too far from my professional focus. In accordance to the journal, where the article is published - suggested A. (Impact Factor: 0.8)',2])
comments.append(['Kniha ani případné posudky nejsou k dispozici.',3])
comments.append(['I cooperate with the authors in submitting organisation.',2])
comments.append(['Conflict of interest', 2])
comments.append(['Different research field. ',1])
comments.append(['conflict of interest',2])
comments.append(['2nd decile IF journal; I have a conflict of interest.',2])
comments.append(['I have a conflict of interest.',2])

c123 = [c[0] for c in comments]

cnt=0
for c_rs in comments_rs:
    if(not c_rs in c123):
        cnt +=1
        comments.append([c_rs,4])
    if(cnt==100):
        break

comments = random.sample(comments,len(comments))

import string
intab = ".,-:()"
outtab = "      "
trantab = str.maketrans(intab, outtab)
words = []
for comm in comments:
    comm[0] = comm[0].translate(trantab).lower()
    if(comm[1]!=4):
        words += comm[0].split(' ')


words_set = np.unique(words)

len(words_set)

df_data = pd.DataFrame(comments,columns=['comment','label'])

for word in words_set:
    df_data[word]=df_data['comment'].apply(lambda s: 1 if s.split(' ').count(word)>0 else 0)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def get_numpy_matrix(data, features ,label):
    return data[features].as_matrix(),data['label'].as_matrix()

features = df_data.columns.get_values()
features = np.delete(features,[0,1,2])

train_data, train_label = get_numpy_matrix(df_data,features,'label')

print('Počet trénovacích dat:',len(df_data))
print('Počet trénovacích dat pro třídu "Mimo kvalifikaci":',len(df_data[df_data['label']==1]))
print('Počet trénovacích dat pro třídu "Střed zájmů":',len(df_data[df_data['label']==2]))
print('Počet trénovacích dat pro třídu "Nedostupné materiály":',len(df_data[df_data['label']==3]))

from sklearn import cross_validation

lr_model = LogisticRegression(C=3.2).fit(train_data,train_label)
svm_model = SVC(C=1.8,kernel='linear').fit(train_data,train_label)

scores_lr = cross_validation.cross_val_score(lr_model, train_data, train_label, cv=10)
scores_svm = cross_validation.cross_val_score(svm_model, train_data, train_label, cv=10)
print("Průměrná accuracy logistické regrese:",scores_lr.mean())
print("Průměrná accuracy SVM:",scores_svm.mean())

classes = ['Mimo kvalifikaci','Střet zájmů','Nedostupné']
for l in range(3):
    print(classes[l])
    for i in range(5):
        print('   ', i+1,features[np.argsort(lr_model.coef_[l])[::-1][i]],'  ',features[np.argsort(svm_model.coef_[l])[::-1][i]])


