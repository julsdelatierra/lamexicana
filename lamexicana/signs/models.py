#encoding:utf-8
from django.db import models

class Sign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    date_creation = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return unicode(self.name)
