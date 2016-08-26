from __future__ import unicode_literals

from django.db import models


class Party(models.Model):
    party_name = models.CharField(max_length=20)
    creation_date = models.DateTimeField('date created')

class Contact(models.Model):
    contact_name = models.CharField(max_length=20)
    creation_date = models.DateTimeField('date created')
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

