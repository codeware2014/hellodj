from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    post_code = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    last_log_in_datetime = models.DateTimeField()
    email = models.EmailField()


    def __str__(self):
        return  u'%s %s' % (self.first_name, self.last_name)



class User_Post(models.Model):
    post_title = models.CharField(max_length=100)
    feed_text = models.TextField(max_length=3000)
    user = models.ForeignKey(User)
    creation_time = models.DateTimeField(auto_now_add=True)