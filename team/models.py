from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Team(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    text = models.TextField("Текст")
    image = models.ImageField(upload_to='post/%Y/%m/%d', verbose_name="Изображения")
    slug = models.SlugField("Слаг", default='', null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Автор")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("about_detail", kwargs={"slug": self.slug})
class Meta:
    verbouse_name_plural = "посты"
    verbouse_name = "пост"
