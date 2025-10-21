from django.db import models

class Job(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Position')
    firma = models.CharField(max_length=50, verbose_name='Firma')
    firma_link = models.CharField(max_length=250, verbose_name='Link zur Firma')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Stellenangebot'
        verbose_name_plural = 'Stellenangebote'