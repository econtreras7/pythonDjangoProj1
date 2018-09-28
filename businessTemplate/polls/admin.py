from django.contrib import admin
from .models import Question
#making sure no one random can creste a queetion in our admin site

admin.site.register(Question)
# Register your models here.
