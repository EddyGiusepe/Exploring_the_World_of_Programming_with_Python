#!/usr/bin/env python3
import mysql.connector
#pip install mysql-connector-python
import streamlit as st

conn = mysql.connector.connect(
host="localhost",
port="3306",
user="root",
password="123456",
db="multiple_regression")

c = conn.cursor()


def view_all_data():
	c.execute('SELECT * FROM economic_index')
	data = c.fetchall()
	return data

