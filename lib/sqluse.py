# -*- coding: utf-8 -*-

import sqlite3


def dbconn(list):

    dbconn = sqlite3.connect("/Users/cj/booksys/book_DB.db")
    print("db connect success")
    
    cur = dbconn.cursor()
    
    
    
    
  #  cur.execute("INSERT INTO bookcj (id,cname,ename,author,size,format) \
    #  VALUES (2, 'j++编程','j++program','xxx', 33, 'txt' )")
   
    cur.execute("INSERT INTO bookcj (id,cname,ename,author,size,format) \
    #  VALUES (list)"))
    
    
    dbconn.commit()          
    
    cur.execute("select * from bookcj")
    
    for item in cur.fetchall():
        for element in item:
            print(element)
        print("okkkk")
    dbconn.commit()     

    return
'''
CREATE TABLE "bookcj" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"cname"	TEXT NOT NULL,
	"ename"	TEXT NOT NULL,
	"author"	TEXT NOT NULL,
	"size"	INTEGER NOT NULL,
	"format"	TEXT NOT NULL
);
'''
dbconn()