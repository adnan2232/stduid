from dataclasses import field
from django.contrib import admin
from .models import State, University, College, Student
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    exclude = ("state_uid",)
    list_display = ("state_uid","state_name")
    
class UniversityAdmin(admin.ModelAdmin):
    exclude = ("uni_id","uni_uid")
    list_display = [field for field in University._meta.get_fields()]
    
admin.site.register(State, StateAdmin)
admin.site.register(University,UniversityAdmin)
admin.site.register(College)
admin.site.register(Student)