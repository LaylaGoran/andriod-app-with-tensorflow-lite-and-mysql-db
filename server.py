#start a connections fist and import the modlue 
import mysql.connector
#import the nessceary moudle
import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd


mydb=mysql.connector.connect( host='localhost' , port= '3306' , user= 'layla' , passwd='1234', db='ml' )

mycursor= mydb.cursor()






sql="SELECT class_name AS 'Image Label' \
     , COUNT(CASE WHEN img_use = 1 THEN img_label END) AS 'Training Images'\
     , COUNT(CASE WHEN img_use = 2 THEN img_label END) AS 'Testing Images'\
     FROM tf_images INNER JOIN categories ON class_idx = img_label \
     GROUP BY class_name"
result = ""

    


mycursor.execute(sql)
result = mycursor.fetchall()
 
query= pd.read_sql(sql,mydb)

print(query)
ax = query.plot.bar(rot=0)

for i in mycursor:
  print(i)