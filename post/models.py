from django.db import models
from django.utils import timezone
# Create your models he
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post-img/')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
