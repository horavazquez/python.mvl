import mysql.connector
import credentials

mydb = mysql.connector.connect(
  host= credentials.host,
  user=credentials.user,
  password=credentials.password,
  port=credentials.port
)

print(mydb)