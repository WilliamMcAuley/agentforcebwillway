from django.shortcuts import get_object_or_404, render, redirect
from .models import Account, JobApplication
from .forms import AccountForm, JobApplicationForm


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

#orginal render only views
def index(request):
     return render(request,"index.html")

def db(request):
     accounts = Account.objects.all()

     return render(request, "db.html", {"accounts": accounts})

# News article view

def news_article(request):
    return render(request, "news_article.html")

# List all job applications
def jobs_list(request):
    jobs = JobApplication.objects.all()
    return render(request, "jobs_list.html", {"jobs": jobs})

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

