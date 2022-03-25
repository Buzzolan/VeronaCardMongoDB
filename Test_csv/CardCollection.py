# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 17:51:07 2022

@author: tomma
Prendo in input un file csv e lo converto in json pronto per mongodb Compass.
Struttura del file CSV:
    Row[0]= POI
    Row[1]=Date '2014-12-30'
    Row[2]=time
    Row[3]=device
    Roe[4]=VeronaCard
    Row[5]=Data attivazione
    row[6]=profilo

Struttura intermedia:
    matrice= [{numero_card,attivazione,type,accessVR:[{Poi,data,time},{Poi,data,time},...]]
Struttura json che voglio in output:
{
    _id:veronacard Object
    activation:Date
    type:string
    accessVR:[
    	{	
    		POI_access:string
    		Data_access_VR:Date
    		Hour_access_VR:Time
    	}
    ]
}
    
"""

import csv
import json


 

 

 

listObj = []
listaAccess = []
POI1={'POI':'casaGiulietta', 'DataAcc':'01-12-11', 'hour':10 }
POI2={'POI':'casaGiulietta2', 'DataAcc':'01-12-112', 'hour':107}
listaAccess.append(POI1)
listaAccess.append(POI2)
with open("Test_dati1.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    id_vr=''
    activation=''
    profile_type=''
    Data_access_vr=''
    Hour_access_vr=''
    objectVR=''
    
    
    for row in csv_reader:
        #print(row)
        if row[4] != id_vr:
            id_vr= row[4]
            
            if listaAccess: #true se la lista ha elementi, allora carico quanto registrato fino ad ora
            
            
        
        
        
        
        dataTest=''
        dataTest={'$date': row[5]}
        card={'_id': row[4], 'activation': dataTest , 'type': row[6], 'accessVR':listaAccess}
        
        
        listObj.append(card)
        
      
s = json.dumps(listObj)     
open("prova2.json","w").write(s) 
'''        
        if row[4] != id_vr: #allora sono in una nuova riga con id ancora da registrare
            
            
            with open("prova1.json") as fp:
              listObj = json.load(fp)
              listObj.update({ 'id_vr': row[4]}) 
              json.dumps(listObj)
            
        #card={'id_vr': row[4]}
         #   s=json.dumps(card)

'''
#open("prova1.json","w").write(s) 


#d = {'alpha': 1,'beta': 2}
#s = json.dumps(d)
#type(d)
