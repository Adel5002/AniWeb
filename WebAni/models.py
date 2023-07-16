from datetime import date
from django.db import models


class Series(models.Model):
    poster = models.ImageField(upload_to='poster/')
    name = models.CharField(max_length=200)
    japanese_name = models.CharField(max_length=200, blank=True, null=True)
    premiere = models.DateField(default=date.today)
    episodes = models.PositiveSmallIntegerField(default=24)
    STATUS_CHOICES = (
        ('ongoing', 'Онгоинг'),
        ('released', 'Вышел'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # genre = models.ManyToManyField('')
    # studio = models.ForeignKey()
    season = models.CharField(blank=True, null=True, max_length=120)
    slug = models.SlugField(max_length=180, unique=True)


