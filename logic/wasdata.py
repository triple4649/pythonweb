from flask import Flask, render_template,g
import sys
import os
sys.path.append(os.getcwd())
from app import db


class Word(db.Model): # �ǉ�
    __tablename__ = "words" # �ǉ�
    id = db.Column(db.Integer, primary_key=True) # �ǉ�
    examkind = db.Column(db.String(), nullable=False) # �ǉ�
    season = db.Column(db.String(), nullable=False) # �ǉ�
    questionkind = db.Column(db.String(), nullable=False) # �ǉ�
    questionno = db.Column(db.Integer) # �ǉ�
    questionnorenban = db.Column(db.Integer) # �ǉ�
    word = db.Column(db.String(), nullable=False) # �ǉ�

    
def add_Word_toDB(str):
   # target_list = list(map(lambda word:edit(word.split(":")[0],word.split(":")[1]),str.split("\n\r")))
    target_list =[x+'<br>' for x in str.split("\n") ]  
    return target_list

def edit(strlist):
    list = [x for x in strlist if len(x)==2]
    print(list)
    return [[y[0],y[1].split('|')] for y in list]
    