import mysql.connector as mc
dbc = mc.connect(host="localhost",user="root",passwd="root",database="rainfall")
cursor=dbc.cursor()