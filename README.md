# Práctica 4

## Creación de script python
Basándonos en el readme de la práctica que nos dieron, lo tomamos como base y fuimos añadiendo cosas que eran necesarias, como la función de ayuda y la implementación de los demás parámetros.

## Ejemplos de ejecución



## Creación de dockerfile

Teníamos alguna experiencia con los dockerfiles gracias al servicio y el trabajo en donde estamos, queríamos hacer nuestra imagen de ubuntu por lo que tomamos como base el que venía de ejemplo y modificamos la instalación de paquetes para utilizar los de python3 en vez de python2. Ya que los paquetes _socket_ y _sys_ vienen por defecto en python, no es necesario instalar pip ni los paquetes en nuestro contenedor, por lo que simplemente creamos la imagen de ubuntu, y descargamos python, para poder ejecutar nuestro script . El ejemplo fue de mucha ayuda pues sólo tuvimos que cambiar las versiones y eliminar algunas cosas para poder usarlo. Nos parece que docker es una increíble herramienta pues facilita mucho la creación de contenedores, una vez que se entiende la sintaxis es muy fácil de usar.

Nosotros utilizamos windows para la creación de todo, por lo que antes de ejecutar los comandos entramos a nuestro DockerDesktop y no necesitamos usar _sudo_. Para probar nuestro contenedor lo hicimos con los comandos:

> docker build -t redes:p4

para construir la imagen 

## Preguntas

1. ¿Cuál es la función de los métodos de HTTP HEAD, GET, POST, PUT y DELETE?
2. ¿Investigue y enliste junto con su significado las categorías de códigos de estado que usa HTTP?
3. ¿Para qué se usan los campos encoding y connection

## Integrantes:
  - Carmen Paola Innes Barrón
  - Jean Durán Villanueva

