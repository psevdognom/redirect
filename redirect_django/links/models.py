import random
import string

from django.db import models
from retry import retry

from redirect.settings import DOMAIN

class Link(models.Model):
    original_link = models.URLField()
    short_link = models.CharField(max_length=7, unique=True, blank=True, null=True)
    lifetime = models.DateTimeField(null=True, blank=True)

    @retry(tries=10)
    def save(self, **kwargs):
        self.short_link = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        if self.short_link == 'links':
            raise Exception()
        super().save(**kwargs)



