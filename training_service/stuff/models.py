from django.db import models

# Create your models here.

class TopicCategory(models.Model):
    name = models.CharField(verbose_name='Название темы', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    category = models.ForeignKey(TopicCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название теста', max_length=128)
    description = models.TextField(verbose_name='Описание теста', blank=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"