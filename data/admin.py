from django.contrib import admin
from .models import *
class CallbackFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'subject',
        'is_done',
        'created_at',
    )

    list_filter = (
        'is_done',
    )
    model = CallbackForm


# admin.site.register(CallbackForm,CallbackFormAdmin)
admin.site.register(Currency)
admin.site.register(Sale)