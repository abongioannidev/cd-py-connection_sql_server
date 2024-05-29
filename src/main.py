import pyodbc
def get_data():

# Definir los parámetros de la conexión
    server = '.'  # Ejemplo: 'localhost\SQLEXPRESS'
    database = 'mydatabase'
    nombre_tabla = 'personas';


    # Crear la cadena de conexión
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    # Establecer la conexión
    conn = pyodbc.connect(connection_string)

    # Crear un cursor desde la conexión
    cursor = conn.cursor()

    # Definir la consulta SQL
    query = f'SELECT * FROM {nombre_tabla}'

    # Ejecutar la consulta
    cursor.execute(query)

    # Obtener los resultados
    rows = cursor.fetchall()

    # Procesar los resultados
    for row in rows:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()




if __name__ == "__main__":
    get_data()
    