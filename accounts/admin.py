from .models import StudentProfile
from django.contrib import admin

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'phone', 'course', 'state', 'city', 'is_active_student')

    search_fields = (
        'id',                 # StudentProfile table id
        'user__id',           # User table id
        'user__username',     # username
        'user__first_name',   # first name
        'user__last_name',    # last name
    )

    list_filter = ('state', 'course', 'is_active_student')
