# Proyecto de Portafolios 
## Setup
Para instalar las dependencias cree un entorno virtual y ejecute
```
pip install -r requirements.txt
```

Luego cree un archivo `.env` con el siguiente contenido
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