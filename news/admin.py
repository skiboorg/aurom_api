from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.safestring import mark_safe
from .models import *



class NewsItemAdmin(NestedModelAdmin):
    model = NewsItem

admin.site.register(NewsItem, NewsItemAdmin)