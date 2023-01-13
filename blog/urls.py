from django.contrib import admin
from django.urls import path
from backend.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', joy),
    path('car/', car),
    path('ish/', ish),
    path('soqqa/', soqqa),
]
