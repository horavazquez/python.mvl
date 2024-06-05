import mysql.connector
import credentials

mydb = mysql.connector.connect(
  host= credentials.host,
  user=credentials.user,
  password=credentials.password,
  port=credentials.port
)
''',
  database=credentials.database
'''


print(mydb)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE testpython")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)