from django.db import models
import ast

class Person(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta():
        abstract = True

class Owner(Person):
    photo_url = models.CharField(max_length=250)
    p_langs = models.CharField(max_length=350)

    class Meta():
        db_table = "ownership"

class OwnerProxy(Owner):
    def get_json(self):
        langs = [n.strip() for n in ast.literal_eval(self.p_langs)]
        return {
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "photo_url": self.photo_url,
            "p_langs": langs,
        }
    
    class Meta():
        proxy = True

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    url = models.CharField(max_length=250, null=True)

    class Meta():
        db_table = "projects"

class ProjectProxy(Project):
    def get_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "url": self.url
        }
    
    class Meta():
        proxy = True

