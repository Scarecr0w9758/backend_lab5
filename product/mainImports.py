import sys
sys.path.append('..')
from config.database import Product, engine
from sqlalchemy.orm import sessionmaker
import pymysql
from flask import Flask,jsonify, render_template

app=Flask(__name__)
Session= sessionmaker (autoflush=False,bind=engine)
