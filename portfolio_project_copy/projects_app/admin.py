from django.contrib import admin

# Register your models here.
from projects_app.models import Project, About, Skills, Education, Certification, Work_experience

admin.site.register(Project)
admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Work_experience)