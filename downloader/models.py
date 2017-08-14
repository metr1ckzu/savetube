from django.db import models


class Saver(models.Model):
    source_link = models.CharField(max_length=500)

    def __unicode__(self):
        return self.source_link
