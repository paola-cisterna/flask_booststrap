# Documentacion
Esta es una aplicacion web utilizando el framework flask y bootstrap. Su proposito es ejemplificar un CRUD utilizando el recurso mensaje.
Los datos se guardan en la base de datos postgres utilizando migraciones.
Las dependencias del proyecto de gestionan con pipenv.
## Dependencias
Para correr este proyecto de necesita previamente tener instalado python 3 y su herramienta pip.
Para revisar si las tienes instalado debes ejecutar los siguientes comandos:
```
python -V
pip -V
```
El resultado debe indicar el número superior a 3.
Luego de clonar el repositorio y para instalar las dependencias debe ejecutar el comando
`pipenv install`
## Migraciones
Para ejecutar las migraciones el comando es el siguiente:
```
flask db upgrade
```
En caso de modificar un modelo agregando o modificando un atributo , debemos generar una nueva migración con el comando
```
flask db migrate -m "Mensaje de la migracion"
```
**not**:
Los comandos anteriores se deben ejecutar dentro de `pipenv shell`
## Levantando la aplicación
Para ejecutar el servidor de desarrollo el comando es el siguiente
```
flask --app app-- debug run
``



## Blueprint 

Los blueprint permiten componer aplicaciones desde componente pequeños. Cada componente es como una nini aplicacion.permiten crear aplicaciones grandes manteniendo el codigo y la estructura simple.

## Modulos 

para que los blueprint esten bien organizados, es mejor trabajarlos como modulos, es decir,que esten dentro de una carpeta. Los modulos se pueden anidar nosotros hicimos el modulo 'app' con su respectivo__init__.py y dentrotenemos otros modulos como el modulo 'messages' que es ademas un blueprint 

## Tarea 
Crear un nuevo recurso sencillo, sin base de datos, como blueprint bajo a url / memes debe renderiar html lleno de memes. 
