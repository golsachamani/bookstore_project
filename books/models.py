from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length= 200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detai', args=[self.id])


class Comment(models.Model):
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete= models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    datetime_creat = models.DateTimeField(auto_now_add= True)
    is_active = models.BooleanField(default=True)
    recomend = models.BooleanField(default=True)

    def __str__(self):
        return self.text