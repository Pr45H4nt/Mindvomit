from django.contrib import admin
from .models import Posts , feedback

class post(admin.ModelAdmin):
    list_display = ('title' , 'content' , 'date')

admin.site.register(Posts,post)

class feedbackClass(admin.ModelAdmin):
    list_display = ('Name', 'contact', 'Email' , 'message')

admin.site.register(feedback,feedbackClass)
