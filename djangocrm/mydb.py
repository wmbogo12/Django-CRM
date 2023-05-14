import mysql.connector

dataBase  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password123',

)

# prepare a cursor object
cursorObject = dataBase.cursor()

#create a databese
cursorObject.execute("CREATE DATABASE crmdb")

print("All Done!")