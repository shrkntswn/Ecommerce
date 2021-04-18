from django.contrib import admin
from . models import *

class ContactAdmin(admin.ModelAdmin):
    model = Contact
    search_field = ('id', 'send_on')
    readonly_fields = ('name', 'email', 'subject', 'message')
    list_display = ('name', 'email', 'read')
    search_fields = ('name', 'email',)

admin.site.register(Contact, ContactAdmin,)
