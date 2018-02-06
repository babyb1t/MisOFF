#!/bin/python

import csv
import json

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

          i = 0
          f = csv.writer(open("users.csv", "w+"))
          f.writerow(["user_id","user_age","Sexo","codigo_sexo","nombre_cancion","Codigo_cancion","codigo_parrafo_estereotipo","Grado_estereotipo",\
                   "texto_parrafo_estereotipo","codigo_parrafo_roles","Grado_roles","texto_parrafo_roles","codigo_parrafo_poder",\
                   "Grado_poder","texto_parrafo_poder","codigo_parrafo_cuerpo","Grado_cuerpo","texto_parrafo_cuerpo", 
                     "Pregunta_general","Grado_general"])
        
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
                
                f.writerow([data[0],data[1],data[2],data[3],x["name"],x["Codigo_cancion"],x["codigo_parrafo_estereotipo"],\
                            x["Grado_estereotipo"],x["texto_parrafo_estereotipo"],x["codigo_parrafo_roles"],x["Grado_roles"],\
                            x["texto_parrafo_roles"],x["codigo_parrafo_poder"],x["Grado_poder"],x["texto_parrafo_poder"],\
                            x["codigo_parrafo_cuerpo"],x["Grado_cuerpo"],x["texto_parrafo_cuerpo"],x["Pregunta_general"],\
                            x["Grado_general"]])
            
             i+=1
if __name__=='__main__':
  main()
