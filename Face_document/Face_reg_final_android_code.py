# Face App Code Details
# Created by Thirumoorthi (Unlicensed)
# Last updated: Mar 07, 202210 min read
# 2 people viewed
# face app code explanation and details

# Go to the Terminal

# ssh troondxadmin@129.151.44.205 -p22

# TrdX@dM!!9#4132$

# Go to face app path and activate the environment

# cd aimp

# source bin/activate

# file name is face_app.py

# Run commend Face App

# python face_app.py

# Install libraries commends

# pip install unicorn

# pip install numpy

# pip install opencv-python

# pip install mysql-connector-python

# pip install fastapi

# pip install arcface

# necessary libraries 


import uvicorn
import os
import numpy as np
import cv2
import mysql.connector
from datetime import datetime
from fastapi import FastAPI, File, UploadFile
from arcface import ArcFace
from typing import List
import time
 

Database connectivity


app = FastAPI()
face_rec = ArcFace.ArcFace()

mydb = mysql.connector.connect(
  host="localhost",  
  user="oasys",  
  password="Oasys@123!*",  
  database="oasys")
mycursor = mydb.cursor()
Login API


@app.post("/login")
async def analyze_route(id:int,pasd:int):
    try:
        if id==pasd:
            sql = "SELECT * FROM login WHERE id = {}".format(id)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            print("this is first login data",myresult)
            check = "SELECT max(intime),max(outtime)  FROM test WHERE id = {}".format(id)
            mycursor.execute(check)
            result = mycursor.fetchone()
            in_date = str(result[0])
            out_date = str(result[1])
            print(in_date, " ############", out_date)
            if in_date == 'None' and out_date == 'None':
                indate = ""                
                intime = ""                
                outtime = ""                
                outdate = ""            
             elif in_date != 'None' and out_date == 'None':
                c_date = in_date.split(" ")
                indate = c_date[0]
                intime = c_date[1]
                outdate = ""
             elif in_date != 'None' and out_date != 'None':
                c_date = in_date.split(" ")
                indate = c_date[0]
                intime = c_date[1]
                out_date = str(result[1])
                c_date = out_date.split(" ")
                outdate = c_date[0]
                outtime = c_date[1]

            else:
                print("this is else conditio")
            if myresult != []:
                data = myresult[0]
                mydb.commit()
                # mycursor.close()                
                return {"success": "true","result": {"name": data[0], "id": data[1], "isEnroll": data[3], "checkindate": indate,"checkoutdate": outdate, "checkintime": intime, "checkouttime": outtime}}
            else:
                return {"Success": "false", "errorMsg": "Please check your userID"}
        else:
            return {"Success": "False", "errorMsg": "Please check your userID"}
    except Exception as e:
        return {"Success": "false", "errorMsg": "The service is not available"}


 

Enrol API


