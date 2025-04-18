from django.db import models

class Account(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    system_modstamp = models.DateTimeField()

    class Meta:
        managed = False  # Because Heroku Connect creates this table, not Django
        db_table = 'salesforce.account'
