from django.db import models


class Ansatt(models.Model):
    username = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20)
    is_it_hjelp = models.BooleanField(default=False)
    is_vaktleder = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f'{self.username}'
