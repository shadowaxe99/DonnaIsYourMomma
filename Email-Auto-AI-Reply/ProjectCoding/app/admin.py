
from django.contrib import admin
from .models import User, Payment, Data

# Register your models here.
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Data)
