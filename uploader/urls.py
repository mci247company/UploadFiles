from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('upload-multiple-files', views.upload_multiple_files, name='upload-multiple-files'),
]