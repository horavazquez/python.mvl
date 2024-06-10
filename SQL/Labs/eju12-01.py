import mysql.connector
import credentialslab
try:
    mydb = mysql.connector.connect(
        host=credentialslab.host,
        user=credentialslab.user,
        password=credentialslab.password,
        port=credentialslab.port,
        )
except mysql.connector.Error as e:
    print(e)
else:
    print(f'Se logro conectar al host {credentialslab.host} en el puerto {credentialslab.port} con el usuario {credentialslab.user}')
    mydb.close()
finally:
    if 'mydb' in locals():
        print("Conexion Exitosa!!!!")
    else:
        print("Error de Conexion")

