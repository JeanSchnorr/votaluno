from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'Administração votAluno'
admin.site.site_title = 'Administração votAluno'
admin.site.index_title = 'Administração votAluno'
admin.site.unregister(Group);