# -*- coding: utf-8 -*-
#encoding=utf-8
"""
Created on Mon Nov 27 11:23:29 2017

@author: alex
"""

import sys  
reload(sys)  
sys.setdefaultencoding("utf-8")  

import MySQLdb
 
                     
class db:
      def __init__(self):
          self.db = MySQLdb.connect(host="localhost",user="root",passwd="123456",port=3306,db="link" )
          self.cursor = self.db.cursor()
      
      def insert(self,url,content):
         
          sql = "insert into link(url,content)VALUES ('%s','%s')"%(url,content)
          #print sql
          try:
              self.cursor.execute(sql)
              self.db.commit()
          except:
              print self.db.Error
          finally:             
              self.db.close()
             
      def fetchlink(self):
          print("-------")
          sql = "select * from link"
          try:
              self.cursor.execute(sql)
              res = self.cursor.fetchall()
              print "-------"
              return res
          except:
              print self.db.Error
          finally:
             self.db.close()
             


             
        

if __name__=='__main__':
     url ='http://www.runoob.com/python/python-object.html'
     db1 =db();
     db1.fetchlink()
  

    
        
        