@app.post("/endroll")
async def analyze_route(id:int,files: List[UploadFile] = File(...)):
    try:
        directory = '/home/troondxadmin/aimp/dataset/images/{}'.format(id)

        if not os.path.exists(directory):
            os.mkdir(directory)
        i = 0        for img in files:
            contents = await img.read()
            nparr = np.fromstring(contents, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            cv2.imwrite("{}/{}{}.jpg".format(directory, id, int(i)), img)
            i = i + 1        
        faces = []
        name = []
        dir = "/home/troondxadmin/aimp/dataset/images/{}".format(id)
        # print(os.path.splitext(dir)[0])        
        for filename in os.listdir(dir):
            img_path = os.path.join(dir, filename)
            emb1 = face_rec.calc_emb(img_path)
            faces.append(emb1)
            name.append(id)
        Embeddings = np.array(faces)
        Names = np.array(name)
        np.save("/home/troondxadmin/aimp/model_file/{}embed.npy".format(id), Embeddings)
        np.save("/home/troondxadmin/aimp/model_file/{}name.npy".format(id), Names)
        # sql = "UPDATE login SET endroll = '0' WHERE endroll = '1'"        sql = "update login set endroll='1' where id={}".format(id)
        mycursor.execute(sql)
        check = mycursor.fetchall()
        print(check)

        #mydb.commit()        
        #mycursor.close()        
        return {"Success": "True"}
    except Exception as e:
        return {"Success": "false", "errorMsg": "please try again ofter some times" }
 

Checkin API


@app.post("/checkin")
async def analyze_route1(id:str,file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # img = mtcnn(img)        
        emb2 = face_rec.calc_emb(img)
        encode= np.load('/home/troondxadmin/aimp/model_file/{}embed.npy'.format(id))
        name = np.load('/home/troondxadmin/aimp/model_file/{}name.npy'.format(id))
        test = []
        for x in encode:
            a = face_rec.get_distance_embeddings(x, emb2)
            test.append(a)
        com = dict(zip(test, name))
        order = sorted(com.items(), key=lambda d: d[0])
        result = min(order)
        print("percentage match",result[0])
        if result[0] <= 0.60:
            sql = "SELECT * FROM login WHERE id = {}".format(result[1])
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            name = myresult[0][0]
            name = str(name).upper()
            eid = myresult[0][1]
            #print(eid)            #print(id)            
            if eid==int(id):
                formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')

                sql = """INSERT INTO test VALUES(%s,%s,%s,null,%s,null,null)"""                cmts = "New record"                inp_val = (name,id,formatted_date,cmts)
                print(inp_val)
                mycursor.execute(sql, inp_val)
                mydb.commit()
                #mycursor.close()                
                print("inside checkin")
                return {"Success":"true","result":name,"time":formatted_date}
            else:
                return{"success":"false","errorMsg":"Multi face detect"}
        else:
            return {"Success":"false","errorMsg":"Face not recognize"}
    except Exception as e:
        return {"Success": "false", "errorMsg": "The service is not available"}
 Checkout API


@app.post("/checkout")
async def analyze_route1(id:str,break_time:str,lunch_time:str,file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # img = mtcnn(img)        emb2 = face_rec.calc_emb(img)
        print("kumararaja response",break_time,lunch_time)
        encode= np.load('/home/troondxadmin/aimp/model_file/{}embed.npy'.format(id))
        name = np.load('/home/troondxadmin/aimp/model_file/{}name.npy'.format(id))
        test = []
        for x in encode:
            a = face_rec.get_distance_embeddings(x, emb2)
            test.append(a)
        com = dict(zip(test, name))
        order = sorted(com.items(), key=lambda d: d[0])
        result = min(order)
        print("percentage match",result[0])
        if result[0] <= 0.60:
            sql = "SELECT * FROM login WHERE id = {}".format(result[1])
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            name = myresult[0][0]
            name = str(name).upper()
            eid = myresult[0][1]
            if eid==int(id):
                formatted_date = time.strftime('%Y-%m-%d %H:%M:%S')

                sql = """Update test set outtime = %s, comments = %s where id = %s and comments = 'New record'"""                cmts = "Record updated with checkout time"                input_data = (formatted_date,cmts,id)
                print(input_data)
                mycursor.execute(sql, input_data)
                mydb.commit()
                print("inside else")
                sql2 = """Update test set break = %s, lunch = %s where id = %s"""                input_data = (break_time,lunch_time,id)
                print(input_data)
                mycursor.execute(sql2, input_data)
                mydb.commit()
                #mycursor.close()                return {"Success":"true","result": name, "time": formatted_date}
            else:
                return{"success":"false","errorMsg":"Multi face detect"}
        else:
            return {"Success":"false","errorMsg":"Face not recognize"}
    except Exception as e:
        return {"Success": "false", "errorMsg":"The service is not available "}

API Closing


if __name__ == '__main__':
    uvicorn.run('face_app:app', port=8002, host='0.0.0.0',reload=True,debug=True)
