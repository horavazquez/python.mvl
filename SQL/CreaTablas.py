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
#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
for x in mycursor:
  print(x)