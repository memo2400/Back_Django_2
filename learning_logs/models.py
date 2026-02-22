from django.db import models

# Create your models here.

class Topic(models.Model):
    "topico del que el usuario esta aprendiendo"
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        "regresa un string del modelo"
        return self.text
    
class Entry(models.Model):
    "algo especifico aprendido"
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # si borro el topico, las etradas del mismo se borran en casvcada
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    # telling Django to use Entries when it needs to refer to more than one entry
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        "solo muestra 50 caracteres de la entrada"
        return f"{self.text[:50]}"