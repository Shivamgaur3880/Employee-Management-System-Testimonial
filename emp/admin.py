from django.contrib import admin
from .models import employee,testimonial
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','emp_id','working')
    list_editable=('working',)
    list_filter=('working',)
    search_fields=('name',)
admin.site.register(employee,EmpAdmin)
admin.site.register(testimonial)