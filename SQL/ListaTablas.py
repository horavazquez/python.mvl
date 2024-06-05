import mysql.connector
import credentials

mydb = mysql.connector.connect(
  host=credentials.host,
  user=credentials.user,
  password=credentials.password,
  port=credentials.port,
  database=credentials.database
  )

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)