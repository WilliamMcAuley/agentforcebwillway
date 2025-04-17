from django.db import models

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)



# New Account model
class Account(models.Model):
 account_source = models.CharField(max_length=255)
 created_date = models.DateTimeField()
 account_id = models.CharField(max_length=18, unique=True)
 industry = models.CharField(max_length=255)
 is_deleted = models.BooleanField()
 name = models.CharField(max_length=255)
 system_modstamp = models.DateTimeField()

# Updated JobApplication model
class JobApplication(models.Model):
 account = models.ForeignKey(Account, on_delete=models.CASCADE)
 application_status = models.CharField(max_length=255)
 created_date = models.DateTimeField()
 feedback = models.CharField(max_length=255)
 record_id = models.CharField(max_length=18, unique=True)
 is_deleted = models.BooleanField()
 name = models.CharField(max_length=80)
 source = models.CharField(max_length=255)
 system_modstamp = models.DateTimeField()
 job_application_id = models.FloatField(unique=True)
