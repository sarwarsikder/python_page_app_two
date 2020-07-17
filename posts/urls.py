from django.urls import path
from .views import HopePageView

urlpatterns = [
    path('', HopePageView.as_view(), name='home')
]
