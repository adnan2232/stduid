import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def homepage(req):
    return render(req, 'index.html')
<<<<<<< HEAD

def tempPage(req):
    return render(req, 'temp.html')
    
=======
    
def stdid(req):
    return render(req,"stdid.html")

def collegeid(req):
    return render(req,"clgid.html")

def  studentDataRetrivel(req):
    
    stateId = req.POST.get("stateId")
    uniId = req.POST.get("uniId")
    collegeId = req.POST.get("collegeId")
    grNo = req.POST.get("grNo")
    
    context = {
        "state": stateId,
        "uniId": uniId,
        "collegeId": collegeId,
        "grNo": grNo,
    }
    
    return JsonResponse(json.dumps(context), safe=False)

>>>>>>> 5179bfe9b2a52f1fc5cf7ae8c2844c4cbb92c246
