from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count
from .models import Account, JobApplication, NewsArticle
from .forms import AccountForm, JobApplicationForm
from collections import defaultdict


# Account Detail View
def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)

    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_detail", account_id=account.id)
    else:
        form = AccountForm(instance=account)

    return render(request, "account_detail.html", {"form": form, "account": account})

def add_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db')  # or wherever you want to go after adding
    else:
        form = AccountForm()
    return render(request, "add_account.html", {"form": form})

#orginal render only views
def index(request):
     return render(request,"index.html")

def db(request):
    accounts = Account.objects.all()
    industry_counts = (
        Account.objects.values('industry')
        .annotate(account_count=Count('id'))
        .order_by('-account_count')
    )
    return render(request, "db.html", {
        "accounts": accounts,
        "industry_counts": list(industry_counts),
    })

# News article view

def news_article(request, slug):
    article = get_object_or_404(NewsArticle, slug=slug)
    return render(request, "news_article.html", {"article": article})

def news_list(request):
    articles = NewsArticle.objects.order_by('-published')
    return render(request, "news_list.html", {"articles": articles})

# List all job applications
def jobs_list(request):
    jobs = JobApplication.objects.all()
    # Aggregate job counts by application_status
    stage_counts = (
        JobApplication.objects.values('application_status')
        .annotate(count=Count('id'))
        .order_by('application_status')
    )
    # Group jobs by application_status for Kanban
    kanban = defaultdict(list)
    for job in jobs:
        kanban[job.application_status or "Unknown"].append(job)
    kanban = dict(sorted(kanban.items()))
    accounts = Account.objects.all()
    return render(request, "jobs_list.html", {
        "jobs": jobs,
        "stage_counts": list(stage_counts),
        "kanban": kanban,  # Grouped jobs by status
        "accounts": accounts, # Pass accounts for potential use in the jobs_list.html template
    })

# Job application detail/edit views
def job_detail(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("job_detail", job_id=job.id)
    else:
        form = JobApplicationForm(instance=job)
    return render(request, "job_detail.html", {"form": form, "job": job})

