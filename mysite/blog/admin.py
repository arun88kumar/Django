from django.contrib import admin
from .models import EntryQuerySet, Entry

# Register your models here.
admin.site.register(Entry, EntryQuerySet)
