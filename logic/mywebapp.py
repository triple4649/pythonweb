from flask import Flask, render_template,g
import sys
import os
sys.path.append(os.getcwd())
from app import db

class Image(db.Model): # 追加
    __tablename__ = "images" # 追加
    id = db.Column(db.Integer, primary_key=True) # 追加
    year     = db.Column(db.String(), nullable=False) # 追加
    examkind = db.Column(db.String(), nullable=False) # 追加
    season   = db.Column(db.String(), nullable=False) # 追加
    questionkind = db.Column(db.String(), nullable=False) # 追加
    questionno = db.Column(db.Integer) # 追加
    questiondetailno = db.Column(db.Integer) # 追加
    base64image = db.Column(db.Text(), nullable=False) # 追加

    
def add_Image_toDB(form):
    db.create_all()
    entry = Image()
    entry.year = form['year']
    entry.examkind = form['examkind']
    entry.season = form['season']
    entry.questionkind = form['examkind']
    entry.base64image = form['base64image']
    entry.questionno = form['questionno']
    entry.questiondetailno = form['questiondetailno']
    
    db.session.add(entry)
    db.session.commit()
    