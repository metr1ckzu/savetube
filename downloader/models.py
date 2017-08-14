from django.db import models


class Saver(models.Model):
    source_link = models.CharField(max_length=500)
    creation_date = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.source_link
