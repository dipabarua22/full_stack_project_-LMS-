from django.contrib import admin


from . import models

admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.Lesson)
admin.site.register(models.Material)
admin.site.register(models.QuestionAnswer)
admin.site.register(models.Enrollment)

# Register your models here.
