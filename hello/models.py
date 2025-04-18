from django.db import models

class Account(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False  # Because Heroku Connect creates this table, not Django
        db_table = 'account'
