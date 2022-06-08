from django.urls import path
from triangles import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("a_types/", views.a_types, name="a_types"),
    path("t_types/", views.t_types, name="t_types"),
    path("t_area/", views.t_area, name="t_area"),
    path("contact/", views.contact, name="contact"),
    path("triangles/<name>", views.triangle_angles, name="Types of Angles"),
    path("students/", views.students, name="students"),
    path("add/", views.add, name="add"),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path("update/", views.update, name="update"),
    path('delete/<int:id>', views.delete, name='delete'),
]