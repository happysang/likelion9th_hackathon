from inner_account.models import CustomUser
from django.contrib import admin

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'cert','ans_auth', 'date_joined']
    list_display_links = ['username']
    search_fields = ['username'] # 아이디로 검색 가능