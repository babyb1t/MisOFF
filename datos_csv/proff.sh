#!/bin/bash


#for i in {0..1}
#do
mongoexport  --db users --collection users --type=csv  --out  userspre.csv --fields update_id,user_id,user_age,Sexo,Codigo_sexo,analisis
#done


mongoexport  --db song --collection regueton --type=csv  --out  raw_regueton.csv --fields _id,Name_song,Genero,Artista,user_id,user_age,analisis,valid,Lyrics

mongoexport  --db song --collection pop --type=csv  --out  raw_pop.csv --fields _id,Name_song,Genero,Artista,user_id,user_age,analisis,valid,Lyrics

mongoexport  --db song --collection romantica --type=csv  --out  raw_romantica.csv --fields _id,Name_song,Genero,Artista,user_id,user_age,analisis,valid,Lyrics


mongoexport  --db song --collection pop_es --type=csv  --out  raw_pop_es.csv --fields _id,Name_song,Genero,Artista,user_id,user_age,analisis,valid,Lyrics

mongoexport  --db song --collection allsongs --type=csv  --out  allsongs.csv --fields _id,estrofa
