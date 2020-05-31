
''' Following script is Generates the output of ChemdataExtractor into a TSV appends that into a SQL DATABASE '''
''' Developer Nitin k.chauhan v1.0 ''' 

from chemdataextractor import Document
import sys
import os
from prettytable import PrettyTable


def list_chemicals(foin):
    fchem=open(foin,'rb')
    docchem=Document.from_file(fchem)
    ct=0
    t = PrettyTable(['Filename','Entity_count','Start','End','Entity'])
    for i in docchem.cems:
        ct=ct+1
        t.add_row([foin,ct,i.start,i.end,i.text])
    t.align='l'
    t.border=False
    return(t)
    
#running over batch files/folder
for i in os.listdir(sys.argv[1]):
    fout=open('chemdb.csv','a') # if filename chemdb.csv not their then do create one 
    if i.endswith('nxml'): #can be changes based on input format
        fout.write(str(list_chemicals(str(sys.argv[1])+"/"+str(i))))


#mysql -u root -p
#CREATE DATABASE Test_images;
# USE Test_images;
#CREATE TABLE `images` ( `id` INT NOT NULL , `images` blob NOT NULL ));
#mysql -h localhost -u root -p 
#use Test_images;
#grant all privileges on Test_images to 'root'@'10.107.226.66';
#flush privileges;
#GRANT INSERT ON Test_images.images TO 'root'@'10.107.226.66';
#show FIELDS FROM images;

#import re
#import os
#import mysql.connector
#from mysql.connector import Error
#from mysql.connector import errorcode
#import mysql.connector
#import sys
#import base64
#from PIL import Image



def insertclass(id,filee):
    print("Inserting into test table")
    try:
        connection = mysql.connector.connect(host='10.107.226.66',
                             database='Test_images',
                             user='root',
                             password='scisjnu')
        cursor = connection.cursor(prepared=True)
        sql_insert_blob_query = """ INSERT INTO `images`
                          (`id`, `images`) VALUES (%s,%s)"""
        
        # Convert data into tuple format
        insert_blob_tuple = (id, filee)
        result  = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print (" file inserted successfully  table", result)
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed inserting  data into MySQL table {}".format(error))
    finally:
        #if(connection.is_connected()):
        #   cursor.close()
        #   connection.close()
        print("MySQL connection is closed")

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

'''
foin=open('index','r')
count=0
for i in foin:
    i=i.strip()
    file_word=i.split('/')
    filee=file_word[1]
    ids=re.search('\d+',file_word[1])
    class_word=file_word[1].split('.pdf')
    row_class=class_word[0]
    classs=re.sub(r'\d+','',row_class)
    count=count+1
    ids=format(count,'>08')
    ids=str('2')+ids
    ids=format(ids,'>09')
    #ids=str('20')+str(ids.group())
    print(ids,filee,classs)
    #insertclass(ids,filee,classs)
'''



