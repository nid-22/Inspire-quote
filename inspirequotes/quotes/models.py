from django.db import models

# Create your models here.
class author(models.Model):
    name= models.CharField(max_length=25)
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to = 'images', default='')

    def __str__(self):
        return self.name

class movie(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class quotes(models.Model):
    line = models.TextField(max_length=500)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.line