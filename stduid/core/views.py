from django.shortcuts import render

# Create your views here.
def homepage(req):
    return render(req, 'index.html')
    
def stdid(req):
    return render(req,"stdid.html")

def collegeid(req):
    return render(req,"clgid.html")


