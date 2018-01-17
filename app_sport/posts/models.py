from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from groups.models import Group
import misaka

# Create your models here.


from django.conf import settings
try:
    from django.contrib.auth import get_user_model
    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User



class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts')
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField()
    group=models.ForeignKey(Group,related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username': self.user.username,'pk':self.pk})

    class Meta:
        ordering =['created_at']





