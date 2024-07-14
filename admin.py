
from django.contrib import admin
from .models import User, Account, Transaction




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'user', 'account_type', 'balance')
    list_filter = ('account_type',)
    search_fields = ('user__username', 'account_type')
    readonly_fields = ('account_id',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'account', 'transaction_type', 'amount', 'date')
    list_filter = ('transaction_type',)
    search_fields = ('account__user__username',)
    readonly_fields = ('transaction_id', 'date')
