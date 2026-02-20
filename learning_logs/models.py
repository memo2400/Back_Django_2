from django.db import models

# Create your models here.

class Topic(models.Model):
    "topico del que el usuario esta aprendiendo"
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        "regresa un string del modelo"
        return self.text
    