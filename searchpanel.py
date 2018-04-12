#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:39:56 2018

@author: alex
"""

import easygui as g
import sys
from index import ESindex



       
name = g.enterbox(msg="your search target",title="search---")
es = ESindex()
ress = es.searchEs(name,name)
context=""
for hit in ress['hits']['hits']:
         names = hit['_source']['name']
         descs = hit['_source']['desc']
         print(names)
         print(descs)
         context += names+" "+descs+"\n "
g.msgbox(context)
   
           #
      
   
        
        
        
        

if __name__=='__main__':
     url ='http://www.runoob.com/python/python-object.html'
     #p =panels();
     #db1.fetchlink()
  
        