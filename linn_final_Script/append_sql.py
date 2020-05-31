
''' Following script is used for appending the linneaous output into a SQL database'''
''' Developer Nitin k.chauhan v1.0 ''' 

import re
import os
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import mysql.connector
import sys
import base64
#from PIL import Image



def insertclass(id,Entity,Document,Start,End,Text,Context):
    print("Inserting into linn table") #change name of table
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='output_sample4k',
                             user='chemdb',
                             password='Scis@123')
        cursor = connection.cursor(prepared=True)
        sql_insert_blob_query = "INSERT INTO linn(id,Entity,Document,Start,End,Text,Context) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        # Convert data into tuple format
        insert_blob_tuple = (id,Entity,Document,Start,End,Text,Context)
        result  = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print (" file inserted successfully  table", result)
    except mysql.connector.Error as error :
   #     connection.rollback()
        print("Failed inserting  data into MySQL table {}".format(error))
   # finally:
        #if(connection.is_connected()):
        #   cursor.close()
        #   connection.close()
  #      print("MySQL connection is closed")

#path="/home/acer/jnudatadepot/mini/db/data/"
#files=os.listdir(path)
#for i in files:
#    id = i
#    abspath=(path+i+"/")
#    images=os.listdir(path+i+"/")
#    for z in images:
#        if str(z).endswith('.xml') == False:
#            z=abspath+str(z)
#            insertclass(i,z)
            #image = Image.open(str(z))

#image = Image.open('')
#blob_value = open('', 'rb').read()
#sql = 'INSERT INTO images(images) VALUES(%s)'    
#args = (blob_value, )
#cursor=db.cursor()
#cursor.execute(sql,args)

#sql1='select * from img'
#db.commit()
#cursor.execute(sql1)
#data=cursor.fetchall()
#print type(data[0][0])
#file_like=cStringIO.StringIO(data[0][0])
#img=PIL.Image.open(file_like)
#img.show()
#db.close()         


foin=open(sys.argv[1],'r')
count=0
for i in foin:
    i=i.strip()
    word=i.split('\t')
    if len(word)>=5:
        Entity,Document,Start,End,Text,Context=word[0],word[1],word[2],word[3],word[4],word[-1]
        count=count+1
        ids=count
        #print(ids,Entity,Document,Start,End,Text,Context)
        insertclass(ids,Entity,Document,Start,End,Text,Context)

#CREATE DATABASE output_sample4k;
#USE output_sample4k;
#CREATE TABLE IF NOT EXISTS linn(Id INT AUTO_INCREMENT PRIMARY KEY, Entity VARCHAR(255) NOT NULL, Document VARCHAR(255) NOT NULL, Start INT NOT NULL, End INT NOT NULL, Text VARCHAR(255) NOT NULL, Context MEDIUMTEXT NOT NULL);
#grant insert on output_sample4k.* to chemdb;
