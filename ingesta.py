import boto3
import mysql.connector
import pandas as pd

# 1. Configuración de conexión a la BD
db_config = {
    'host': 'mysql_c',
    'user': 'root',
    'password': 'utec',
    'database': 'mi_base_datos'
}

# 2. Extraer datos de MySQL
conn = mysql.connector.connect(**db_config)
query = "SELECT * FROM tu_tabla" # Reemplaza por tu tabla
df = pd.read_sql(query, conn)
conn.close()

# 3. Guardar en CSV local
ficheroUpload = "data.csv"
df.to_csv(ficheroUpload, index=False)

# 4. Subir a S3
nombreBucket = "rchoque-tarea" # Tu bucket actualizado
s3 = boto3.client('s3')
s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada")