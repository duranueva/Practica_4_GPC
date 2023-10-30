# Práctica 4

## Creación de script python
Basándonos en el readme de la práctica que nos dieron, lo tomamos como base y fuimos añadiendo cosas que eran necesarias, como la función de ayuda y la implementación de los demás parámetros. Lo que hicimos fue agregar algunos agents que le pedimos a chatgpt, y modificar las funciones para que funcionen con parámetros en vez de tener valores fijos.

Para ver ejemplos de ejecución se puede ejecutar:

> python3 opt/HTTPClient --help

> python3 opt/HTTPClient --h

Dentro o fuera del contenedor


## Creación de dockerfile

Teníamos alguna experiencia con los dockerfiles gracias al servicio y el trabajo en donde estamos, queríamos hacer nuestra imagen de ubuntu por lo que tomamos como base el que venía de ejemplo y modificamos la instalación de paquetes para utilizar los de python3 en vez de python2. Ya que los paquetes _socket_ y _sys_ vienen por defecto en python, no es necesario instalar pip ni los paquetes en nuestro contenedor, por lo que simplemente creamos la imagen de ubuntu, y descargamos python, para poder ejecutar nuestro script . El ejemplo fue de mucha ayuda pues sólo tuvimos que cambiar las versiones y eliminar algunas cosas para poder usarlo. Nos parece que docker es una increíble herramienta pues facilita mucho la creación de contenedores, una vez que se entiende la sintaxis es muy fácil de usar.

Nosotros utilizamos windows para la creación de todo, por lo que antes de ejecutar los comandos entramos a nuestro DockerDesktop y no necesitamos usar _sudo_. Para probar nuestro contenedor lo hicimos con los comandos:

> docker build -t redes:p4 .

para construir la imagen, y luego probarla con:

> 

## Preguntas

1. ¿Cuál es la función de los métodos de HTTP HEAD, GET, POST, PUT y DELETE?

Los métodos de HTTP (Hypertext Transfer Protocol) son comandos que indican la acción que se debe realizar en un recurso identificado, como por ejemplo, una aplicación que pida recursos a una API utilizaría estos metodos. 

- HEAD: Solicita los encabezados de un recurso, funciona para obtener los primeros datos de este que pueden servir para reconocimiento. 
- GET: Solicita la representación de un recurso específico. Se utiliza para recuperar información y no debe tener ningún otro efecto secundario en el servidor (es decir, no debe modificar los datos, sino solo obtenerlos).
- POST: Envía datos al servidor para que sean procesados. Se utiliza para enviar datos a un recurso (que puede ser un servidor) a través del cuerpo de la solicitud. Esta información se puede utilizar para que el "recurso" pueda crear otros datos a través de este.
- PUT: Actualiza un recurso existente o crea uno nuevo si no existe. Tiene, a diferencia de POST, que realizar la misma solicitud varias veces no tiene efectos diferentes que realizarla una sola vez.
- DELETE: Solicita la eliminación de un recurso específico en el servidor. Realizar la misma solicitud varias veces no tiene efectos diferentes que realizarla una sola vez.

Es muy importante tener en cuenta que estas son solo una convencion de buenas practicas, pues en teoría, podrías enviar una solicitud GET que tenga un efecto secundario de borrado en el servidor. Así que es importante seguir esta convencion para tener un uso correcto y por ende ser menos propenso a errores.


2. ¿Investigue y enliste junto con su significado las categorías de códigos de estado que usa HTTP?

Los códigos de estado HTTP son parte del protocolo de comunicación HTTP utilizado en la Web. Son enviados por parte del servidor como respuesta despues de haber recibido una solicitud de un cliente.

Algunas caracteristicas principales:

- Constan de tres digitos, comenzando en 100 y terminando en 599.
- El primer digito nos indica su significado:
  - 1xx - Respuestas informativas
  - 2xx - Respuestas exitosas
  - 3xx - Redirecciones
  - 4xx - Errores del cliente
  - 5xx - Errores del servidor
- Los ultimos dos digitos nos indican las diferentes respuestas que se tienen en torno a el primer digito, como por ejemplo:
  - 100 - Continuar: El servidor ha recibido la solicitud y el cliente puede continuar con la siguiente parte de la solicitud.
  - 200 - OK: La solicitud fue exitosa.
  - 201 - Creado: La solicitud ha sido completada y ha resultado en la creación de un nuevo recurso.
  - 400 - Solicitud incorrecta: La solicitud no pudo ser entendida o estaba mal formada.
  - 401 - No autorizado: La solicitud necesita autenticación del usuario.
  - 500 - Error interno del servidor: El servidor ha encontrado una situación que no sabe cómo manejar.
  - 503 - Servicio no disponible: El servidor no está listo para manejar la solicitud. Por lo general, esto se debe a mantenimiento del servidor o sobrecarga.

3. ¿Para qué se usan los campos encoding y connection?

'encoding' se utiliza para especificar la codificación de contenido aplicada al cuerpo del mensaje. Indica cómo se ha comprimido o codificado el cuerpo del mensaje para su transferencia. Un ejemplo es, si el servidor envía datos comprimidos para ahorrar ancho de banda, este campo informará al cliente sobre la codificación utilizada (por ejemplo, gzip, deflate). El campo 'connection' se utiliza para controlar las opciones de conexión entre el cliente y el servidor. Puede incluir directivas que informan al servidor sobre cómo manejar la conexión después de completar la respuesta.  Algunos valores comunes son keep-alive para indicar que la conexión debe mantenerse abierta para futuras solicitudes, o close para indicar que la conexión debe cerrarse después de la respuesta actual.


## Integrantes:
  - Carmen Paola Innes Barrón
  - Jean Durán Villanueva

