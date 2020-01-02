from django.db import models

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site Url')

    def __str__(self):
        return  self.site_name + " , " +  self.url