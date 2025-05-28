from django.db import models

class Account(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

    class Meta:
        managed = False  # Because Heroku Connects creates this table, not Django
        db_table = 'account'

class JobApplication(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    application_status = models.CharField(max_length=255, db_column='application_status__c')
    # Add other fields as needed.

    class Meta:
        managed = False  # Heroku Connect manages this table
        db_table = 'job_application__c'
