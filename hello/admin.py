from django.contrib import admin
from .models import Account, JobApplication, NewsArticle

admin.site.register(Account)
admin.site.register(JobApplication)
admin.site.register(NewsArticle)
# Register your models here.
