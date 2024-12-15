from django.contrib import admin
from .models import Coffe  

# Register your models here.
class CoffeAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')


admin.site.register(Coffe,CoffeAdmin)
