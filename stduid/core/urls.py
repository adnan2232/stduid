from django.urls import path
from .views import homepage, tempPage

urlpatterns = [
    path("",homepage, name="homepage" ),
    path("temp", tempPage, name="tempPage")
]
