# Proyecto de Portafolios
El proyecto original termino con serios bugs y no pude perder mas tiempo intentando resolverlos, borre la base de datos para intentar reproducir la experiencia de instalacion desde 0 pero django se bloqueo con un error en el que no podia reconocer las tablas. Igual puedes revisarlo [aqui](https://github.com/rdev32/django-folio)
## Setup
Para instalar las dependencias cree un entorno virtual y ejecute
```
pip install -r requirements.txt
```
No te olvides de crear el superusuario!

Ya casi esta todo listo, ahora solo falta ejecutar la aplicacion
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```