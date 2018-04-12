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
            
            
    def searchEs(self,name,desc):
        
        ress = self.es.search(index="people",doc_type="records",body={"query": {"match": {"name":name}}})
        
        print("%d documents found" % ress['hits']['total'])
        for hit in ress['hits']['hits']:
            print(hit["_source"])
            print(hit['_source']['name'])
            names = hit['_source']['name']
            descs = hit['_source']['desc']
        return ress
            
            
if __name__=='__main__':
     t = ESindex();
     t.searchEs('anne','ll')