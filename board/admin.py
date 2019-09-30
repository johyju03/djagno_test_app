from django.contrib import admin
from .models import Board


# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)  # admin 에서 표시할 컬럼


admin.site.register(Board, BoardAdmin)
