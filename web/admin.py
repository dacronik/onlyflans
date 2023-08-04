from django.contrib import admin
from .models import Flan,ContactForm
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display= ["customer_name","customer_email","subject"]

class FlanProducto(admin.ModelAdmin):
    list_display=["name","slug","precio"]
    list_editable=["precio"]

admin.site.register(Flan,FlanProducto)
admin.site.register(ContactForm, ContactAdmin)
