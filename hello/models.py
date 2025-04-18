from django.db import models

class Account(models.Model):
    account_source = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    account_id = models.CharField(max_length=18, unique=True)
    industry = models.CharField(max_length=255)
    is_deleted = models.BooleanField()
    name = models.CharField(max_length=255)
    system_modstamp = models.DateTimeField()

    class Meta:
        db_table = '"salesforce"."Account"'
        managed = False             # Don't let Django manage this table (no migrations)
