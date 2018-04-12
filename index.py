#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:15:18 2018

@author: alex
"""
from db import db
from elasticsearch import Elasticsearch


class ESindex:
    es = Elasticsearch() 
    def buildIndx(self):
        db1 =db();
        elements = db1.fetchlink()
        
        for ele in elements:
            ids = ele[0]
            name =ele[1]
            desc = ele[2]
            self.es.index(index="people",doc_type="records",id=ids,body={"name":name,"desc":desc})
            
            
            
            
            
            
if __name__=='__main__':
     t = ESindex();
     t.buildIndx()