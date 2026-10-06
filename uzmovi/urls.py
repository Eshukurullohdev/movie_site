from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('navigation/', navigation, name='navigation'),
    path('footer/', footer, name='footer')
]
