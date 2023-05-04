import sys
sys.path.append('..')
from config.database import connection
import pymysql
from flask import Flask,jsonify
app=Flask(__name__)