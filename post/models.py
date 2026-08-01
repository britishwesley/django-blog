from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)

    created_at = models.DateField(auto_now_add=True) #do it once when created
    created_at = models.DateField(auto_now=True) #do it everytime


    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True

    )

    