from post import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path("add/", views.adding, name = 'add'),
    path("post/<slug>" , views.post),
    path('feedback', views.feedback, name= 'feedback'),
    path('about', views.about, name= 'about'),

]