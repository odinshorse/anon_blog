from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

class Comments(models.Model):
    models.ForeignKey(Post)
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


