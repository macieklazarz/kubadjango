from django.db import models

# Create your models here.
class Akcesoria(models.Model):
    nazwa = models.CharField(max_length=100)
    # slug = models.SlugField()
    # rozmiar = models.TextField()
    # waga = models.IntegerField()
    opis = models.TextField()
    # date = models.DateTimeField(auto_now_add=True)
    # marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    foto = models.ImageField(blank=True)


    def __str__(self):
    	return self.nazwa

    class Meta:
    		verbose_name = "Akcesoria"
    		verbose_name_plural = "Akcesoria"
