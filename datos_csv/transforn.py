#!/bin/python

import csv
import json

def CSV(codigo_parrafo,grado,name):
        with open("userspre.csv") as f1:
          reader = csv.reader(f1, delimiter=',')#, quotechar='') 
          i = 0
          f = csv.writer(open(name, "w+"))
          f.writerow(["user_id","user_age","Sexo","codigo_sexo","nombre_cancion","Codigo_cancion",codigo_parrafo,grado,"parrafos"])
                   #"texto_parrafo_estereotipo","codigo_parrafo_roles","Grado_roles","texto_parrafo_roles","codigo_parrafo_poder",\
                   #"Grado_poder","texto_parrafo_poder","codigo_parrafo_cuerpo","Grado_cuerpo","texto_parrafo_cuerpo", 
                   #"Pregunta_general","Grado_general"])
          
          for row in reader:# Number of rows including the death rates 
             data =[]
             
             for col in range(1,5): # The columns I want read   B and D
               data.append(row[col])
             if i > 0:
          
              x = row[5]
              x= json.loads(x)
              
              #print(data)

            # Write CSV Header, If you dont need that, remove this line
            
              
              for x in x:
               j = 0 
               if x[codigo_parrafo] == 0:
                 x[codigo_parrafo] = [0]
               for k in x[codigo_parrafo]:
               
                if  j == 0:
                  
                  f.writerow([data[0],data[1],data[2],data[3],x["name"],x["Codigo_cancion"],k,x[grado]])
                if  j > 0:
                  f.writerow(['','','','','','',k])  
                            #x["Grado_estereotipo"],x["texto_parrafo_estereotipo"],x["codigo_parrafo_roles"],x["Grado_roles"],\
                            #x["texto_parrafo_roles"],x["codigo_parrafo_poder"],x["Grado_poder"],x["texto_parrafo_poder"],\
                            #x["codigo_parrafo_cuerpo"],x["Grado_cuerpo"],x["texto_parrafo_cuerpo"],x["Pregunta_general"],\
                            #x["Grado_general"]])
                j+=1  
             i+=1

def gen(codigo,grado,name):
   with open("userspre.csv") as f1:
          reader = csv.reader(f1, delimiter=',')#, quotechar='') 
          i = 0
          f = csv.writer(open(name, "w+"))
          f.writerow(["user_id","user_age","Sexo","codigo_sexo","nombre_cancion","Codigo_cancion",codigo,grado])
                   #"texto_parrafo_estereotipo","codigo_parrafo_roles","Grado_roles","texto_parrafo_roles","codigo_parrafo_poder",\
                   #"Grado_poder","texto_parrafo_poder","codigo_parrafo_cuerpo","Grado_cuerpo","texto_parrafo_cuerpo", 
                   #"Pregunta_general","Grado_general"])
        
          for row in reader:# Number of rows including the death rates 
             data =[]
             
             for col in range(1,5): # The columns I want read   B and D
               data.append(row[col])
             if i > 0:
          
              x = row[5]
              x= json.loads(x)
              
              #print(data)

            # Write CSV Header, If you dont need that, remove this line
            
              
              for x in x:
                  
               
                  
                  f.writerow([data[0],data[1],data[2],data[3],x["name"],x["Codigo_cancion"],x[codigo],x[grado]])
               
                 
             i+=1

def main():
  try:
     risk = open('userspre.csv', 'r', encoding="UTF-8").read() #find the file

  except:
      while risk != "userspre.csv":  # if the file cant be found if there is an error
        print("Could not open", risk, "file")
        risk = input("\nPlease try to open file again: ")
  else:
      with open("userspre.csv") as f1:
        reader = csv.reader(f1, delimiter=',')#, quotechar='')
        CSV("codigo_parrafo_estereotipo","Grado_estereotipo","Parrafos_estereotipo.csv")
        CSV("codigo_parrafo_roles","Grado_roles","Parrafos_roles.csv")
        CSV("codigo_parrafo_poder","Grado_poder","Parrafos_poder.csv")
        CSV("codigo_parrafo_cuerpo","Grado_cuerpo","Parrafos_cuerpo.csv")
        gen("Pregunta_general","Grado_general","Parrafos_general.csv")
        
   
if __name__=='__main__':
  main()
