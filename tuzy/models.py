from django.db import models

# Create your models here.

class Marka(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

    class Meta:
            verbose_name = "Marki"
            verbose_name_plural = "Marki"

class Tuz(models.Model):
    nazwa = models.CharField(max_length=100)
    # slug = models.SlugField()
    opis = models.TextField()
    # waga = models.IntegerField()
    # typ = models.TextField()
    # date = models.DateTimeField(auto_now_add=True)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    foto = models.ImageField(blank=True)


    def __str__(self):
    	return self.nazwa

    class Meta:
    		verbose_name = "Wszystkie tuzy"
    		verbose_name_plural = "Wszystkie tuzy"


