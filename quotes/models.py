from django.db import models
from django.core.exceptions import ValidationError

class Source(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Quote(models.Model):
    text     = models.TextField(unique=True)
    source   = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='quotes')
    weight   = models.PositiveIntegerField(default=1)
    views    = models.PositiveIntegerField(default=0)
    likes    = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def clean(self):
        if self.source.quotes.exclude(pk=self.pk).count() >= 3:
            raise ValidationError('У источника уже 3 цитаты.')

    def rating(self):
        return self.likes - self.dislikes
