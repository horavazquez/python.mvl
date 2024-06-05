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
sql = "SELECT * FROM customers"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


