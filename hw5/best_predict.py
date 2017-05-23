import pandas as pd
import math
import numpy as np
import sys
import os

tag_list = [
        "SCIENCE-FICTION",
        "SPECULATIVE-FICTION",
        "FICTION",
        "NOVEL",
        "FANTASY",
        "CHILDREN'S-LITERATURE",
        "HUMOUR",
        "SATIRE",
        "HISTORICAL-FICTION",
        "HISTORY",
        "MYSTERY",
        "SUSPENSE",
        "ADVENTURE-NOVEL",
        "SPY-FICTION",
        "AUTOBIOGRAPHY", "HORROR",
        "THRILLER",
        "ROMANCE-NOVEL",
        "COMEDY",
        "NOVELLA",
        "WAR-NOVEL",
        "DYSTOPIA",
        "COMIC-NOVEL",
        "DETECTIVE-FICTION",
        "HISTORICAL-NOVEL",
        "BIOGRAPHY",
        "MEMOIR",
        "NON-FICTION",
        "CRIME-FICTION",
        "AUTOBIOGRAPHICAL-NOVEL",
        "ALTERNATE-HISTORY",
        "TECHNO-THRILLER",
        "UTOPIAN-AND-DYSTOPIAN-FICTION",
        "YOUNG-ADULT-LITERATURE",
        "SHORT-STORY",
        "GOTHIC-FICTION",
        "APOCALYPTIC-AND-POST-APOCALYPTIC-FICTION",
        "HIGH-FANTASY"]


assert len(tag_list)==38
num = 6
df = []
files = [ 'rnn1.csv', 'rnn2.csv', 'bog1.csv', 'bog2.csv', 'best1.csv', 'best2.csv' ]

for i, f in enumerate(files):
    df.append( pd.read_csv(os.path.join('CSVs',f)) )
    df[i].fillna("fuck", inplace=True)


pred = []
ln = len(df[0])
for i in range(ln):
    dic = {}
    for tag in tag_list: dic[tag] = 0

    for j in range(num):
        fuck = (df[j]["tags"][i])
        if fuck=="fuck": continue
        x =  df[j]["tags"][i].split(' ')
        for xx in x: dic[xx] += 1

    labels = []
    dic_keys = []
    dic_values = []
    for xx in dic.keys():
        dic_keys.append( xx )
        dic_values.append( dic[xx] )

        '''
        if "FICTION" in xx:
            if dic[xx] >= 6:
                labels.append( xx )
        else:
        '''
        if dic[xx] >= 3:
            labels.append( xx )

    if len(labels)==0:
        print("=.=")
        res =  dic_keys[ np.argmax(dic_values) ]
        print(res)
        dic_values[ np.argmax(dic_values) ] = 0
        labels.append(res)
        labels.append(dic_keys[ np.argmax(dic_values) ])

    pred.append( labels )

output_path = sys.argv[2]
with open(output_path,'w') as output:
    print ('\"id\",\"tags\"',file=output)
    for index,labels in enumerate(pred):
        assert len(labels)>0
        '''
        labels = [tag_list[i] for i,value in enumerate(labels) if value==1 ]
        if len(labels) == 0:
            labels.append( tag_list[ np.argmax(pred[index]) ] )
        '''
        labels_original = ' '.join(labels)
        print ('\"%d\",\"%s\"'%(index,labels_original),file=output)
