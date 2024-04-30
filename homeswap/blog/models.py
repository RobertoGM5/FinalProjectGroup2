from django.db import models
from accounts.models import User, HomePhoto

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    max_capacity = models.PositiveIntegerField()
    to_city = models.CharField(max_length=100)
    date_period = models.DateField()
    num_travelers = models.PositiveIntegerField()
    description = models.TextField()
    home_photos = models.ManyToManyField('accounts.HomePhoto', related_name='blog_posts')
    

    def save(self, *args, **kwargs):
        self.location = self.user.location
        self.max_capacity = self.user.max_capacity
        super().save(*args, **kwargs)
