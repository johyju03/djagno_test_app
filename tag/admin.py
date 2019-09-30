from django.contrib import admin
from .models import Tag


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # admin 에서 표시할 컬럼


admin.site.register(Tag, TagAdmin)
