from django.urls import path
<<<<<<< HEAD
from .views import homepage, tempPage

urlpatterns = [
    path("",homepage, name="homepage" ),
    path("temp", tempPage, name="tempPage")
=======
from .views import homepage, stdid, collegeid, studentDataRetrivel

urlpatterns = [
    path("",homepage, name="homepage" ),
    path("stdid",stdid, name="stdid"),
    path("clgid",collegeid, name= "clgid"),
    path("studentData", studentDataRetrivel, name="studentdata")
>>>>>>> 5179bfe9b2a52f1fc5cf7ae8c2844c4cbb92c246
]
