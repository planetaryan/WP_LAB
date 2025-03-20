from django.db import models

# Model for Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    number_of_visits = models.IntegerField(default=0)
    number_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Model for Page
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='pages')
    title = models.CharField(max_length=200)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
