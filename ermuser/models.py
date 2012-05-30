import datetime
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')  

    def paco(self):
        return u'paco'

    def count_user_erms(self):
        return self.user.erms.count()

class Erm(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='erm_files')
    created_at = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User, related_name='erms')

    def __unicode__(self):
        return self.title
