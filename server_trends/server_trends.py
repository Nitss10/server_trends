from flask import Flask, render_template, request,session,g
import os
import json
import sqlite3

app=Flask(__name__)

@app.route('/')
def index():
   keyword_list=[]
   con = sqlite3.connect("trends.db")    
   cur = con.cursor()
   cur.execute("select * from KEYWORDS where day=1")
   con.commit()
   rows = cur.fetchall()
   for row in rows:
       keyword_list.append(row)
   return json.dumps(keyword_list)

@app.route('/cluster/getrank/<string:clusterNo>')
def getRank(clusterNo):
   rank_list=[]
   con = sqlite3.connect("trends.db")    
   cur = con.cursor()
   cur.execute("select c"+clusterNo+" from RANK")
   con.commit()
   rows = cur.fetchall()
   for row in rows:
       rank_list.append(row[0])
   return json.dumps(rank_list)

@app.route('/cluster/getkeywords/<string:clusterNo>')
def getkeywords(clusterNo):
   keyword_list=[]
   con = sqlite3.connect("trends.db")    
   cur = con.cursor()
   cur.execute("select c"+clusterNo+" from KEYWORDS")
   con.commit()
   rows = cur.fetchall()
   for row in rows:
       keyword_list.append(row[0])
   return json.dumps(keyword_list)

@app.route('/cluster/getsize/<string:clusterNo>')
def getSize(clusterNo):
   size_list=[]
   con = sqlite3.connect("trends.db")    
   cur = con.cursor()
   cur.execute("select c"+str(clusterNo)+" from SIZE")
   con.commit()
   rows = cur.fetchall() 
   for row in rows:
       size_list.append(row[0])
   return json.dumps(size_list)

@app.route('/cluster/getcluster/<string:clusterNo>')
def getCluster(clusterNo):
   cluster_object = {"rank":[],"size":[],"keywords":[]}
   rank_list=[]
   size_list=[]
   keywords_list=[]
   clusterNo=str(clusterNo)
   rank_list=getRank(clusterNo)
   size_list=getSize(clusterNo)
   keywords_list=getkeywords(clusterNo)
   cluster_object['rank']=rank_list
   cluster_object['size']=size_list
   cluster_object['keywords']=keywords_list
   return cluster_object


@app.route('/cluster/getInfo')
def getInfo():
   all_clusters={}
   for i in range(0,100):
      all_clusters[i]=getCluster(i)
   return json.dumps(all_clusters)
     
@app.route('/cluster/getallsize')
def getsizeinfo():
   all_sizes={}
   for i in range(0,100):
      all_sizes[i]=getSize(i)
   return all_sizes

def getkeywordsinfo():
   all_={}
   for i in range(0,100):
      all_sizes[i]=getSize(i)
   return all_sizes

if __name__ == "__main__":
    app.run(debug=True)

