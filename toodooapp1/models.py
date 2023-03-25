from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class toodoo(models.Model):
    #host=
    #topic=
    toodooitem = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.toodooitem
    