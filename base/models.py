from django.db import models
from tinymce.models import HTMLField

POST_TYPES = (
    ('a', 'Software'),
    ('b', 'Books and essay'),
    ('c', 'Design projects'),
    ('d', 'Projects')
)

class Post(models.Model):
    headline = models.CharField(blank=True, max_length=100)
    body = HTMLField(blank=True)
    json_path = models.CharField(blank=True, max_length=50)
    image_path = models.CharField(blank=True, max_length=50)
    post_type = models.CharField(blank=False, choices=POST_TYPES, max_length='5')

    def __unicode__(self):
        return "{0} - {1}".format(self.headline, self.post_type)

class PostImage(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(blank=False, upload_to="images/")

class Event(models.Model):
    timestamp = models.DateField()
    short_desc = models.CharField(max_length=255)
    description = HTMLField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return "{0} - {1}".format(self.timestamp, self.short_desc)

    def is_short(self):
        return True if self.description else False