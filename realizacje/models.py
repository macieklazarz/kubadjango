from django.db import models

# Create your models here.
class Realizacje(models.Model):
    nazwa = models.CharField(max_length=100)
    foto = models.ImageField(blank=True)


    def __str__(self):
    	return self.nazwa

    class Meta:
    		verbose_name = "Realizacje"
    		verbose_name_plural = "Zdjęcia"