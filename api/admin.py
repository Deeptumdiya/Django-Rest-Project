from django.contrib import admin
from . models import MemberDetails, Members
# Register your models here.
admin.site.register(MemberDetails)
# Register models for admin panel
admin.site.register(Members)