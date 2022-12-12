# Proyecto de Portafolios 
## Setup
Para instalar las dependencias cree un entorno virtual y ejecute
```
pip install -r requirements.txt
```
No te olvides de crear el superusuario!
Luego agrega un archivo `.env` con el siguiente contenido
```
SECRET_KEY=supersecretkey
DB_ENGINE=sqlite3
DB_NAME=portfolio
```

Ya casi esta todo listo, ahora solo falta ejecutar la aplicacion
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Edit
Si por algun motivo la aplicacion crashea prueba comentando la implementacion en `client/views.py`
dejando **solo** los templates, una vez hechas las migraciones descomenta todo y funcionara (sigo investigando porque pasa este error)
