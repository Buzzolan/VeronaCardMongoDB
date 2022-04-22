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
    
    id_card:string
    activation:Date
    type:string
    	access:[
    		{	
    			POI_access:string
    			Data_access_VR:Date
    			Hour_access_VR:Time
    		}
    		]
}

"$date":"2003-03-26T10:50:57.240Z"
    
"""

import csv
import json


 

 

 

listObj = [] #array dove viene salvata ogni nuova tessera
listaAccess = [] #array dove viene salvata ogni strisciata che esegue un utente

with open("Dati2014ordinatifineDef.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    id_vr=''
    activation=''
    profile_type=''
    Data_access_vr=''
    Hour_access_vr=''
    card=''
    
    #le tessere sono ordinate per numero di tessera, poi per data e infine per ora
    for row in csv_reader:
        
        if row[4] != id_vr:#capisco se ho nuova id_card da registare
            
            if listaAccess: #true se la lista ha elementi e quindi ha registrato almeno un accesso
            
                #ora carico tutti gli accessi effettuati da questo utente 
                
                activation_format_date={'$date':activation}
    
                #carico la nuova tessera con tutti i suoi accessi
                card={'_id': id_vr,'activation':activation_format_date, 'type':profile_type, 'Info_access':listaAccess }
                listObj.append(card)
                listaAccess=[]  #svuoto la lista di accessi
                
                
                
            #dato che ho nuova card, mi salvo subito la variabile
            id_vr=row[4]
            
            #registro la data di attivazione e il tipo di profilo
            activation=row[5]
            profile_type=row[6]
                
            
            
            
            
        
        #registro tutti gli accessi affettuati con questa attivazione
        # formato per ora T10:50:57.240Z
       
        DataFormat=row[1]+"T"+row[2]+".000Z"
        print(DataFormat)
        Data_access_vr={'$date': DataFormat}
        POI={'POI':row[0] , 'Data_Hour_access':Data_access_vr }
        listaAccess.append(POI)
            
        
    
     
#carico ultima tessera con relativa lista accessi
activation_format_date={'$date':activation}
#carico la nuova tessera con tutti i suoi accessi
card={'_id': id_vr, 'activation':activation_format_date, 'type':profile_type, 'Info_access':listaAccess}
listObj.append(card)
     
      
s = json.dumps(listObj)     
open("CardCollection.json","w").write(s) 
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
