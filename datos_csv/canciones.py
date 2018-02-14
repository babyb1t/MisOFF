#!/bin/python

import csv
import json
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.song

def CSV(name):
          allsongs =db.allsongs
          f = csv.writer(open(name, "w+"))
          f.writerow(["Codigo_cancion","Numero de estrofa","Texo de estrofa"])
                
          total = allsongs.find().count()
          for row in range(0, total):# Number of rows including the death rates 
              
             #x= json.loads(x)
        
             
             for j in range(0,len(allsongs.find()[row]["estrofa"]) ):
               f.writerow([int(allsongs.find()[row]["_id"]),j,allsongs.find()[row]["estrofa"][j]])   
                
                      
             

def main():
  try:
     risk = open('allsongs.csv', 'r', encoding="UTF-8").read() #find the file

  except:
      while risk != "allsongs.csv":  # if the file cant be found if there is an error
        print("Could not open", risk, "file")
        risk = input("\nPlease try to open file again: ")
  else:
     CSV("todas_canciones.csv")     


if __name__ =='__main__':
  main()
       

