# Portafolios 
## Setup
Para instalar las dependencias cree un entorno virtual y ejecute
```
pip install -r requirements.txt
```

Luego cree un archivo `.env` con el siguiente contenido
```
SECRET_KEY=supersecretkey
DB_ENGINE=mysql
DB_NAME=portfolio
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

Ya casi esta todo listo, ahora solo falta ejecutar la aplicacion
```
python manage.py migrate
python manage.py runserver
```