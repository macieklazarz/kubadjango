from django.db import models

# Create your models here.
class Tuz(models.Model):
    nazwa = models.CharField(max_length=100)
    # slug = models.SlugField()
    rozmiar = models.TextField()
    waga = models.IntegerField()
    typ = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(blank=True)


    def __str__(self):
    	return self.nazwa

    class Meta:
    		verbose_name = "Wszystkie tuzy"
    		verbose_name_plural = "Wszystkie tuzy"


