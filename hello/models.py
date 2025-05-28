from django.db import models

class Account(models.Model):
    id = models.IntegerField(primary_key=True)  # or CharField if using Salesforce IDs
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

    class Meta:
        managed = False  # Because Heroku Connects creates this table, not Django
        db_table = 'account'

class JobApplication(models.Model):
    id = models.IntegerField(primary_key=True)  # or CharField if using Salesforce IDs
    name = models.CharField(max_length=255)
    application_status = models.CharField(max_length=255, db_column='application_status__c')
    # Add other fields as needed.

    class Meta:
        managed = False  # Heroku Connect manages this table
        db_table = 'job_application__c'

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'news_article'
