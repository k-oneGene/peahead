from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Quotes(models.Model):
    name = models.CharField(max_length=120)
    quote = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    last_seen = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('brainfood:quotes_edit', kwargs={'pk': self.pk})

    def get_random(self):
        quote = Quotes.objects.order_by('?').first()
        return quote