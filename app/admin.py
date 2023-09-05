from django.contrib import admin
from app.models import TODO
# Register your models here.

class TODOModel(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'due_date')
    
admin.site.register(TODO, TODOModel)
