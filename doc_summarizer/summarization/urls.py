from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('upload_file/', views.upload_file, name="upload_file"),
    path('documents/', views.documents, name="documents"),
    path('about_us/', views.about_us, name="about_us"),
]