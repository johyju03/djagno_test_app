from django.contrib import admin
from .models import Fcuser


# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # admin 에서 표시할 컬럼


admin.site.register(Fcuser, FcuserAdmin)
