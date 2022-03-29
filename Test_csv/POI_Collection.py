# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:07:08 2022

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
     _id:string #nome POI
    code_device:integer
    accessPOI:[
        {
            Data_Hour_access_POI:Timestamp
        },
        ...
        ]
}
"""

import csv
import json


listObj = [] #array dove viene salvata ogni nuovo POI
listaAccess = [] #array dove viene salvata ogni accesso al POI selezionato

with open("Test_dati_POI.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    id_POI=''
    code_device=''
    Data_Hour_access_POI=''
    POI=''
    
    #Ordino il file csv in odine dalle A-Z per POI, per data ed infine per orario
    for row in csv_reader:
        
        if row[0] != id_POI:#capisco se ho nuovo POI
            
            if listaAccess: #true se la lista ha elementi e quindi ha registrato almeno un accesso al POI
            
                #ora carico tutti gli accessi effettuati a questo POI 
    
                #carico il nuovo POI con tutti i suoi accessi
                POI={'_id': id_POI,'code_device':code_device, 'Info_access':listaAccess }
                listObj.append(POI)
                listaAccess=[]  #svuoto la lista di accessi
                
                
                
            #dato che ho nuovo POI, mi salvo subito la variabile
            id_POI=row[0]
            
            #registro poi il codice del device utilizzato 
            code_device=row[3]
                
            
            
            
            
        
        #registro tutti gli accessi affettuati in questo POI
        # formato per datatime "$date": "2014-05-02T13:22:55.000Z"
       
        DataFormat=row[1]+"T"+row[2]+".000Z"
        print(DataFormat)
        DataFormat1={'$date': DataFormat}
        Data_Hour_access_POI={'Data_Hour_access_POI': DataFormat1}
        listaAccess.append(Data_Hour_access_POI)
            
        
    
     
#carico ultimo POI con relativa lista accessi
POI={'_id': id_POI,'code_device':code_device, 'Info_access':listaAccess }
listObj.append(POI)

     
      
s = json.dumps(listObj)     
open("POI_collection.json","w").write(s) 