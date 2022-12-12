from django.db import models
import ast

class Person(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    born_date = models.DateField(null=True, blank=True)

    class Meta():
        abstract = True

class Owner(Person):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=250)
    languages = models.CharField(max_length=250)
    prog_languages = models.CharField(max_length=350)

    class Meta():
        db_table = "owner"

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    url = models.CharField(max_length=250, null=True)

    class Meta():
        db_table = "projects"

    class OwnerProxy(Owner):
        def get_json(self):
            languages = [n.strip() for n in ast.literal_eval(self.languages)]
            prog_languages = [n.strip() for n in ast.literal_eval(self.prog_languages)]
            
            return {
                "name": self.name,
                "lastname": self.lastname,
                "email": self.email,
                "phone": self.phone,
                "born_date": self.born_date,
                "username": self.username,
                "password": self.password,
                "photo_url": self.photo_url,
                "languages": languages,
                "prog_languages": prog_languages
            }
        
        class Meta():
            proxy = True

class ProjectProxy(Project):
    def get_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "url": self.url
        }
    
    class Meta():
        proxy = True