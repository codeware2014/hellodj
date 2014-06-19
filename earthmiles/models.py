from django.db import models

# Create your models here.

from django.db import models


from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


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


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)
    owner = models.ForeignKey('auth.User',related_name='snippets')
    highlighted = models.TextField()


    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """

        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
