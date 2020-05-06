from flask import Flask, render_template, request,session,g
import os
import sqlite3

app=Flask(__name__)

@app.route('/')
def index():
   return 'home page'

@app.route('/cluster/getRank/<string:clusterNo>')
def getRank(clusterNo):
   rank_list=[]
   con = sqlite3.connect("trends.db")    
   cur = con.cursor()
   cur.execute("select c"+clusterNo+" from RANK")
   con.commit()
   rows = cur.fetchall(); 
   for row in rows:
       rank_list.append(row)
   return rank_list

@app.route('/cluster/getsize/<string:clusterNo>')
def getSize(clusterNo):
   size_list=[]
   con = sqlite3.connect("trends.db")    
   cur = con.cursor()
   cur.execute("select c"+clusterNo+" from SIZE ")
   con.commit()
   rows = cur.fetchall(); 
   for row in rows:
       size_list.append(row[0])
   listToStr = ' '.join(map(str, size_list)) 
   return listToStr


if __name__ == "__main__":
    app.run(debug=True)

