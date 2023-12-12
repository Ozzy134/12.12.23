from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    date = models.DateTimeField()
    agree = models.BooleanField()

    def __str__(self):
        return f'Пользователь {self.name}. Его возраст {self.age}'

class Posts(models.Model):
    title = models.CharField(max_length=25)
    text = models.TextField()
    is_published = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'