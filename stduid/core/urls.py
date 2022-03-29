from django.urls import path
from .views import homepage, stdid, collegeid

urlpatterns = [
    path("",homepage, name="homepage" ),
    path("stdid",stdid, name="stdid"),
    path("clgid",collegeid, name= "clgid"),
    
]
