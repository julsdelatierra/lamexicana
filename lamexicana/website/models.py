#encoding:utf-8
from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    source = models.TextField()
    date_creation = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return unicode(self.title)
