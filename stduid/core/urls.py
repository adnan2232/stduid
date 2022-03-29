from django.urls import path
from .views import homepage, stdid, collegeid, studentDataRetrivel

urlpatterns = [
    path("",homepage, name="homepage" ),
    path("stdid",stdid, name="stdid"),
    path("clgid",collegeid, name= "clgid"),
    path("studentData", studentDataRetrivel, name="studentdata")
]
