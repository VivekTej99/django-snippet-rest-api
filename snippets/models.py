from django.db import models
""" from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles """

# LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(0,'python'), (1, 'c language'),(2, 'java')])
STYLE_CHOICES = sorted([(0,'friendly'), (1,'tough'), (2,'stylish')])

class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

