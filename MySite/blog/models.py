from django.db import models as m
from django.utils import timezone
from django.conf import settings

class PublishedManager(m.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )

class Post(m.Model):
    class Status(m.TextChoices):
        DRAFT = 'DF', 'Roboczy'
        PUBLISHED = 'PB', 'Opublikowany'

    title = m.CharField(max_length = 250)
    slug = m.SlugField(max_length = 250)
    author = m.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=m.CASCADE,
        related_name='blog_post'
    )
    body = m.TextField()
    publish = m.DateTimeField(default=timezone.now)
    created = m.DateTimeField(auto_now_add=True)
    updated = m.DateTimeField(auto_now=True)
    status = m.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )    
    objects = m.Manager() # Menedżer domyślny
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            m.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title 

# Coś tu jest solidnie nie tak 

class Product(m.Model):
    class Status(m.TextChoices):
        DRAFT = 'DF', 'Roboczy'
        PUBLISHED = 'PB', 'Opublikowany'

    p_key = m.AutoField(primary_key=True)
    name = m.CharField(max_length = 250)
    price = m.DecimalField(max_digits = 100, decimal_places=2)
    slug = m.SlugField(max_length = 250)

