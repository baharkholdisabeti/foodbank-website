
from django.contrib import admin
from .models import Branch, BranchNeed, Need

# Register your models here
admin.site.register(Branch)
admin.site.register(BranchNeed)
admin.site.register(Need)