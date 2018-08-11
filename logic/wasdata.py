from flask import Flask, render_template,g
import sys
import os
sys.path.append(os.getcwd())
from app import db


class Word(db.Model): # 追加
    __tablename__ = "words" # 追加
    id = db.Column(db.Integer, primary_key=True) # 追加
    examkind = db.Column(db.String(), nullable=False) # 追加
    season = db.Column(db.String(), nullable=False) # 追加
    questionkind = db.Column(db.String(), nullable=False) # 追加
    questionno = db.Column(db.Integer) # 追加
    questionnorenban = db.Column(db.Integer) # 追加
    word = db.Column(db.String(), nullable=False) # 追加

    
def add_Word_toDB(str):
   # target_list = list(map(lambda word:edit(word.split(":")[0],word.split(":")[1]),str.split("\n\r")))
    target_list =[x+'<br>' for x in str.split("\n") ]  
    return target_list

def edit(strlist):
    list = [x for x in strlist if len(x)==2]
    print(list)
    return [[y[0],y[1].split('|')] for y in list]
    