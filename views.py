
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Account, Transaction

def home(request):
    # Retrieve user's accounts
    user_accounts = Account.objects.filter(user=request.user)
    return render(request, 'home.html', {'user_accounts': user_accounts})

def account_details(request, account_id):
    # Retrieve account details and transactions
    account = get_object_or_404(Account, pk=account_id)
    transactions = Transaction.objects.filter(account=account)
    return render(request, 'account_details.html', {'account': account, 'transactions': transactions})
