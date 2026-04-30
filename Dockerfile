FROM python:3-slim

# Instalar dependencias del sistema necesarias para mysql-connector
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /programas/ingesta

# Instalar librerías de Python
RUN pip3 install boto3 pandas mysql-connector-python

COPY . .

CMD [ "python3", "./ingesta.py" ]