# mediamapper
Mapa de Medios

Aplicación con base de datos para mapear la propiedad de los medios.

Para instalar la aplicación se requiere tener alguna experiencia en Django Framework y la configuración de un servidor con Apache2 y MySQL.
Mapa de Medios está desarrollado para correr en un servidor Apache 2, MySQL y Django 1.8 (Python 2.7)
Esta es una descripción de los pasos para instalar la aplicación pero no de los procesos externos a la app misma.

1. Preparar el servidor con Debian/Ubuntu Linux, Apache 2, MySQL y Python 2.7
2. Crear un ambiente virtualizado de desarrollo con viartualenv. Recordar que la instalación de algunos elementos requiere sudo. (este punto no es requisito si se tiene un servidor propio)
3. Crear una base de datos MySQL con nombre mmapper e importar la base de datos actual que viene con el proyecto (MediosChile y MediosColombia) (mmapper.sql).
4. Instalar pip si es que no está y correr pip install -r path/to/requeriments.txt, eso debe instalar django y todos los requerimientos.
5. Cargar y modificar, según las rutas locales, el archivo mediamapper.conf en los virtual hosts de Apache. esto es para salir a través del servidor web.
6. Realizar el proceso de configuración y puesta en marcha habitual de Django. Configurar settings.py. Se necesita crear un nuevo superusuario de django para administrar la aplicación.

La aplicación tiene un sitio público y un admin con mantenedores de medios, contenidos y control centralizado de mensajes de colaboración y rectificación.
Se debe abrir una cuenta en mailchimp para usar el plugin de django para mandrill.
La aplicación está en modo de desarrollo, para pasar a producción cambiar debug a false.
Las imágenes de los directorios medio y uploads que están en mediamapper/media fueron eliminados de este repositorio.
En el documento Virtualenv+Nginx+Supervisor hay un tutorial para instalar la aplicación con esas características. Puede ser útil pero no está actualizado.
