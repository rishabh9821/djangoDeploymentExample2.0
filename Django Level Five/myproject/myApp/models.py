from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING) ## Connects to auth user model

    ## Additional Class
    portfolioSite = models.URLField(unique = True, blank = True)
    profilePic = models.ImageField(upload_to = 'profilePics', blank = True)

    def __str__(self):
        return str(self.user.username)


