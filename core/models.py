from django.db import models
from django.utils.text import slugify


class ExamConcours(models.Model):
    numero_ordre = models.IntegerField()
    titre = models.CharField(max_length=100)
    description = models.TextField()
    statut = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titre)
            self.slug = base_slug
            counter = 1
            while ExamConcours.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter +=1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre

