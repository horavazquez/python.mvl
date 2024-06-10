import mysql.connector
import credentialslab
try:
    mydb = mysql.connector.connect(
        host=credentialslab.host,
        user=credentialslab.user,
        password=credentialslab.password,
        port=credentialslab.port,
        database=credentialslab.database
        )
except mysql.connector.Error as e:
    print(e)
else:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTS (id INT, description VARCHAR(255), price FLOAT)")
    print("Creacion de la Tabla Exitosa!!!!")
finally:
    mydb.close()