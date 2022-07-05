from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class PostTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(null=True, upload_to="post_images/", blank=True)
    shorttext = models.TextField(null=True, blank=True, default=None)
    datetime = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(PostTag, related_name='tags')
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
