from django.db import models


class Ansatt(models.Model):
    username = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username} | {self.phone_number} | last updated: {self.last_updated}'
