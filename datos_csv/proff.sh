#!/bin/bash


#for i in {0..1}
#do
mongoexport -u 'ricardo' -p 'rcancar' --authenticationDatabase 'admin' --db users --collection users --type=csv  --out  userspre.csv --fields update_id,user_id,user_age,Sexo,Codigo_sexo,analisis
#done


mongoexport -u 'ricardo' -p 'rcancar' --authenticationDatabase 'admin' --db song --collection regueton --type=csv  --out  regueton.csv --fields _id,Name_song,Genero,Artista,user_id,user_age,analisis,valid,Lyrics

mongoexport -u 'ricardo' -p 'rcancar' --authenticationDatabase 'admin' --db song --collection pop --type=csv  --out  pop.csv --fields _id,Name_song,Genero,Artista,user_id,user_age,analisis,valid,Lyrics

mongoexport -u 'ricardo' -p 'rcancar' --authenticationDatabase 'admin' --db song --collection romantica --type=csv  --out  romantica.csv --fields _id,Name_song,Genero,Artista,user_id,user_age,analisis,valid,Lyrics
