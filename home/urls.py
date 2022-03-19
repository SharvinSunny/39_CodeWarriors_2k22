from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Animal Rescue Portal Admin"
admin.site.site_title = "Animal Rescue Portal"
admin.site.index_title = "Welcome to Animal Rescue Portal"

urlpatterns = [
    path("", views.index, name='home')
]