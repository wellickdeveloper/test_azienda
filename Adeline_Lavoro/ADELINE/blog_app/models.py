from django.db import models
from datetime import datetime, date
# Create your models here.
from django.utils import timezone
from django.urls import reverse # new


from ckeditor.fields import RichTextField


class blogpost(models.Model):
    slug = models.SlugField(unique=True)
    data = models.DateField(max_length=30, default=timezone.now)
    title = models.CharField(max_length=80)
    content = RichTextField(default="articolo del blog")
    image = models.ImageField(upload_to='immagini_database')
    autore = models.TextField(null=True, blank=True, max_length=30)

    def get_absolute_url(self):
        # new method for avoid url manually
        # ricordarsi molto bene di aggiungere il parametro nel file url.py per connettere questa funzione
        return reverse('articols', args=[str(self.slug)])


    class Meta:
        # UTILIZZO DELLA CLASSE META PERCHE DJANGO AGGIUNGE UNA S ALLA FINE DEI NOMI
        verbose_name_plural = "ARTICOLI BLOG"