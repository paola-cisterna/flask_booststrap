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
```