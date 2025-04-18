from django.shortcuts import get_object_or_404,render,redirect

from .models import Account
from .forms import AccountForm


# Create your views here.
def account_detail(request,account_id):
     account = get_object_or_404(Account, id=account_id)

     if request.method == "Post":
          form = AccountForm(request.POST, instance=account)
          if form.is_valid():
               form.save()
               return redirect("account_detail", account_id=account.id)
     else:
          form = AccountForm(instance=account)

     return render(request, "account_detail.html", {"form": form,"account": account})
#orginal render only views
def index(request):
     return render(request,"index.html")

def db(request):
     accounts = Account.objects.all()

     return render(request, "db.html", {"accounts": accounts})

