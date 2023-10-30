# Descargamos la imagen de ubuntu
FROM ubuntu
RUN apt-get update -y

# Instala Python 3 y pip para Python 3
RUN apt-get install -y python3

# Copia el archivo clientHTTP_base.py al directorio /opt/ dentro de la imagen
ADD HTTPClient.py /opt/
