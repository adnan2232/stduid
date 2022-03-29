import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def homepage(req):
    return render(req, 'index.html')

def tempPage(req):
    return render(req, 'temp.html')

def stdid(req):
    return render(req,"stdid.html")

def collegeid(req):
    return render(req,"clgid.html")

def  studentDataRetrivel(req):
    body = json.loads(req.body)
    stateId = body["stateId"]
    uniId = body["uniId"]
    collegeId = body["collegeId"]
    grNo = body["grNo"]
    
    context = {
        "state": stateId,
        "uniId": uniId,
        "collegeId": collegeId,
        "grNo": grNo,
    }
    
    return JsonResponse(data=context, safe=False)

