from django.db import models



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

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Задание',max_length=256)
    result = models.IntegerField(verbose_name='Ответ')

class Ask(models.Model):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FORTH = 4
    VARIABLE_CHOICES = [
        (FIRST, '1'),
        (SECOND, '2'),
        (THIRD,'3'),
        (FORTH,'4')
    ]
    choice = models.IntegerField(verbose_name='Вариант ответа',choices=VARIABLE_CHOICES,blank=True)
    question = models.OneToOneField(Question,on_delete = models.CASCADE,primary_key=True)