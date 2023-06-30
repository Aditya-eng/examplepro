from django.urls import re_path
from exampleapp import views

urlpatterns = [

    re_path("",views.math_screenshot_file,name="math_screenshot_file"),

    re_path("",views.index,name="index"),
    re_path("",views.steve,name="steve"),
]